from wordfreq import zipf_frequency
import spacy
import numpy as np
import pandas as pd
from googletrans import Translator
translator = Translator()

# from spacy import displacy
# from collections import Counter
spacy.load('es_core_news_md')

ignored_pos_tags = ['PUNCT', 'SPACE', 'SYM', 'X', 'PROPN', 'NUM']

# Load the data
nlp = spacy.load('es_core_news_md')
text = open('./words.txt').read()
doc = nlp(text)

# construct a dataframe
words = [(
    token.text,
    token.lemma_,
    token.pos_,
) for token in doc]
df = pd.DataFrame(words, columns=['word', 'lemma', 'pos_tag', ])
df['frequency'] = df['lemma'].apply(
    lambda word: zipf_frequency(word, "es", wordlist='best', minimum=0.0))
df['included'] = df['frequency'].apply(lambda freq: freq < 4)
sorted = df.sort_values(by=['frequency'], ascending=False)
filtered = sorted[
    (sorted['pos_tag'].isin(ignored_pos_tags) == False)
    # & (sorted['word'] != '-')
]

target_words = filtered[filtered['included'] == True][['lemma']]
target_words['translation'] = target_words['lemma'].apply(
    lambda word: translator.translate(word, src='es', dest='en').text)
csv = target_words.to_csv('./target_words.csv', index=False)
print(target_words)

# words = [
#     ('hacer'),
#     ('hacer'),
#     ]
# df = pd.DataFrame(words, columns=['word'])
# df['translation'] = df['word'].apply(lambda word:translator.translate(word, src='es', dest='en').text)
# df['translation'] = df['word'].apply(lambda word: translator.translate(word, src='es', dest='en').text)
# print(df)
# translations = [token.text for token in doc]
