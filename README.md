# Movie Recommender System

## Presentation and Installation

This repository contains the code for our project **Movie Recommendation System**, developed during our [Data Scientist training](https://datascientest.com/en/data-scientist-course) at [DataScientest](https://datascientest.com/).

The goal of this project is to create a recommendation system based on the MovieLens 25M dataset using collaborative filtering and model optimization through Deep Learning algorithms.

This project was developed by the following team :

- Lena Ametsbichler ([GitHub](https://github.com/) / [LinkedIn](https://www.linkedin.com/in/lena-ametsbichler/))
- Leonhard Löffler ([GitHub](https://github.com/) / [LinkedIn](www.linkedin.com/in/leonhard-loeffler))

You can browse and run the [notebooks](./notebooks). 

You will need to download the data from [MovieLens](https://files.grouplens.org/datasets/movielens/ml-25m.zip) and extract/save it to the directory data/raw:

├── data               <- Should be in your computer but not on Github (only in .gitignore)  
│   ├── dataframes     <- Pre-processed data for Streamlit app.  
│   ├── models         <- Pre-calculated models for Streamlit app.  
│   ├── processed      <- The final, canonical data sets for modeling; Should be on your computer but not on Github (only in .gitignore)  
│   └── raw            <- The original, immutable data dump; Should be on your computer but not on Github (only in .gitignore)  

You will need to install the dependencies (in a dedicated environment) :

```
pip install -r requirements.txt
```

## Streamlit App

```shell
conda create --name my-awesome-streamlit python=3.9
conda activate my-awesome-streamlit
pip install -r requirements.txt
streamlit run streamlit_presentation.py
```

The app should then be available at [localhost:8501](http://localhost:8501).

**How to use the app:**

- Navigate: Open your browser and enter the URL of the Streamlit app.
- Interact: Use the sidebar to navigate topics, adjust parameters and settings.
- View Output: The main area will display outputs like charts, tables, and text.
- Refresh: Streamlit updates in real-time; adjust inputs and observe changes immediately.

