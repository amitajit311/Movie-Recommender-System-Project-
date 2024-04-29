import streamlit as st
import  pickle
import  pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarty[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies =[]

    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarty = pickle.load(open('simlarty.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'would you like to be connected',
    movies['title'].values
)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)