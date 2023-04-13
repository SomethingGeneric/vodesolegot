from translator import to_mandoa, to_english

while True:
    ct = input("m or e? : ")
    if ct == "e":
        english = input("> ")
        if " " in english:
            total = ""
            for word in english.split(" "):
                total += to_mandoa(word)
        else:
            total = to_mandoa(english)
        print(total)
    else:
        mandoa = input("> ")
        if " " in mandoa:
            total = ""
            for word in mandoa.split(" "):
                total += to_english(word)
        else:
            total = to_english(mandoa)
        print(total)