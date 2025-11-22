import pandas as pd
import json

keywords = json.load(open("rules/keywords.json"))

def detect_ledger(narration):
    n = narration.lower()
    for key, ledger in keywords.items():
        if key in n:
            return ledger
    return "Unknown Ledger"


def standard_parser(df):
    # Normalize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Identify typical bank columns
    date_col = next(c for c in df.columns if "date" in c)
    narr_col = next(c for c in df.columns if "narr" in c)
    debit_col = next(c for c in df.columns if "debit" in c or "withdraw" in c)
    credit_col = next(c for c in df.columns if "credit" in c or "deposit" in c)

    df["date"] = pd.to_datetime(df[date_col], errors="coerce").dt.strftime("%Y%m%d")
    df["narration"] = df[narr_col].astype(str)
    df["debit"] = pd.to_numeric(df[debit_col], errors="coerce").fillna(0)
    df["credit"] = pd.to_numeric(df[credit_col], errors="coerce").fillna(0)

    # Amount (positive = receipt, negative = payment)
    df["amount"] = df["credit"] - df["debit"]

    # Auto ledger detection
    df["ledger"] = df["narration"].apply(detect_ledger)

    return df[["date", "narration", "ledger", "amount", "debit", "credit"]]
