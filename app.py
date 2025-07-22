import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8007af338d1bcfdce87ca8672cee27da&language=en-US'
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch poster for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Image+Not+Available"



def recommender(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movie_lists = pickle.load(open('movie.dict.pkl','rb'))
movies = pd.DataFrame(movie_lists)
st.title("MovieMesh")
similarity=pickle.load(open("similarity.pkl","rb"))

selected_movie_name = st.selectbox(
    'What movie you want to watch?',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommender(selected_movie_name)

    # Define the number of columns you want per row
    num_columns_per_row = 5
    
    # Iterate through the recommendations and display them in columns
    for i in range(0, len(names), num_columns_per_row):
        cols = st.columns(num_columns_per_row) # Create a new row of columns

        for j in range(num_columns_per_row):
            if i + j < len(names):  # Check if there's a movie to display
                with cols[j]:
                    st.text(names[i+j])
                    st.image(posters[i+j])

