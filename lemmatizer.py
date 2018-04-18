import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet


# to convert pos_tag to compatible wordnet tags
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

lemmatizer= WordNetLemmatizer()
example_text= "I like to play. I played yesterday. I am playing right now. He plays soccer"
tokenized= sent_tokenize(example_text)

def process_content():
    try:
        for i in tokenized:
            words= nltk.word_tokenize(i)
            tagged= nltk.pos_tag(words)

            for i, w in enumerate(words):
                print(lemmatizer.lemmatize(w, get_wordnet_pos(tagged[i][1])))

    except Exception as e:
        print(str(e))

process_content()