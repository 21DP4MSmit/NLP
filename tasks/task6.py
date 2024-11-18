import stanza

def main():
    stanza.download("lv")
    
    nlp = stanza.Pipeline("lv", processors="tokenize")
    
    text = (
        "Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru "
        "un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. "
        "Tā ir viena no Eiropas Savienības dalībvalstīm."
    )
    
    doc = nlp(text)
    sentences = [sentence.text for sentence in doc.sentences]
    
    summary = sentences[:1] + sentences[-1:]
    
    print("Kopsavilkums:")
    for sentence in summary:
        print(sentence)
