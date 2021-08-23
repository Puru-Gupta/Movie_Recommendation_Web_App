import pandas as pd
import streamlit as st
import pickle
base="light"
def recommend(movie):
    index = moviess[moviess['title'] == movie].index[0]
    distances = simil_dist[index]
    moviess_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in moviess_list:
        recommended_movies.append(moviess.iloc[i[0]].title)
    return recommended_movies


moviedict = pickle.load(open('Suggest13.pkl','rb'))
moviess = pd.DataFrame(moviedict)


simil_dist = pickle.load(open('simil_dist.pkl','rb'))

st.title('Movie Recommendation system')



selected_movie_name = st.sidebar.selectbox(
 'How would you like to be contacted?',
moviess['title'].values)

if st.button('Recommend'):
    recomme = recommend(selected_movie_name)
    for i in recomme:
        st.write(i)

st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

