try:
    letters = {
        "a": "c",
        "b": "d",
        "c": "e",
        "d": "f",
        "e": "g",
        "f": "h",
        "g": "i",
        "h": "j",
        "i": "k",
        "j": "l",
        "k": "m",
        "l": "n",
        "m": "o",
        "n": "p",
        "o": "q",
        "p": "r",
        "q": "s",
        "r": "t",
        "s": "u",
        "t": "v",
        "u": "w",
        "v": "x",
        "w": "y",
        "x": "z",
        "y": "a",
        "z": "b"
    }

    string = input("enter the string:").lower()
    output = ""

    for i in string:
        for key, value in letters.items():
            if i == key:
                output += value
        if i == " ":
            output += " "
    print(output)
except Exception as e:
    print("error:",e)
