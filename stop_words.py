import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

stop_words= set(stopwords.words("English"))

words= word_tokenize(EXAMPLE_TEXT)

print(words)

filtered_sentence=[]

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)


