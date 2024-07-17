import streamlit as st
from PIL import Image
import os

st.header('Advanced Models')
st.write("""
    We implemented a Neural Collaborative Filtering (NCF) model for collaborative filtering tasks to improve predictive performance.

    ### Neural Collaborative Filtering

    - **Embeddings**: 
        - User and item IDs were transformed into dense vectors using embedding layers.
        - Tags were also converted into embeddings using a Word2Vec model.
    
    - **Model Architecture**:
        - User and item embeddings were flattened and concatenated with additional features.
        - The combined inputs were passed through dense layers with ReLU activations.
        - Dropout layers were used to prevent overfitting.
        - The model was compiled with the Adam optimizer and MAE as the loss function.
        
""")

with st.expander("Model Architecture NCF"):
    st.image(Image.open(os.path.join(os.path.dirname(__file__), "..", "images", "ncf_img.png")), caption="NCF Model Architecture", width=600)

st.write("""
    - **Hyperparameter Tuning**:
        - RandomizedSearchCV explored different hyperparameters (embedding dimensions, dropout rates, dense layer units, learning rates, regularization) on 10% of data.
        - The best hyperparameters were used to train the final model.
        - Best results were obtained after 14 epochs.
""")
   
# Find and display image
with st.expander("Training and Validation Loss"):
    st.image(Image.open(os.path.join(os.path.dirname(__file__), "..", "images", "img3.jpg")), caption=" ", width=550)

st.write("""   
    ### Learnings
    - The NCF model showed promising results but requires further refinement.
    - Including additional features like tag embeddings and one-hot encoded genres improved performance slightly, with mixed results.
""")