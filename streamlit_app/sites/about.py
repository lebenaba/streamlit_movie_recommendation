import streamlit as st

st.title('About')

st.subheader('Contributors')
box =  st.container(border=True)
box.write('Lena Ametsbichler [LinkedIn](https://www.linkedin.com/in/lena-ametsbichler/)')
box.write('Leonhard Löffler [LinkedIn](https://www.linkedin.com/in/leonhard-loeffler/)')

st.subheader('Mentor')
box =  st.container(border=True)
box.write('Roseline Polle [LinkedIn](https://www.linkedin.com/in/roseline-polle-68559762/)')

st.subheader('References')

ref_ML25m = "F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872"
ref_Surprise = "Hug, N., (2020). Surprise: A Python library for recommender systems. Journal of Open Source Software, 5(52), 2174, https://doi.org/10.21105/joss.02174"

box =  st.container(border=True)
box.markdown('###### MovieLens 25M dataset:')
box.markdown(ref_ML25m)
box.markdown('###### Surprise library:')
box.write(ref_Surprise)
box.markdown("""
###### Title image credit:
https://pixabay.com/illustrations/ai-generated-movie-theater-8848753/
             """)
