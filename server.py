### IMPORTS ###
import numpy as np
import pandas as pd
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from IPython.display import display
import plotly.express as px
import wordcloud

from functions.tops import API_call_top_artists, API_call_top_tracks, merge_tops_into_big_df_by_id,\
    count_genres, sb_data, top_releases_into_df, top_tracks_vs_release_chart, fake_API_call_top_artists,\
    fake_API_call_top_tracks, sb_decades_data, sb_decades_format, count_years, genres_into_string

### FUNCTIONS ###

def top_art():  # || API CALL MADE HERE - SWITCH BETWEEN TRUE AND FAKE API ||

    # Retrieving data as dictionary from Spotify API ('dic'), turning it into three dataframes
    # user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df = API_call_top_artists()

    # FAKE API: Retrieving data as dictionary from FAKE API ('dic'), turning it into three dataframes
    user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df = fake_API_call_top_artists()

    # Merge dataframes into one big dataframe
    big_artists_df = merge_tops_into_big_df_by_id(user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df)

    # To solve "-" problem in Streamlit
    big_artists_df.replace("-", np.nan, inplace=True)

    return big_artists_df, user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df

def top_songs():
    ## 2. TOP SONGS ##
    # Retrieving data as dictionary from Spotify API ('dic'), turning it into three dataframes
    # user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df = API_call_top_tracks()

    # FAKE API: Retrieving data as dictionary from FAKE API ('dic'), turning it into three dataframes
    user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df = fake_API_call_top_tracks()

    # Merge dataframes into one big dataframe
    big_tracks_df = merge_tops_into_big_df_by_id(user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df, entity='track')
    big_tracks_df.replace("-", np.nan, inplace=True)

    return big_tracks_df, user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df

def top_art_table(df, period):
    '''Take the big dataframe from top_art, with the artists ordered by user preference, and return a table concerning only the selected period'''

    df = df[['Artist', period]] # Select only PERIOD and "Artist" columns
    df.sort_values(by=[period], inplace=True, ascending=True) # Sort by selected period
    df.index.name = 'Ranking' # Rename index to "Ranking"
    df.index += 1 # Have index start from 1
    df = df.head(50)
    df = df[["Artist"]]



    # df.rename(columns={'All Time': 'Ranking'}, inplace=True) # Rename "All Time" column to "Ranking"
    # df = df.head(50)
    # df.sort_values(by=['Ranking'], inplace=True) # Sort by "Ranking"
    # df['Ranking'] = df['Ranking'].astype(int) # Change "Ranking" column to int

    return df

def wcloud(df_lt, df_mt, df_st):

    text_lt = genres_into_string(df_lt)
    text_mt = genres_into_string(df_mt)
    text_st = genres_into_string(df_st)

    wcloud_lt = wordcloud.WordCloud(width=450, height=400, max_words=50, background_color="black").generate(text_lt)
    wcloud_mt = wordcloud.WordCloud(width=450, height=400, max_words=50, background_color="black").generate(text_mt)
    wcloud_st = wordcloud.WordCloud(width=450, height=400, max_words=50, background_color="black").generate(text_st)

    return wcloud_lt, wcloud_mt, wcloud_st

def genre_sb_analysis(user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df):
    ## 3. GENRE ANALYSIS ##
    genre_count_lt = count_genres(user_top_artists_long_term_df)
    sb_df_lt = sb_data(user_top_artists_long_term_df, genre_count_lt)
    sb_df_lt_top = sb_df_lt.head(40)

    genre_count_mt = count_genres(user_top_artists_medium_term_df)
    sb_df_mt = sb_data(user_top_artists_medium_term_df, genre_count_mt)
    sb_df_mt_top = sb_df_mt.head(40)

    genre_count_st = count_genres(user_top_artists_short_term_df)
    sb_df_st = sb_data(user_top_artists_short_term_df, genre_count_st)
    sb_df_st_top = sb_df_st.head(40)

    return sb_df_lt, sb_df_lt_top, sb_df_mt, sb_df_mt_top, sb_df_st, sb_df_st_top



# REVIEW:::::::::


def decades_sb_analysis(longterm_df, mediumterm_df, shortterm_df):
    ## 4. DECADES ANALYSIS ##

    decades_formatted_lt = sb_decades_format(longterm_df)
    decades_formatted_mt = sb_decades_format(mediumterm_df)
    decades_formatted_st = sb_decades_format(shortterm_df)

    yc_lt = count_years(decades_formatted_lt)
    yc_mt = count_years(decades_formatted_mt)
    yc_st = count_years(decades_formatted_st)

    sb_df_lt_decades = sb_decades_data(decades_formatted_lt, yc_lt)
    sb_df_mt_decades = sb_decades_data(decades_formatted_mt, yc_mt)
    sb_df_st_decades = sb_decades_data(decades_formatted_st, yc_st)

    return sb_df_lt_decades, sb_df_mt_decades, sb_df_st_decades

def genre_barchart_analysis(user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df):
    ## 5. GENRE ANALYSIS ##
    gc_series_lt = count_genres(user_top_tracks_long_term_df)
    gc_series_mt = count_genres(user_top_tracks_medium_term_df)
    gc_series_st = count_genres(user_top_tracks_short_term_df)

    genre_count_lt = pd.DataFrame({'genre':gc_series_lt.index, 'count':gc_series_lt.values})
    genre_count_mt = pd.DataFrame({'genre':gc_series_mt.index, 'count':gc_series_mt.values})
    genre_count_st = pd.DataFrame({'genre':gc_series_st.index, 'count':gc_series_st.values})

    return genre_count_lt, genre_count_mt, genre_count_st

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


# tmpdf1, tmpdf2, tmpdf3 = fake_API_call_top_tracks()

# r1, r2, r3 = decades_sb_analysis(tmpdf1, tmpdf2, tmpdf3)
# print(r1, r2, r3)
# print("\n\n\n")

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
