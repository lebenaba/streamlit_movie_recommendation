import streamlit as st
from PIL import Image
import os



# Find and display image
st.image(Image.open(os.path.join(os.path.dirname(__file__), "..", "images", "movie_title_image.jpg")), caption=" ")#, width=650)
st.title("Movie Recommender System")

st.markdown("""
   
    Recommendation systems are important tools, enhancing customer experience and **boosting revenue** by providing personalized product or service suggestions, which **increase customer satisfaction**.  
    Our project focuses on developing a collaborative filtering-based movie recommendation system.  
    We utilized the MovieLens 25M dataset to train and evaluate various models.

    
    ### Introduction to the Project
    
    - **Collaborative Filtering**: The project employs collaborative filtering, focusing on similarities between users and items respectively to provide recommendations.
    - **Data Analysis and Preprocessing**: Initial data analysis and preprocessing were conducted to create a manageable dataset for further analysis and model building.
    - **Model Evaluation**: Various models were trained and fine-tuned, with the best-performing models evaluated for their effectiveness.
    - **Common Challenges**: 
        - **Data Sparcity**: Most users interact with only a small subset of items, making it challenging to find enough data to generate reliable recommendations.
        - **Scalability**: Computational complexity increases with growing database.
""", unsafe_allow_html=True)
