# LIBRARY IMPORTS
import numpy as np
import pandas as pd
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from IPython.display import display
import plotly.express as px

# FUNCTION IMPORTS
from functions.tops import API_call_top_artists, API_call_top_tracks, merge_tops_into_big_df_by_id, count_genres, sb_data


# SCOPE
scope = ["user-top-read", "user-read-playback-state"]

# CLIENT
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# '''VER SI PUEDO CORRER UNA APP.PY SEPARADA PARA EL FRONTEND, Y QUE:
#     1- SE CORRAN DOS SCRIPTS EN PARALELO Y APP TOME VARIABLES DE SERV.PY
#     2- SIMPLEMENTE HACER UNA GRAN FUNCION SERVER QUE CORRA EN SERV.PY Y QUE APP.PY LA LLAME

#     LA DOS ME PARECE MEJOR'''



## 1. TOP ARTISTS ##
# Retrieving data as dictionary from Spotify API ('dic'), turning it into three dataframes
user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df = API_call_top_artists()

# Merge dataframes into one big dataframe
big_artists_df = merge_tops_into_big_df_by_id(user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df)

# To show in Streamlit
big_artists_df.replace("-", np.nan, inplace=True)
st.write(big_artists_df)


## 2. TOP SONGS ##

user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df = API_call_top_tracks()

# Merge dataframes into one big dataframe
big_tracks_df = merge_tops_into_big_df_by_id(user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df, entity='track')
big_tracks_df.replace("-", np.nan, inplace=True)
st.write(big_tracks_df)


## 3. GENRE ANALYSIS ##

genre_count = count_genres(user_top_artists_long_term_df)
sb_df = sb_data(user_top_artists_long_term_df, genre_count)


# Plotting

fig = px.sunburst(sb_df, path=['genres', "artists"], values="count")
fig.update_layout(margin=dict(t=10, l=0, r=0, b=0), title={'text': "visualizing your music taste",
                                                                   'x': 0.5, 'y': 0.92})

st.plotly_chart(fig)





## DISPLAY IN TERMINAL FOR TESTING ##
# with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000):
#     display(big_artists_df)

## CAT INTO CSV FOR TESTING ##
# user_top_tracks_long_term_df.to_csv('test_csvs/user_top_tracks_long_term_df.csv', index=False)
# print('user_top_tracks_long_term_df.csv created')
# user_top_tracks_medium_term_df.to_csv('test_csvs/user_top_tracks_medium_term_df.csv', index=False)
# print('user_top_tracks_medium_term_df.csv created')
# user_top_tracks_short_term_df.to_csv('test_csvs/user_top_tracks_short_term_df.csv', index=False)
# print('user_top_tracks_short_term_df.csv created')
# big_tracks_df.to_csv('test_csvs/big_tracks_df.csv', index=False)
# print('big_tracks_df.csv created')

# user_top_artists_long_term_df.to_csv('test_csvs/user_top_artists_long_term_df.csv', index=False)
# print('user_top_artists_long_term_df.csv created')
# user_top_artists_medium_term_df.to_csv('test_csvs/user_top_artists_medium_term_df.csv', index=False)
# print('user_top_artists_medium_term_df.csv created')
# user_top_artists_short_term_df.to_csv('test_csvs/user_top_artists_short_term_df.csv', index=False)
# print('user_top_artists_short_term_df.csv created')

# big_artists_df.to_csv('test_csvs/big_artists_df.csv', index=False)
# print('big_artists_df.csv created')
