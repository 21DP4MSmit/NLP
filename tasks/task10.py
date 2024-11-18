from googletrans import Translator

def main():
    translator = Translator()
    texts = ["Labdien! Kā jums klājas?", "Es šodien lasīju interesantu grāmatu."]
    
    print("Tulkots teksts:")
    for text in texts:
        translation = translator.translate(text, src="lv", dest="en")
        print(f"Oriģinālais teksts: {text}")
        print(f"Angliski: {translation.text}")
