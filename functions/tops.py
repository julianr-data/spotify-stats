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

    user_top_artists_df = pd.DataFrame({'type': typ, 'artist_name': name,'genres': genres, 'popularity': popularity,
                                        'image': image, 'followers': followers, 'artist_id': idstring, 'url': url, 'uri': uri})
    return user_top_artists_df

def user_top_tracks_into_df(dic):
    '''Function to transform top tracks 'dic' data into a dataframe'''

    # Create empty lists to store data, using same structure as reference

    artist_name, artist_url = [], []
    album_name, album_release_date, album_image_url = [], [], []
    album_external_url, album_total_tracks = [], []
    track_duration, track_external_url, track_name, track_popularity = [], [], [], []
    track_preview_url, track_number_in_album = [], []

    # Further variables to process other stats
    track_href, track_idstring, track_explicit, track_available_markets, album_label, album_group, artist_id = [], [], [], [], [], [], []

    # Loop through dictionary to append data to lists
    for track in dic['items']:
        artist_name.append(track['artists'][0]['name'])
        artist_url.append(track['artists'][0]['external_urls']['spotify'])
        artist_id.append(track['artists'][0]['id']) # Not in reference

        album_name.append(track['album']['name'])
        album_release_date.append(track['album']['release_date'])
        try:
            album_image_url.append(track['album']['images'][0]['url'])
        except IndexError:
            album_image_url.append(np.nan)
        album_external_url.append(track['album']['external_urls']['spotify'])
        album_total_tracks.append(track['album']['total_tracks'])
        try:
            album_label.append(track['album']['label']) # Not in reference
        except KeyError:
            album_label.append(np.nan)
        album_group.append(track['album']['album_type']) # Not in reference

        track_duration.append(track['duration_ms'])
        track_external_url.append(track['external_urls']['spotify'])
        track_name.append(track['name'])
        track_popularity.append(track['popularity'])
        track_preview_url.append(track['preview_url'])
        track_number_in_album.append(track['track_number'])
        track_href.append(track['href']) # Not in reference
        track_idstring.append(track['id']) # Not in reference
        track_explicit.append(track['explicit']) # Not in reference
        track_available_markets.append(track['available_markets']) # Not in reference, not sure if useful

    # Create dataframe with lists
    user_top_tracks_df = pd.DataFrame({'artist_name': artist_name, 'artist_url': artist_url, 'artist_id': artist_id,
                                        'album_name': album_name, 'album_release_date': album_release_date,
                                        'album_image_url': album_image_url, 'album_external_url': album_external_url,
                                        'album_total_tracks': album_total_tracks, 'album_label': album_label,
                                        'album_group': album_group, 'track_duration': track_duration,
                                        'track_external_url': track_external_url, 'track_name': track_name,
                                        'track_popularity': track_popularity, 'track_preview_url': track_preview_url,
                                        'track_number_in_album': track_number_in_album, 'track_href': track_href,
                                        'track_id': track_idstring, 'track_explicit': track_explicit,
                                        'track_available_markets': track_available_markets})


    return user_top_tracks_df

def merge_tops_into_big_df(df_lt, df_mt, df_st, entity="artist"):
    '''Function to merge the three dataframes of artists depending on the period into a single dataframe,
    featuring the columns: artist, all time, last 6 months, last month'''

    print("Got into function")

    # Deffro's code has this "entity" addition, I think it is to make the function work for songs as well
    entity_name = 'name' if entity.lower() == "artist" else "track_name"

    print("Entity name is: ", entity_name)

    # Create lists of entity names for each period from dataframes
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

def merge_tops_into_big_df_by_id(df_lt, df_mt, df_st, entity="artist"):
    '''
    REWRITE OF merge_tops_into_big_df TO USE ID INSTEAD OF NAME
    Function to merge the three dataframes of artists depending on the period into a single dataframe,
    featuring the columns: artist, all time, last 6 months, last month
    Improved original: using ID to find position instead of name'''

    print("Got into function")

    # Deffro's code has this "entity" addition, I think it is to make the function work for songs as well
    entity_type = 'artist_id' if entity.lower() == "artist" else "track_id"

    print("Entity type is: ", entity_type)

    # Create lists of entity names for each period from dataframes
    lt_ids = df_lt[entity_type].tolist()
    mt_ids = df_mt[entity_type].tolist()
    st_ids = df_st[entity_type].tolist()

    # Use long term list as base and append names from other lists if not already in long term list
    for idstring in mt_ids:
        if idstring not in lt_ids:
            lt_ids.append(idstring)
    for idstring in st_ids:
        if idstring not in lt_ids:
            lt_ids.append(idstring)

    # Iterate over id lists, find index of id in each dataframe (ie. position in that time range)
    # and append to new 'position' lists. If not found, append '-' and move to next list.
    # At the same time do the same with names.

    lt_pos, mt_pos, st_pos = [], [], []
    lt_names, mt_names, st_names = [], [], []

    for idstring in lt_ids:

        # First add the ranking (index) of the entity
        try:
            lt_pos.append(df_lt.loc[df_lt[entity_type] == idstring].index.values[0] + 1)
        except IndexError:
            lt_pos.append('-')
        # Then add the name corresponding to the entity
        if entity_type == 'track_id':
            lt_names.append(df_lt.loc[df_lt[entity_type] == idstring, 'track_name'].to_string(index=False))
        elif entity_type == 'artist_id':
            lt_names.append(df_lt.loc[df_lt[entity_type] == idstring, 'artist_name'].to_string(index=False))

        # Again for mid term
        try:
            mt_pos.append(df_mt.loc[df_mt[entity_type] == idstring].index.values[0] + 1)
        except IndexError:
            mt_pos.append('-')
        # if entity_type == 'track_id':
        #     lt_names.append(df_mt.loc[df_mt[entity_type] == idstring, 'track_name'].to_string(index=False))
        # elif entity_type == 'artist_id':
        #     lt_names.append(df_mt.loc[df_mt[entity_type] == idstring, 'artist_name'].to_string(index=False))

        # Again for short term
        try:
            st_pos.append(df_st.loc[df_st[entity_type] == idstring].index.values[0] + 1)
        except IndexError:
            st_pos.append('-')
        # if entity_type == 'track_id':
        #     lt_names.append(df_st.loc[df_st[entity_type] == idstring, 'track_name'].to_string(index=False))
        # elif entity_type == 'armist_id':
        #     lt_names.append(df_st.loc[df_st[entity_type] == idstring, 'artist_name'].to_string(index=False))


    print(lt_names)
    print("Number of names:")
    print(len(lt_names))

    quit()


    # hasta ahora el problema es despues de la posicion 49, no encuentra el nombre del artista o cancion y pone series vacias
    # seguir recorrido de un artist id y ver que mierda pasa que no encuentra el nombre,
    # el artist id que estoy siguiendo es 4P70aqttdpJ9vuYFDmf7f6 y el nombre es "Vangelis"



    # Create blank dataframe and add lists as columns
    merged_df = pd.DataFrame()
    merged_df[f"{entity.capitalize()} ID"] = lt_ids
    merged_df[entity.capitalize()] = lt_names
    merged_df['All Time'] = lt_pos
    merged_df['Last 6 Months'] = mt_pos
    merged_df['Last Month'] = st_pos

    return merged_df
