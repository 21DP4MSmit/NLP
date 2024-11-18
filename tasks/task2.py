from langdetect import detect

def main():
    texts = [
        "Šodien ir saulaina diena.",
        "Today is a sunny day.",
        "Сегодня солнечный день."
    ]
    
    for text in texts:
        language = detect(text)
        print(f"Teksts: '{text}' -> Valoda: {language}")
