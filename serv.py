# LIBRARY IMPORTS
import requests
import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from IPython.display import display

# FUNCTION IMPORTS
from functions.tops import user_top_artists_into_df, user_top_tracks_into_df, merge_tops_into_big_df_by_id

# SCOPE
scope = ["user-top-read", "user-read-playback-state"]

# CLIENT
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))



## 1. TOP ARTISTS ##

# Retrieving data in dictionary form from Spotify API ('dic')
user_top_artists_long_term_dic = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term') # dictionary of user top artists
user_top_artists_medium_term_dic = sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
user_top_artists_short_term_dic = sp.current_user_top_artists(limit=50, offset=0, time_range='short_term')

# Create dataframes from dictionaries
user_top_artists_long_term_df = user_top_artists_into_df(user_top_artists_long_term_dic)
user_top_artists_medium_term_df = user_top_artists_into_df(user_top_artists_medium_term_dic)
user_top_artists_short_term_df = user_top_artists_into_df(user_top_artists_short_term_dic)

# Merge dataframes into one big dataframe
big_artists_df = merge_tops_into_big_df_by_id(user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df)



## 2. TOP SONGS ##

# Retrieving data in dictionary form from Spotify API ('dic')
user_top_tracks_long_term_dic = sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term') # dictionary of user top tracks
user_top_tracks_medium_term_dic = sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')
user_top_tracks_short_term_dic = sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')

# Create dataframes from dictionaries
user_top_tracks_long_term_df = user_top_tracks_into_df(user_top_tracks_long_term_dic)
user_top_tracks_medium_term_df = user_top_tracks_into_df(user_top_tracks_medium_term_dic)
user_top_tracks_short_term_df = user_top_tracks_into_df(user_top_tracks_short_term_dic)

# Merge dataframes into one big dataframe
big_tracks_df = merge_tops_into_big_df_by_id(user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df, entity='track')


## DISPLAY IN TERMINAL FOR TESTING ##
# with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000):
#     display(big_artists_df)

## CAT INTO CSV FOR TESTING ##
user_top_tracks_long_term_df.to_csv('test_csvs/user_top_tracks_long_term_df.csv', index=False)
print('user_top_tracks_long_term_df.csv created')
user_top_tracks_medium_term_df.to_csv('test_csvs/user_top_tracks_medium_term_df.csv', index=False)
print('user_top_tracks_medium_term_df.csv created')
user_top_tracks_short_term_df.to_csv('test_csvs/user_top_tracks_short_term_df.csv', index=False)
print('user_top_tracks_short_term_df.csv created')
big_tracks_df.to_csv('test_csvs/big_tracks_df.csv', index=False)
print('big_tracks_df.csv created')

user_top_artists_long_term_df.to_csv('test_csvs/user_top_artists_long_term_df.csv', index=False)
print('user_top_artists_long_term_df.csv created')
user_top_artists_medium_term_df.to_csv('test_csvs/user_top_artists_medium_term_df.csv', index=False)
print('user_top_artists_medium_term_df.csv created')
user_top_artists_short_term_df.to_csv('test_csvs/user_top_artists_short_term_df.csv', index=False)
print('user_top_artists_short_term_df.csv created')

big_artists_df.to_csv('test_csvs/big_artists_df.csv', index=False)
print('big_artists_df.csv created')
