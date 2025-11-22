# bank_to_tally

Utility to parse bank statements and convert entries for import into Tally.

Repository created and initialized using an automated workflow.

## Windows: how to give the .exe to a friend

The repository's CI builds a Windows executable and publishes it as a Release asset.

Steps for your friend to run the app on Windows:

1. Download the latest Windows release from:
	 https://github.com/mohdimran4449/bank_to_tally/releases

2. Extract (if it's zipped) and run `bank_to_tally-windows.exe`.

Prerequisites and notes:

- Tesseract OCR: this app uses `pytesseract` which requires the Tesseract binary installed on the Windows machine.
	- Download & install from: https://github.com/tesseract-ocr/tesseract/releases
	- Add the Tesseract install folder (e.g., `C:\\Program Files\\Tesseract-OCR`) to the Windows PATH so `pytesseract` can find it.

- ODBC / Database drivers: if the app uses `pyodbc` to send data to Tally or other DBs, the appropriate ODBC drivers must be installed on the Windows machine.

- Antivirus / SmartScreen: some self-built executables may trigger warnings on first run. If the exe is blocked, try allowing it or mark as safe in the AV console.

- Architecture: the CI builds on `windows-latest` (x86_64). Make sure the target machine is compatible.

If you want me to make the .exe more portable (bundle Tesseract, or produce an installer), tell me which option you'd like and I will add that to CI.

