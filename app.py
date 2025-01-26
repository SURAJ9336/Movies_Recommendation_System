#importing all reuired libraries
import streamlit as st
import pickle
import pandas as pd
import requests

#function to fetch similar movies
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# fetch poster  using API
def get_poster(title):
    url=f'https://www.omdbapi.com/?t={title}&apikey=14e005fd'
    response=requests.get(url)
    poster=response.json()['Poster']
    response=requests.get(poster)
    with open('image.jpg','wb')as f:
        f.write(response.content)

#loading dataset
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

#setting a frontend
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values,
)

if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        get_poster(i)
        st.image('image.jpg')
        st.write(i)

    