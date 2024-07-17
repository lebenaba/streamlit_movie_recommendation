import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go
import os

st.header('Results & Conclusion')

# counter for automated chart number updates
n_chart = 0

###################################################################################################
########################################### Methodology ###########################################
###################################################################################################

st.markdown('''
The methodology involved data preprocessing, exploratory analysis, and the implementation of both traditional and deep learning models. 
''')

###################################################################################################
####################################### Initial Model Comparison ###################################
####################################################################################################


st.markdown('''
Our **metric of choice** was MAE because it is easy to interpret, representing the average absolute deviation in the same units as the ratings, and it is less sensitive to outliers compared to metrics like RMSE.
''')

st.markdown('''
Our initial evaluation **without parameter tuning** showed that the SVD model performed best, followed closely by several KNN-based models. The NormalPredictor served as a benchmark and had significantly higher errors. The results indicated that matrix factorization and KNN models are promising for movie recommendations, even without optimization.
''')

# Data for the table
model_data = {
    "Metric": ["MAE"],
    "knnBasic": [0.7177],
    "knnMeans": [0.6538],
    "knnBaseline": [0.6527],
    "knnZScore": [0.6531],
    "SVD": [0.6515],
    "NMF": [0.6838],
    "NormalPredictor": [1.1537],
    "SlopeOne": [0.6619],
    "BaselineOnly": [0.6675],
    "CoClustering": [0.7125]
}

# Creating DataFrame and setting 'Metric' as the index
df_model = pd.DataFrame(model_data).set_index('Metric')

# Function to highlight the MAE row with dark green
def highlight_mae(row):
    return ['background-color: darkgreen; color: white' if row.name == 'MAE' else '' for _ in row]
styled_df = df_model.style.apply(highlight_mae, axis=1)

# Displaying the table in Streamlit
with st.expander('See performance metrics without parameter tuning'):
    st.dataframe(styled_df, use_container_width=True)



####################################################################################################
####################################### Parameter Tuning and CV ####################################
####################################################################################################

st.subheader('Parameter Tuning and Cross-Validation')

st.markdown('''
After **parameter tuning**, our models showed improved MAE and other performance metrics. We used GridSearchCV and RandomizedSearchCV to explore various hyperparameters and 5-fold cross-validation to ensure robustness.
''')

st.markdown('''
The following table also includes the results of the Neural Collaborative Filtering (NCF) model using only userId and movieId.
''')

# Data for the table
tuning_data = {
    "Metric": ["MAE"],
    "NCF DL": [0.6744],
    "knnBasic": [0.6674],
    "knnMeans": [0.6340],
    "knnBaseline": [0.6324],
    "knnZScore": [0.6330],
    "SVD": [0.6327],
    "NMF": [0.6679],
}

# Creating DataFrame and setting 'Metric' as the index
df_tuning = pd.DataFrame(tuning_data).set_index('Metric')

# Function to highlight the MAE row with dark green
def highlight_tuning(row):
    return ['background-color: darkgreen; color: white' if row.name == 'MAE' else '' for _ in row]
styled_df_tuning = df_tuning.style.apply(highlight_tuning, axis=1)

with st.expander('See detailed performance metrics after parameter tuning'):
    st.dataframe(styled_df_tuning, use_container_width=True)


###################################################################################################
################################### final results after NCF improvement ###########################
###################################################################################################


st.markdown('''
The NCF model was **enhanced by incorporating additional features**, such as tag embeddings and one-hot encoded genres. 
However, this did not improve the NCF model significantly. While the MAE showed a slight improvement, other metrics  showed reduced performance.
''')

st.markdown('''
The following table shows the results of the enhanced NCF model and the **top three performing models** as a end result.   
''')

# Data for the table
ncf_data = {
    "Metric": ["MAE"],
    "knnBaseline": [0.6324],
    "SVD": [0.6327],
    "knnZScore": [0.6330],
    "NCF (all features)": [0.6681],
}

# Creating DataFrame and setting 'Metric' as the index
df_ncf = pd.DataFrame(ncf_data).set_index('Metric')

# Function to highlight the MAE row with dark green
def highlight_ncf(row):
    return ['background-color: darkgreen; color: white' if row.name == 'MAE' else '' for _ in row]
styled_df_ncf = df_ncf.style.apply(highlight_ncf, axis=1)

# Displaying the table in Streamlit
with st.expander('See detailed performance metrics of the NCF model and top 3 performing models'):
    st.dataframe(styled_df_ncf, use_container_width=True)



###################################################################################################
################################### Precision@k and Recall@k ######################################
###################################################################################################

# Muss hier was hin?

###################################################################################################
############################################ Learnings ############################################
###################################################################################################

st.subheader('Learnings')
st.markdown('''
- **Model Performance**: Traditional collaborative filtering techniques, particularly matrix factorization (SVD) and KNN-based models, provided robust performance. 
- **Metrics**: The MAE values indicated that predicted ratings were, on average, within 0.63 of the actual ratings, which are satisfying results.
- **Parameter Tuning**: GridSearchCV improved the performance of some models, but not by a large amount.
- **Deep Learning**: While the NCF model showed potential, it did not perform as well as classical methods.


Future work could focus on further refining deep learning models, integrating interpretability techniques and conducting a more exhaustive grid search for better performance.
''')
