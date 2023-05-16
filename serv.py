# IMPORTS
import requests
import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from IPython.display import display


# SCOPE
scope = ["user-top-read", "user-read-playback-state"]

# CLIENT
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))





# create dataframe with user top artists,

# retrieve data in dictionary form ('dic')
user_top_artists_long_term_dic = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term') # dictionary of user top artists
user_top_artists_medium_term_dic = sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
user_top_artists_short_term_dic = sp.current_user_top_artists(limit=50, offset=0, time_range='short_term')

def user_top_artists_into_df(dic):
    typ, name, genres, popularity, image, followers, idstring, url, uri = [], [], [], [], [], [], [], [], []

    for artist in dic['items']:
        typ.append(artist['type'])
        name.append(artist['name'])
        genres.append(artist['genres'])
        popularity.append(int(artist['popularity']))
        followers.append(artist['followers']['total'])
        idstring.append(artist['id'])
        url.append(artist['external_urls']['spotify'])
        uri.append(artist['uri'])
        try:
            image.append(artist['images'][0]['url'])
        except IndexError:
            image.append(np.nan)

    user_top_artists_df = pd.DataFrame({'type': typ, 'name': name,'genres': genres, 'popularity': popularity,
                                        'image': image, 'followers': followers, 'id': idstring, 'url': url, 'uri': uri})
    return user_top_artists_df

# into df
user_top_artists_long_term_df = user_top_artists_into_df(user_top_artists_long_term_dic)
user_top_artists_medium_term_df = user_top_artists_into_df(user_top_artists_medium_term_dic)
user_top_artists_short_term_df = user_top_artists_into_df(user_top_artists_short_term_dic)



def create_user_top_artists_across_periods(df_lt, df_mt, df_st, entity="artist"):
    """
    From the three dataframes of artists depending on the period, create a single dataframe with columns
    Artist, All Time, Last 6 Months, Last Month
    """
    entity_name = 'name' if entity.lower() == "artist" else "song_name"
    lt_names = df_lt[entity_name].tolist()
    mt_names = df_mt[entity_name].tolist()
    st_names = df_st[entity_name].tolist()

    for name in mt_names:
        if name not in lt_names:
            lt_names.append(name)
    for name in st_names:
        if name not in lt_names:
            lt_names.append(name)

    long_term_position, medium_term_position, short_term_position = [], [], []
    for t in lt_names:
        try:
            long_term_position.append(
                df_lt.loc[df_lt[entity_name] == t].index.values[
                    0] + 1)
        except IndexError:
            long_term_position.append('-')
        try:
            medium_term_position.append(
                df_mt.loc[df_mt[entity_name] == t].index.values[
                    0] + 1)
        except IndexError:
            medium_term_position.append('-')
        try:
            short_term_position.append(
                df_st.loc[df_st[entity_name] == t].index.values[
                    0] + 1)
        except IndexError:
            short_term_position.append('-')

    user_top_artists_across_periods = pd.DataFrame()

    user_top_artists_across_periods[entity.capitalize()] = lt_names
    user_top_artists_across_periods['All Time'] = long_term_position
    user_top_artists_across_periods['Last 6 Months'] = medium_term_position
    user_top_artists_across_periods['Last Month'] = short_term_position

    return user_top_artists_across_periods

big_df = create_user_top_artists_across_periods(user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df)

with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000):
    display(big_df)


# user_top_artists_long_term_df, user_top_artists_medium_term_df,
#                                            user_top_artists_short_term_df
