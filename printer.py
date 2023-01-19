import cups

PRINTER_NAME = "Epson"

conn = cups.Connection()

def print(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    
    new_text = ""
    count = 0
    for char in text:
        new_text += char
        count += 1
        if count % 25 == 0:
            new_text += "\n"
    conn.printFile(PRINTER_NAME, new_text, "", {})
    