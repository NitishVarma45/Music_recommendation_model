import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
import pickle

nltk.download('punkt_tab')

data = pd.read_csv('spotify_millsongdata.csv')
data.drop(columns='link', inplace=True)

data = data

data['text'] = (
    data['text']
    .str.lower()
    .replace(r'[^\w\s]', ' ', regex=True)
    .replace(r'\n', ' ', regex=True)
)

stemmer = PorterStemmer()

def tokenization(txt):
    tokens = nltk.word_tokenize(txt)
    return " ".join(stemmer.stem(w) for w in tokens)

data['text'] = data['text'].apply(tokenization)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidvector = TfidfVectorizer(stop_words='english')
matrix = tfidvector.fit_transform(data['text'])
similarity = cosine_similarity(matrix)

pickle.dump(similarity, open('similarity.pkl','wb'))
pickle.dump(data, open('df.pkl','wb'))
