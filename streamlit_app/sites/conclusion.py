import streamlit as st

st.header('Conclusion & Outlook')

st.write("""
        
    **Key Takeaways:**
    - **Traditional Models**: Collaborative filtering techniques, particularly matrix factorization (SVD) and KNN-based models, demonstrated robust performance. Hyperparameter tuning further improved these models.
    - **Deep Learning Models**: The NCF model showed potential but needs more sophisticated techniques to potentially achieve better results.
    - **Model Evaluation**: The best models provided reasonably close predictions, making them useful for generating relevant movie recommendations.
""")

st.write("""
**Final Thoughts:**

The results highlight the effectiveness of traditional collaborative filtering techniques when adequately tuned and optimized. Despite the challenges encountered, including handling large datasets and computational complexities, the models developed provide accurate and relevant movie recommendations.

Future work could focus on further refining deep learning models, integrating interpretability techniques and conducting a more exhaustive grid search for better performance
""")
