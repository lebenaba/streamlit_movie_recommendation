import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
movie_rec_path = os.getenv('MOVIE_REC_PATH')

current_dir = os.path.dirname(__file__)

st.header('Data Exploration')

######################################################################################################
######################################## introduction dataset ########################################
######################################################################################################

st.subheader('The MovieLens 25M Dataset')

movielens_data = {"Description": ["Ratings", "Movies", "Users", "Tags added"],
                  "Number of data": ["25 million", "62,000", "162,000", "1.1 million times"]}
df_movielens = pd.DataFrame(movielens_data)
st.dataframe(df_movielens, hide_index=True)

st.markdown('''
            - Open Source dataset provided by [GroupLens](https://grouplens.org/)
            - Time frame covered: January 1995 - November 2019
            - Each rating of a user ranges from 0.5 to 5.0 stars.
            - Free-text tagging provided by users, enhances the descriptive power of the dataset.
            ''')

# ml = pd.DataFrame({"table name": ['movies.csv','links.csv','ratings.csv','tags.csv','genome-scores.csv','genome-tags.csv'],
#                   "columns": ['movieId, title, genres','movieId, imdbId, tmdbId','userId, movieId, rating, timestamp','userId, movieId, tag, timestamp','movieId, tagId, relevance','tagId, tag'],
#                   "length": [62423,62423,25000095,1093360,15584448,1128]})
#                 #   "length": ['62,423','62,423','25,000,095','1,093,360','15,584,448','1,128']})
                  
# st.dataframe(ml, hide_index=True)

######################################################################################################
######################################## loading data, images ########################################
######################################################################################################

@st.cache_data
def load_df_movies():
    # df = pd.read_csv('../../movie_recommendation/data/raw/ml-25m/movies.csv')
    df = pd.read_csv(f'{movie_rec_path}/data/raw/ml-25m/movies.csv')
    os.getenv('MOVIE_REC_PATH')
    return df
df_movies = load_df_movies()

with st.expander('See example of movie data'):
    st.dataframe(df_movies.head(), hide_index=True)

# hot-one encoding to split genres in separate columns using pandas strin method
df_movies = pd.concat([df_movies, df_movies['genres'].str.get_dummies(sep='|')], axis=1)
# removing unnecessary columns
df_movies.drop(['title','genres'], axis=1, inplace=True)
# rename column to avoid spaces
df_movies.rename(columns={'(no genres listed)':'no_genre_listed'}, inplace=True)

frequency_genres = df_movies.iloc[:,1:].sum()

# @st.cache_data
# def load_genre_ratings():
#     df = pd.read_parquet('../data/dataframes/genre_ratings.parquet.gzip')
#     return df
# genre_ratings = load_genre_ratings()

# @st.cache_data
# def load_user_rating_avg():
#     df = pd.read_parquet('../data/dataframes/user_rating_avg.parquet.gizp')
#     return df
# user_rating_avg = load_user_rating_avg()

user_rating_avg_path = os.path.join(current_dir, "..","..", "data", "dataframes", "user_rating_avg.parquet.gizp")
user_rating_avg = pd.read_parquet(user_rating_avg_path)

# @st.cache_data
# def load_user_rating_sum():
#     df = pd.read_parquet('../data/dataframes/user_rating_sum.parquet.gizp')
#     return df
# user_rating_sum = load_user_rating_sum()
# user_rating_sum = pd.read_parquet('../../data/dataframes/user_rating_sum.parquet.gizp')

user_rating_sum_path = os.path.join(current_dir, "..","..", "data", "dataframes", "user_rating_sum.parquet.gizp")
user_rating_sum = pd.read_parquet(user_rating_sum_path)

# df_rat = user_rating_avg.merge(right=user_rating_sum, on='userId', how='outer')
# df_rat.rename(columns={'n_movies':'n_ratings'}, inplace=True)

# genre_ratings = pd.read_parquet('../data/dataframes/genre_ratings.parquet.gzip')
# user_rating_avg = pd.read_parquet('../data/dataframes/user_rating_avg.parquet.gizp')
# user_rating_sum = pd.read_parquet('../data/dataframes/user_rating_sum.parquet.gizp')

stat_user_rating_sum = user_rating_sum.describe()
stat_user_rating_avg = user_rating_avg.describe()

stat_user_tag_movie = pd.DataFrame({'n_tags': [305356.000000,3.580555,4.247787,0.000000,1.000000,2.000000,4.000000,337.000000]}, index=['count','mean','std','min','25%','50%','75%','max'])


### definition of table style / highlight

