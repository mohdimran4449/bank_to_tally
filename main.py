import PySimpleGUI as sg
from parser import parse_statement
from tally import send_to_tally
import pandas as pd

sg.theme("DarkBlue3")

layout = [
    [sg.Text("Bank → Tally Import Tool", font=("Arial", 16))],
    [sg.Text("Select Bank Statement (PDF/CSV/Excel):")],
    [sg.Input(key="-FILE-"), sg.FileBrowse()],
    [sg.Button("Process"), sg.Button("Send to Tally"), sg.Button("Exit")],
    [sg.Output(size=(100, 25))]
]

window = sg.Window("Bank to Tally Automation", layout)

df_global = None

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "Process":
        try:
            file_path = values["-FILE-"]
            print("Processing:", file_path)
            df_global = parse_statement(file_path)
            print(df_global.head())
            print("\nParsing Completed Successfully.\n")
        except Exception as e:
            print("Error:", str(e))

    if event == "Send to Tally":
        if df_global is None:
            print("No data to send. Process a file first.")
        else:
            try:
                print("Sending vouchers to Tally...")
                send_to_tally(df_global)
                print("\nDONE — All vouchers sent successfully.")
            except Exception as e:
                print("Error:", str(e))

window.close()
