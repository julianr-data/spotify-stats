# LIBRARY IMPORTS
import numpy as np
import pandas as pd
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from IPython.display import display
import plotly.express as px

# FUNCTION IMPORTS
from functions.tops import API_call_top_artists, API_call_top_tracks, merge_tops_into_big_df_by_id, count_genres, sb_data, top_releases_into_df, top_tracks_vs_release_chart

# These functions are called in app.py to run all logic behind the app:

def top_art():
    ## 1. TOP ARTISTS ##
    # Retrieving data as dictionary from Spotify API ('dic'), turning it into three dataframes
    user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df = API_call_top_artists()

    # Merge dataframes into one big dataframe
    big_artists_df = merge_tops_into_big_df_by_id(user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df)

    # To solve "-" problem in Streamlit
    big_artists_df.replace("-", np.nan, inplace=True)

    return big_artists_df, user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df

def top_songs():
    ## 2. TOP SONGS ##
    # Retrieving data as dictionary from Spotify API ('dic'), turning it into three dataframes
    user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df = API_call_top_tracks()

    # Merge dataframes into one big dataframe
    big_tracks_df = merge_tops_into_big_df_by_id(user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df, entity='track')
    big_tracks_df.replace("-", np.nan, inplace=True)

    return big_tracks_df, user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df

def genre_analysis(user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df):
    ## 3. GENRE ANALYSIS ##
    genre_count_lt = count_genres(user_top_artists_long_term_df)
    sb_df_lt = sb_data(user_top_artists_long_term_df, genre_count_lt)
    sb_df_lt_top = sb_df_lt.head(20)

    genre_count_mt = count_genres(user_top_artists_medium_term_df)
    sb_df_mt = sb_data(user_top_artists_medium_term_df, genre_count_mt)
    sb_df_mt_top = sb_df_mt.head(20)

    genre_count_st = count_genres(user_top_artists_short_term_df)
    sb_df_st = sb_data(user_top_artists_short_term_df, genre_count_st)
    sb_df_st_top = sb_df_st.head(20)

    return sb_df_lt, sb_df_lt_top, sb_df_mt, sb_df_mt_top, sb_df_st, sb_df_st_top

def top_releases(lt_tracks, mt_tracks, st_tracks):
    x = top_releases_into_df(lt_tracks)
    y = top_releases_into_df(mt_tracks)
    z = top_releases_into_df(st_tracks)
    return x, y, z

def top_tracks_vs_release(lt_tracks, mt_tracks, st_tracks):
    x = top_tracks_vs_release_chart(lt_tracks)
    y = top_tracks_vs_release_chart(mt_tracks)
    z = top_tracks_vs_release_chart(st_tracks)
    return x, y, z





## PRINTS IN TERMINAL FOR TESTING ##
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
