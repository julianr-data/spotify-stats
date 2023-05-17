# IMPORTS
import pandas as pd
import numpy as np

# FUNCTIONS
def user_top_artists_into_df(dic):
    '''Function to transform top artist 'dic' data into a dataframe'''

    # Create empty lists to store data
    typ, name, genres, popularity, image, followers, idstring, url, uri = [], [], [], [], [], [], [], [], []

    # Loop through dictionary to append data to lists
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

def merge_top_artists_df_into_big_df(df_lt, df_mt, df_st, entity="artist"):
    '''Function to merge the three dataframes of artists depending on the period into a single dataframe,
    featuring the columns: artist, all time, last 6 months, last month'''

    # Deffro's code has this "entity" addition, I think it is to make the function work for songs as well
    entity_name = 'name' if entity.lower() == "artist" else "song_name"

    # Create lists of artist names for each period from dataframes
    lt_names = df_lt[entity_name].tolist()
    mt_names = df_mt[entity_name].tolist()
    st_names = df_st[entity_name].tolist()

    # Use long term list as base and append names from other lists if not already in long term list
    for name in mt_names:
        if name not in lt_names:
            lt_names.append(name)
    for name in st_names:
        if name not in lt_names:
            lt_names.append(name)

    # Iterate over name lists, find index of name in each dataframe (ie. position in that time range)
    # and append to new 'position' lists. If not found, append '-' and move to next list.

    lt_pos, mt_pos, st_pos = [], [], []
    for name in lt_names:
        try:
            lt_pos.append(df_lt.loc[df_lt[entity_name] == name].index.values[0] + 1)
        except IndexError:
            lt_pos.append('-')
        try:
            mt_pos.append(df_mt.loc[df_mt[entity_name] == name].index.values[0] + 1)
        except IndexError:
            mt_pos.append('-')
        try:
            st_pos.append(df_st.loc[df_st[entity_name] == name].index.values[0] + 1)
        except IndexError:
            st_pos.append('-')

    # Create blank dataframe and add lists as columns
    merged_df = pd.DataFrame()
    merged_df[entity.capitalize()] = lt_names
    merged_df['All Time'] = lt_pos
    merged_df['Last 6 Months'] = mt_pos
    merged_df['Last Month'] = st_pos

    return merged_df
