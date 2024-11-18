from textblob import TextBlob

def main():
    texts = [
        "Šis produkts ir lielisks, esmu ļoti apmierināts!",
        "Esmu vīlies, produkts neatbilst aprakstam.",
        "Neitrāls produkts, nekas īpašs."
    ]
    
    for text in texts:
        sentiment = TextBlob(text).sentiment.polarity
        if sentiment > 0:
            mood = "Pozitīvs"
        elif sentiment < 0:
            mood = "Negatīvs"
        else:
            mood = "Neitrāls"
        print(f"Teksts: '{text}' -> Noskaņojums: {mood}")
