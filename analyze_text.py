# Remember to reach out for help after your own due diligence

def analyze_text(text):
    e = 0
    alphas = 0
    for char in text:
        if char == "e" or char == "E":
            e += 1
            alphas += 1
        elif char.isalpha() == True:
            alphas += 1
    calculation = round(((e/alphas) * 100), 2)
    percentage = "(" + str(calculation) + "%)"
    alphastr = str(alphas)
    estring = str(e)
    result = str("The text contains " + alphastr + " alphabetic characters, of which " + estring + " " + percentage + " are 'e'.")
    return result
