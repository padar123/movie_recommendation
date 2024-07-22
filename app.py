import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=similar[index]
    recommeded_movies=[]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        recommeded_movies.append(movies.iloc[i[0]].title)
    return recommeded_movies



movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similar=pickle.load(open('similar.pkl','rb'))

st.title("MOVIE RECOMMENDATION SYSTEM")
option = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)
# st.button("Reset", type="primary")
if st.button("Recommend"):
    reco=recommend(option)
    for i in reco:
        st.write(i)
# else:
#     st.write("Goodbye")