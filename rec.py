import pickle
import pandas as pd

# Load saved files
similarity = pickle.load(open('similarity.pkl', 'rb'))
data = pickle.load(open('df.pkl', 'rb'))

def recommend(song_name, n_recommendations=20):
    # Check if song exists
    if song_name not in data['song'].values:
        return "Song not found in dataset."

    # Get index of the song
    idx = data[data['song'] == song_name].index[0]

    # Get similarity scores
    distances = list(enumerate(similarity[idx]))

    # Sort by similarity score (descending)
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    # Collect recommendations
    recommended_songs = []
    for i in distances[1:n_recommendations+1]:
        recommended_songs.append(data.iloc[i[0]].song)

    return recommended_songs

if __name__ == "__main__":
    song = input("Enter song name: ")
    recommendations = recommend(song)

    if isinstance(recommendations, list):
        print("\nRecommended Songs:")
        for i, s in enumerate(recommendations, 1):
            print(f"{i}. {s}")
    else:
        print(recommendations)
