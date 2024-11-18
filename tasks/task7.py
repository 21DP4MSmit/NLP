from gensim.models import Word2Vec

def main():
    sentences = [["māja", "ir", "liela"], ["dzīvoklis", "atrodas", "pilsētā"], ["jūra", "ir", "skaista"]]
    
    model = Word2Vec(sentences, vector_size=10, window=2, min_count=1, workers=4)
    word_vectors = model.wv
    
    print("Vārda 'māja' vektors:", word_vectors['māja'])
    print("Līdzība starp 'māja' un 'dzīvoklis':", word_vectors.similarity('māja', 'dzīvoklis'))
    print("Līdzība starp 'māja' un 'jūra':", word_vectors.similarity('māja', 'jūra'))
