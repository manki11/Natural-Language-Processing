from nltk.tokenize import sent_tokenize, word_tokenize

#Corpus - Body of text, singular. Corpora is the plural of this. Example: A collection of medical journals.
#Lexicon - Words and their meanings. Example: English dictionary. 
#Token - Each "entity" that is a part of whatever was split up based on rules. For examples, each word is a token when a sentence is "tokenized" into words.

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

#tokenizing by sentences
print(sent_tokenize(EXAMPLE_TEXT))