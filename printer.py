import cups

PRINTER_NAME = "Epson"

conn = cups.Connection()

def print(file_name):
    conn.printFile(PRINTER_NAME, file_name, "", {})
    