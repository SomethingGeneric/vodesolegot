# stdlib
import os,sys

# pip
import xlrd

if not os.path.exists("MandoaApril09.xls"):
    print("Please download the data from https://web.archive.org/web/20120402102936/http://www.karentraviss.com/page20/page26/downloads/files/MandoaApril09.xls")
    sys.exit(1)

book = xlrd.open_workbook("MandoaApril09.xls")
sheet = book.sheet_by_index(0)

start_english = 2
stop_english = 1186 # pre +1'd

def to_mandoa(english_text):
    suggestions = []
    for r in range(start_english, stop_english):
        meaning = sheet.cell_value(rowx=r, colx=2)
        if " " in meaning:
            for word in meaning.split(" "):
                if word == english_text:
                    mandoa = sheet.cell_value(rowx=r, colx=0)
                    print(f"Maybe: {mandoa} -> {meaning}")
                    suggestions.append([mandoa, meaning])
        elif english_text in meaning:
            mandoa = sheet.cell_value(rowx=r, colx=0)
            print(f"Maybe: {mandoa} -> {meaning}")
            suggestions.append([mandoa, meaning])
    return suggestions

def to_english(mandoa_text):
    suggestions = []
    for r in range(start_english, stop_english):
        this_mandoa = sheet.cell_value(rowx=r, colx=0)
        if " " in this_mandoa:
            for word in this_mandoa.split(" "):
                if word == mandoa_text:
                    english = sheet.cell_value(rowx=r, colx=2)
                    print(f"Maybe: {this_mandoa} -> {english}")
                    suggestions.append([this_mandoa, english])
        elif mandoa_text in this_mandoa:
            english = sheet.cell_value(rowx=r, colx=2)
            print(f"Maybe: {this_mandoa} -> {english}")
            suggestions.append([this_mandoa, english])
    return suggestions