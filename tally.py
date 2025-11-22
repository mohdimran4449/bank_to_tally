import requests

TALLY_URL = "http://localhost:9000"

def voucher_xml(row):
    if row["amount"] > 0:
        vtype = "Receipt"
    else:
        vtype = "Payment"

    amount = row["amount"]

    xml = f"""
    <ENVELOPE>
     <HEADER>
      <TALLYREQUEST>Import Data</TALLYREQUEST>
     </HEADER>
     <BODY>
      <IMPORTDATA>
       <REQUESTDESC>
        <REPORTNAME>Vouchers</REPORTNAME>
       </REQUESTDESC>
       <REQUESTDATA>
        <TALLYMESSAGE>
         <VOUCHER VCHTYPE="{vtype}" ACTION="Create">
           <DATE>{row['date']}</DATE>
           <NARRATION>{row['narration']}</NARRATION>
           
           <LEDGERENTRIES.LIST>
             <LEDGERNAME>{row['ledger']}</LEDGERNAME>
             <AMOUNT>{amount}</AMOUNT>
           </LEDGERENTRIES.LIST>

           <LEDGERENTRIES.LIST>
             <LEDGERNAME>Bank</LEDGERNAME>
             <AMOUNT>{-amount}</AMOUNT>
           </LEDGERENTRIES.LIST>

         </VOUCHER>
        </TALLYMESSAGE>
       </REQUESTDATA>
      </IMPORTDATA>
     </BODY>
    </ENVELOPE>
    """
    return xml


def send_to_tally(df):
    for _, row in df.iterrows():
        xml = voucher_xml(row)
        resp = requests.post(TALLY_URL, data=xml.encode("utf-8"))
        print("Tally Response:", resp.text)
