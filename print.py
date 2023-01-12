import cups

PRINTER_NAME = "Epson"

conn = cups.Connection()

input("Press enter to print")

conn.printFile(PRINTER_NAME, "test.txt", "", {})
# conn.printFile(PRINTER_NAME, "example.pdf", "", {})

input("Printing... hit enter to continue")