def higlight_mmm(s):
    is_min = s.index == 'min'
    is_median = s.index == '50%'
    is_max = s.index == 'max'
    return ['background-color: lightblue' if m else 'background-color: lightblue' if n else 'background-color: lightblue' if o else '' for m,n,o in zip(is_min, is_median, is_max)]

styled_stat_user_rating_sum = stat_user_rating_sum.style.apply(higlight_mmm, axis=0)
styled_stat_user_rating_avg = stat_user_rating_avg.style.apply(higlight_mmm, axis=0)

styled_stat_user_tag_movie = stat_user_tag_movie.style.apply(higlight_mmm, axis=0)

#####################################################################################################
#################################### charts calculation / import ####################################
#####################################################################################################

# pie chart Proportion of genres
fig_pie = go.Figure()
fig_pie.add_trace(go.Pie(labels=frequency_genres.index, values=frequency_genres, direction='clockwise'))
fig_pie.update_layout(legend_title = 'Genres', title='Proportions of genres', title_x=0.45, title_y=0.95)
fig_pie.update_layout(autosize=False, width=600, height=600)

# # build and cache boxplot of rating distribution per genre
# @st.cache_data
# def build_chart_box():
#     fig_box = plt.figure(figsize=(10, 6))
#     sns.boxplot(genre_ratings.replace({0:np.nan}).iloc[:,1:-2], fliersize=1)
#     plt.title('Distribution movie rating per genre')
#     plt.xticks(rotation=75);
#     return fig_box
# fig_box = build_chart_box()

# build and cache scatterplot avg rating vs. number ratings
# st.cache_data
# def build_chart_scatter1():
    # fig_scatter_rating = plt.figure(figsize=(10, 5))
    # sns.scatterplot(x=df_rat.n_ratings, y=df_rat.avg_rating, hue=df_rat.avg_rating, size=10, legend=False)
    # plt.plot([0,6000],[5,5], c='red', alpha=0.6)
    # plt.xlim([0,10000])
    # plt.title('Average rating over number of ratings a user gave')
    # plt.xlabel('number of ratings')
    # plt.ylabel('average rating');
#     return fig
# fig_scat1 = build_chart_scatter1

### display of charts

######################################################################################################
################################ display statistics and visualization ################################
######################################################################################################

st.subheader('Statistics and data visualization')

# checkbox for displaying plots
with st.expander('See genre analysis'):
    st.markdown('#### Genre distribution and rating')
    st.plotly_chart(fig_pie)
    st.image(Image.open(os.path.join(os.path.dirname(__file__), "..", "images", "distribution_movie_rating_genre.png")))

with st.expander('See rating analysis'):
    st.markdown('#### Rating behaviour')
    st.markdown('**Basic statistics**')

    left_column, right_column = st.columns(2)
    left_column.write('Number of movies rated by each user:')
    left_column.table(styled_stat_user_rating_sum)

    right_column.write('Average rating per user:')
    right_column.table(styled_stat_user_rating_avg)

    st.write('In the following scatter plot each point represents a user. For better readability one user with about 32.000 ratings was cut out by limiting the x-axis.')
    img_path = os.path.join(current_dir, "..", "images", "average_rating_vs_number of ratings.png")
    # st.image('../images/average_rating_vs_number of ratings.png')
    st.image(Image.open(os.path.join(os.path.dirname(__file__), "..", "images", "average_rating_vs_number_of_ratings.png")))

with st.expander('See tag analysis'):
    st.markdown('#### Tagging behaviour')
    st.markdown('**Basic statistics**')
    st.write('Only 9% of users did apply tags, the following statistic refers to those users only.')
    left_column, right_column = st.columns(2)
    left_column.write('Number of tags per user per movie:')
    left_column.table(styled_stat_user_tag_movie)

    st.write('In the following scatter plot each point represents a user. Users who did not use any tags are higlighted in pink, the rugplot underlines the user concentration at zero tags.')
    # st.image('../data/visualization/rug_number_tag_vs_number_ratings.png')
    st.image(Image.open(os.path.join(os.path.dirname(__file__), "..", "images", "rug_number_tag_vs_number_ratings.png")))

###################################################################################################
############################################ learnings ############################################
###################################################################################################

box =  st.container(border=True)
box.markdown('#### Learnings from data exploration')
# box.markdown('- Genres show imbalanced distribution: out of 20 genres the top 2 (drama & comedy) make up for more than one third of all movies.')
box.markdown('- One user gave about 6000 ratings of 5.0 stars, will be removed in pre-processing.')
box.markdown('- There are users that gave exclusively rated movies with 0.5 stars. The same applies to other users with 5.0 stars respectively.')
box.markdown('- Only 9% users applied tags to minimum one movie => influence of tags on predictive performance might be minimal.')