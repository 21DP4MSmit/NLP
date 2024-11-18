import stanza

def main():
    stanza.download("lv")

    nlp = stanza.Pipeline("lv", processors="tokenize,ner")

    text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."
    
    doc = nlp(text)

    print("Identificētās vienības:")
    for sentence in doc.sentences:
        for entity in sentence.ents:
            print(f"Vienība: {entity.text}, Tips: {entity.type}")
