import streamlit as st
import pickle
import pandas as pd
database = pickle.load(open('data/movies.pkl', 'rb'))
# Load split similarity matrices and combine them
similarity_part1 = pickle.load(open('data/similarity_pt1.pkl', 'rb

def recommend(movie):
	movie_index = database[database['title'] == movie].index[0]
	distances = similarity[movie_index]
	movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

	return [database['title'][i[0]] for i in movie_list]


st.title('Movie Recommender System')

st.selectbox('Select a movie', database['title'].values, key='movie')

if st.button('Recommend'):
	recommendations = recommend(st.session_state.movie)
	for i in recommendations:
		st.write(i)