import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps= PorterStemmer()

# example using words
'''
example_words=["google", "googler", "googling", "googlon"]

for w in example_words:
    print(ps.stem(w))
    
'''

# example using a sentence

example_text= "This is me studying . I also study. I also play. I am playing. I studied last night"

words= word_tokenize(example_text)

for w in words:
    print(ps.stem(w))