import streamlit as st
import pandas as pd

st.header('Preprocessing')

st.write("""
After selecting and merging the dataframes 'genome-scores', 'genome-tags', 'movies', and 'ratings' from the MovieLens 25M dataset, the following preprocessing steps were carried out:
""")

with st.expander('1. Filtering and Aggregating Tags'):
    st.write("""
    - Using the genome-scores, we sorted the tags by relevance in descending order.
    - We retained only the top 40 tags for each movie. 
    - Aggregating the 'relevance' and 'tag' values into lists, making the dataset more manageable and compact.
    """)

with st.expander('2. Word2Vec'):
    st.write("""
    - Trained a Word2Vec model on the aggregated tags to convert them into dense vector representations.
    - This transformation helped capture semantic relationships between tags and decreased the size of the dataset.
    """)

with st.expander('3. Cleaning up the Dataset'):
    st.write("""
    - Removed unnecessary columns.
    - Dropped rows with missing values.
    - Dropped outliers.
    - Converted data types of columns to optimize memory usage and processing efficiency.
    """)

with st.expander('4. Sampling'):
    st.write("""
    - Filtered out movies with fewer than 2000 ratings to focus on those with sufficient user interaction.
    - Using the logarithm function, we defined a custom sampling function, reducing the number of rows per movie proportional to the total number.
    - Applying the sampling function to each 'movieId' group resulted in a dataset with 5,273,559 entries.
    """)

st.write("""
The final dataset, approximately 301.8 MB in memory usage, was saved to CSV and Parquet and was then ready for further analysis and modeling.
""")
