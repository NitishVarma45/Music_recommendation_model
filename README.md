This project is a content-based music recommendation system that recommends songs based on the similarity of song lyrics.
It uses Natural Language Processing (NLP) techniques to understand lyrical content and suggest similar songs.
Song lyrics are cleaned and preprocessed (lowercasing, tokenization, stemming).
Lyrics are converted into numerical vectors using TF-IDF.
Cosine similarity is used to measure similarity between songs.
Given a song name, the system recommends the most similar songs based on lyrics.
Step 1: Run Preprocessing (One Time Only)
python clean.py
This generates:
similarity.pkl
df.pkl
Step 2: Get Recommendations
python rec.py
Enter a song name when prompted to receive recommendations.
