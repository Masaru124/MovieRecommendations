import streamlit as st
import pandas as pd
import pickle

with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies.iloc[movie_indices]

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Select a movie you like:", movies['title'].values)

if st.button('Get Recommendations'):
    st.markdown("### Top 10 Recommended Movies:")
    recommendations = get_recommendations(selected_movie)
    
    for idx, row in recommendations.iterrows():
        st.markdown(f"- **{row['title']}**")
