import pandas as pd
import os
import pdfplumber
from banks.standard import standard_parser

def parse_statement(path):
    ext = os.path.splitext(path)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(path)
        return standard_parser(df)

    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(path)
        return standard_parser(df)

    elif ext == ".pdf":
        return parse_pdf(path)

    else:
        raise Exception("Unsupported file format.")


def parse_pdf(path):
    rows = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                rows.extend(table)

    if not rows:
        raise Exception("No tables found in the PDF.")

    df = pd.DataFrame(rows[1:], columns=rows[0])
    return standard_parser(df)
