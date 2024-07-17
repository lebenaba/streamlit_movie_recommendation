import streamlit as st

st.set_page_config(page_title="Movie Recommender System", page_icon=":film_frames:")

intro_page = st.Page("sites/intro.py", title="Introduction") #, icon='🎥')
data_exploration_page = st.Page("sites/data_exploration.py", title="Data Exploration") #, icon='📊')
data_prep_page = st.Page("sites/data_preprocessing.py", title="Data Preprocessing") #, icon='🔁')
models_clas_page = st.Page("sites/models_classical.py", title="Models - classical") #, icon='🧮')
models_adv_page = st.Page("sites/models_advanced.py", title="Models - advanced") #, icon='🧮')
results_page = st.Page("sites/results.py", title="Results & Conclusion") #, icon='🥇')
conclusion_page = st.Page("sites/conclusion.py", title="Conclusion & Outlook") #, icon='📑')
about_page = st.Page("sites/about.py", title="About")



pg = st.navigation([intro_page,
                    data_exploration_page,
                    data_prep_page,
                    models_clas_page,
                    models_adv_page,
                    results_page,
                    # conclusion_page,
                    about_page])

## navigation with sub-groups
# pg = st.navigation({"Getting started": [intro_page],
#                     "Data": [data_exploration_page, data_prep_page],
#                     "Modeling": [models_page],
#                     "Discussion": [results_page, outlook_page],
#                     "": [conclusion_page],
#                     "_____": [about_page]})


pg.run()
