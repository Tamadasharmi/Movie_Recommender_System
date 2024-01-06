import streamlit as st
import pickle
import pandas as pd
import requests


def recommend(movie):
    mov_index = movies[movies['title'] == movie].index[0]
    dist = sorted(list(enumerate(similarity[mov_index])), reverse=True, key=lambda x: x[1])[1:11]
    r=[]
    for i in dist:
        movie_id=i[0]

        r.append(movies.iloc[i[0]].title)
    return r
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name =st.selectbox(
    'Search a movie',
    movies['title'].values
    )
if st.button('Recommend'):
    rr=recommend(selected_movie_name)
    for i in rr:
         st.write(i)