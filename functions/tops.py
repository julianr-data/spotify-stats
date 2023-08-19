# IMPORTS
import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from IPython.display import display
import plotly.express as px
import json

# SCOPE
scope = ["user-top-read", "user-read-playback-state"]

# CLIENT
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

### ### FUNCTIONS ### ###

## FAKE API CALLS ##

def fake_API_call_top_artists():
    with open("functions/fake_api_calls/user_top_artist_long_term.json") as f:
        fake_user_top_artists_long_term_dic = json.load(f)
    print("\n--- FAKE API CALLED FOR TOP ARTISTS LONG TERM ---")
    with open("functions/fake_api_calls/user_top_artist_medium_term.json") as f:
        fake_user_top_artists_medium_term_dic = json.load(f)
    print("\n--- FAKE API CALLED FOR TOP ARTISTS MEDIUM TERM ---")
    with open("functions/fake_api_calls/user_top_artist_short_term.json") as f:
        fake_user_top_artists_short_term_dic = json.load(f)
    print("\n--- FAKE API CALLED FOR TOP ARTISTS SHORT TERM ---")

 # Create dataframes from dictionaries
    user_top_artists_long_term_df = user_top_artists_into_df(fake_user_top_artists_long_term_dic)
    user_top_artists_medium_term_df = user_top_artists_into_df(fake_user_top_artists_medium_term_dic)
    user_top_artists_short_term_df = user_top_artists_into_df(fake_user_top_artists_short_term_dic)

    return user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df

def fake_API_call_top_tracks():
    with open("functions/fake_api_calls/user_top_tracks_long_term.json") as f:
        fake_user_top_tracks_long_term_dic = json.load(f)
    print("\n--- FAKE API CALLED FOR TOP TRACKS LONG TERM ---")
    with open("functions/fake_api_calls/user_top_tracks_medium_term.json") as f:
        fake_user_top_tracks_medium_term_dic = json.load(f)
    print("\n--- FAKE API CALLED FOR TOP TRACKS MEDIUM TERM ---")
    with open("functions/fake_api_calls/user_top_tracks_short_term.json") as f:
        fake_user_top_tracks_short_term_dic = json.load(f)
    print("\n--- FAKE API CALLED FOR TOP TRACKS SHORT TERM ---")

    # Create dataframes from dictionaries
    user_top_tracks_long_term_df = user_top_tracks_into_df(fake_user_top_tracks_long_term_dic)
    user_top_tracks_medium_term_df = user_top_tracks_into_df(fake_user_top_tracks_medium_term_dic)
    user_top_tracks_short_term_df = user_top_tracks_into_df(fake_user_top_tracks_short_term_dic)

    return user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df

## TRUE API CALLS ##

def API_call_top_artists():
    '''Retrieving data in dictionary form from Spotify API ('dic')
    Transforming data into dataframes, returning dataframes for long, medium and short term top artists'''
    user_top_artists_long_term_dic = sp.current_user_top_artists(limit=50, offset=0, time_range='long_term') # dictionary of user top artists
    print("\n--- API CALLED FOR TOP ARTISTS LONG TERM ---")
    user_top_artists_medium_term_dic = sp.current_user_top_artists(limit=50, offset=0, time_range='medium_term')
    print("\n--- API CALLED FOR TOP ARTISTS MEDIUM TERM ---")
    user_top_artists_short_term_dic = sp.current_user_top_artists(limit=50, offset=0, time_range='short_term')
    print("\n--- API CALLED FOR TOP ARTISTS SHORT TERM ---")

    # # Temp json write for fake api call
    # user_top_artist_long_term_json = json.dumps(user_top_artists_long_term_dic)
    # user_top_artist_medium_term_json = json.dumps(user_top_artists_medium_term_dic)
    # user_top_artist_short_term_json = json.dumps(user_top_artists_short_term_dic)

    # with open('user_top_artist_long_term.json', 'w') as outfile:
    #     outfile.write(user_top_artist_long_term_json)
    # with open('user_top_artist_medium_term.json', 'w') as outfile:
    #     outfile.write(user_top_artist_medium_term_json)
    # with open('user_top_artist_short_term.json', 'w') as outfile:
    #     outfile.write(user_top_artist_short_term_json)

    # Create dataframes from dictionaries
    user_top_artists_long_term_df = user_top_artists_into_df(user_top_artists_long_term_dic)
    user_top_artists_medium_term_df = user_top_artists_into_df(user_top_artists_medium_term_dic)
    user_top_artists_short_term_df = user_top_artists_into_df(user_top_artists_short_term_dic)

    return user_top_artists_long_term_df, user_top_artists_medium_term_df, user_top_artists_short_term_df

def API_call_top_tracks():
    '''Retrieving data in dictionary form from Spotify API ('dic')
    Transforming data into dataframes, returning dataframes for long, medium and short term top tracks'''
    user_top_tracks_long_term_dic = sp.current_user_top_tracks(limit=50, offset=0, time_range='long_term') # dictionary of user top tracks
    print("\n--- API CALLED FOR TOP TRACKS LONG TERM ---")
    user_top_tracks_medium_term_dic = sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')
    print("\n--- API CALLED FOR TOP TRACKS MEDIUM TERM ---")
    user_top_tracks_short_term_dic = sp.current_user_top_tracks(limit=50, offset=0, time_range='short_term')
    print("\n--- API CALLED FOR TOP TRACKS SHORT TERM ---")

    # # Temp json write for fake api call
    # user_top_tracks_long_term_json = json.dumps(user_top_tracks_long_term_dic)
    # user_top_tracks_medium_term_json = json.dumps(user_top_tracks_medium_term_dic)
    # user_top_tracks_short_term_json = json.dumps(user_top_tracks_short_term_dic)

    # with open('user_top_tracks_long_term.json', 'w') as outfile:
    #     outfile.write(user_top_tracks_long_term_json)
    # with open('user_top_tracks_medium_term.json', 'w') as outfile:
    #     outfile.write(user_top_tracks_medium_term_json)
    # with open('user_top_tracks_short_term.json', 'w') as outfile:
    #     outfile.write(user_top_tracks_short_term_json)

    # Create dataframes from dictionaries
    user_top_tracks_long_term_df = user_top_tracks_into_df(user_top_tracks_long_term_dic)
    user_top_tracks_medium_term_df = user_top_tracks_into_df(user_top_tracks_medium_term_dic)
    user_top_tracks_short_term_df = user_top_tracks_into_df(user_top_tracks_short_term_dic)

    return user_top_tracks_long_term_df, user_top_tracks_medium_term_df, user_top_tracks_short_term_df

## PROCESSES ##

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
    track_href, track_idstring, track_explicit, track_available_markets, album_label, album_group, album_genre, artist_id, album_id = [], [], [], [], [], [], [], [], []

    # Loop through dictionary to append data to lists
    for track in dic['items']:
        artist_name.append(track['artists'][0]['name'])
        artist_url.append(track['artists'][0]['external_urls']['spotify'])
        artist_id.append(track['artists'][0]['id']) # Not in reference

        album_name.append(track['album']['name'])
        album_id.append(track['album']['id']) # Not in reference
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
        try:
            album_genre.append(track['album']['genres']) # Not in reference
        except KeyError:
            album_genre.append(np.nan) # Try to get the genre for sunburst (this being the best source). If not possible, append NaN

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
                                        'album_name': album_name, 'album_id': album_id, 'album_release_date': album_release_date,
                                        'album_image_url': album_image_url, 'album_external_url': album_external_url,
                                        'album_total_tracks': album_total_tracks, 'album_label': album_label,
                                        'album_group': album_group, "album_genre": album_genre, 'track_duration': track_duration,
                                        'track_external_url': track_external_url, 'track_name': track_name,
                                        'track_popularity': track_popularity, 'track_preview_url': track_preview_url,
                                        'track_number_in_album': track_number_in_album, 'track_href': track_href,
                                        'track_id': track_idstring, 'track_explicit': track_explicit,
                                        'track_available_markets': track_available_markets})


    return user_top_tracks_df

def merge_tops_into_big_df_by_id(df_lt, df_mt, df_st, entity="artist"):
    '''Rewrite of merge_tops_into_big_df to use ID instead of name.
    Function to merge the three dataframes of artists depending on the period into a single dataframe,
    featuring the columns: artist, all time, last 6 months, last month
    Improved original: using ID to find position instead of name'''

    # print("Got into function")

    # Deffro's code has this "entity" addition, I think it is to make the function work for songs as well
    entity_type = 'artist_id' if entity.lower() == "artist" else "track_id"

    # print("Entity type is: ", entity_type)

    # print("printing df short term:")
    # with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000):
    #     display(df_st)


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
        if entity_type == 'track_id':
            lt_names.append(df_mt.loc[df_mt[entity_type] == idstring, 'track_name'].to_string(index=False))
        elif entity_type == 'artist_id':
            lt_names.append(df_mt.loc[df_mt[entity_type] == idstring, 'artist_name'].to_string(index=False))

        # Again for short term
        try:
            st_pos.append(df_st.loc[df_st[entity_type] == idstring].index.values[0] + 1)
        except IndexError:
            st_pos.append('-')
        if entity_type == 'track_id':
            lt_names.append(df_st.loc[df_st[entity_type] == idstring, 'track_name'].to_string(index=False))
        elif entity_type == 'armist_id':
            lt_names.append(df_st.loc[df_st[entity_type] == idstring, 'artist_name'].to_string(index=False))


    # After position 49, the name is not found and the function returns a 'Series([], )' string.
    # Solved this by clearing the list of repeated names and 'Series([], )' strings, without changing the order:

    lt_names = list(dict.fromkeys(lt_names))
    counter = 0
    for name in lt_names:
        if name == 'Series([], )':
            counter += 1
    lt_names = [x for x in lt_names if x != 'Series([], )']
    for i in range(counter):
        lt_names.append('RETRY ID')

    # If the lt_ids list is longer than the lt_names list, it means that there are some names
    # missing and there will be an error. Trim the list to the same length as lt_names:
    # if len(lt_ids) > len(lt_names):
    #     lt_ids = lt_ids[:len(lt_names)]

    ###
    # Debug prints:
    # print("PRINTS TO MAKE INITIAL LENGHT COMPARISON")
    # print(lt_names)
    # print("Number of names:")
    # print(len(lt_names))
    # print()
    # print(lt_ids)
    # print("Number of IDs:")
    # print(len(lt_ids))
    ###

    # Retry ID for failed names
    # if all this fails, we add +1 to a trimcounter than will them trim all lists so we don't get index errors
    # this is all done on the basis that whenever a 'series([], )' is found, the id is last in the list, independent
    # of where the 'series([], )' name is found in the list

    trimcounter = 0

    if entity_type == 'artist_id':
        for name in lt_names:
            if name == 'RETRY ID':
                print("Found a RETRY ID name field")
                i = lt_names.index("RETRY ID")
                print(f"index of RETRY ID element: {i}")
                try:
                    lt_names[i] = df_mt.loc[df_mt[entity_type] == idstring, 'artist_name'].to_string(index=False)
                    print("got in 1st try")
                    print(lt_names[i])
                    if lt_names[i] == 'Series([], )':
                        try:
                            lt_names[i] = df_st.loc[df_st[entity_type] == idstring, 'artist_name'].to_string(index=False)
                            print("got in 2nd try")
                            print(lt_names[i])
                            if lt_names[i] == 'Series([], )':
                                try:
                                    lt_names[i] = df_lt.loc[df_lt[entity_type] == idstring, 'artist_name'].to_string(index=False)
                                    print("got in 3rd try")
                                    print(lt_names[i])
                                except IndexError:
                                    print("IndexError in df_lt")    # NOT TESTED YET!
                                    trimcounter += 1
                                    print("+1 trimcounter")
                                    pass
                        except IndexError:
                            print("IndexError in df_st")
                            pass
                except IndexError:
                    print("IndexError in df_mt")
                    pass

            # Before going for the trimcounter I can add a pass, then an ad hoc api call to get the name from the id,
            # be sure to account for API error messages, and of course if it still returns 'Series([], )' then
            # just settle for adding +1 to the trimcounter and moving on.
    else:
        for name in lt_names:
            if name == 'RETRY ID':
                print("Found a RETRY ID name field")
                i = lt_names.index("RETRY ID")
                print(f"index of RETRY ID element: {i}")
                try:
                    lt_names[i] = df_mt.loc[df_mt[entity_type] == idstring, 'track_name'].to_string(index=False)
                    print("got in 1st try")
                    print(lt_names[i])
                    if lt_names[i] == 'Series([], )':
                        try:
                            lt_names[i] = df_st.loc[df_st[entity_type] == idstring, 'track_name'].to_string(index=False)
                            print("got in 2nd try")
                            print(lt_names[i])
                            if lt_names[i] == 'Series([], )':
                                try:
                                    lt_names[i] = df_lt.loc[df_lt[entity_type] == idstring, 'track_name'].to_string(index=False)
                                    print("got in 3rd try")
                                    print(lt_names[i])
                                except IndexError:
                                    print("IndexError in df_lt")    # NOT TESTED YET!
                                    trimcounter += 1
                                    print("+1 trimcounter")
                                    pass
                        except IndexError:
                            print("IndexError in df_st")
                            pass
                except IndexError:
                    print("IndexError in df_mt")
                    pass

    if trimcounter > 0:
        lt_names = lt_names[:-trimcounter]

    print("PRINTS TO MAKE SECOND LENGHT COMPARISON, AFTER TRYING TO LOCATE RETRY ID TRUE NAMES")
    print(lt_names)
    print("Number of names:")
    print(len(lt_names))
    print()
    print(lt_ids)
    print("Number of IDs:")
    print(len(lt_ids))


    # Trim all lists to the lt_names length if longer than lt_names: ## ALL THESE HASNT BEEN TESTED YET BUT SHOULD WORK

    if len(lt_names) > len(lt_ids):
        lt_names = lt_names[:len(lt_ids)]
        print("Trimmed lt_names to match lt_ids")

    if len(lt_ids) > len(lt_names):
        lt_ids = lt_ids[:len(lt_names)]
        print("Trimmed lt_ids to match lt_names") # Maybe add by how much it was trimmed?

    if len(lt_pos) > len(lt_names):
        lt_pos = lt_pos[:len(lt_names)]
        print("Trimmed lt_pos to match lt_names")

    if len(mt_pos) > len(lt_names):
        mt_pos = mt_pos[:len(lt_names)]
        print("Trimmed mt_post to match lt_names")

    if len(st_pos) > len(lt_names):
        st_pos = st_pos[:len(lt_names)]
        print("Trimmed st_pos to match lt_names")


    # Create blank dataframe and add lists as columns
    merged_df = pd.DataFrame()
    merged_df[f"{entity.capitalize()} ID"] = lt_ids
    merged_df[entity.capitalize()] = lt_names
    merged_df['Last Month'] = st_pos
    merged_df['Last 6 Months'] = mt_pos
    merged_df['All Time'] = lt_pos

    return merged_df

def count_genres(df):
    gcount = {}
    for genre_object in df['genres']:
        # print("Genre object type is: ", type(genre_object))
        if genre_object == "Series([], )" or genre_object == []:
            genre_list = ["Uncategorized"]
        else:
            genre_list = genre_object
        for genre in genre_list:
            if genre not in gcount:
                gcount[genre] = 1
            else:
                gcount[genre] += 1
    gcount = pd.Series(gcount).sort_values(ascending=False)
    return gcount

def count_years(df):
    year_count = {}
    for year in df['album_release_year']:
        if year not in year_count:
            year_count[year] = 1
        else:
            year_count[year] += 1
    year_count = pd.Series(year_count).sort_values(ascending=False)
    return year_count

def sb_data(df, topgenres):
    art, gen, count = [], [], []
    for index, row in df.iterrows():
        for genre, value in zip(topgenres.index, topgenres.values):
            if genre in row["genres"]:
                gen.append(genre)
                count.append(value)
                art.append(row["artist_name"])

    res = pd.DataFrame({"artists": art, "genres": gen, "count": count})

    # with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000):
    #     display(res)

    return res

def count_top_albums(df):
    id_count = {}
    for id in df['album_id']:
        if id not in id_count:
            id_count[id] = 1
        else:
            id_count[id] += 1
    alb_id = pd.Series(id_count).sort_values(ascending=False)
    print(type(alb_id))
    return alb_id

def top_releases_into_df(df):
    count = count_top_albums(df)
    album_names = df.set_index('album_id')["album_name"].to_frame()
    album_prevalence = album_names.merge(count.rename('count'), left_index=True, right_index=True).drop_duplicates().sort_values(by='count', ascending=False).head(20)
    album_prevalence = album_prevalence.reset_index().rename(columns={'album_name': 'Album Name', 'count': 'Nº of songs in this period'}).drop('album_id', axis=1)
    return album_prevalence

def top_tracks_vs_release_chart(df):

    # DEPRECATED renaming columns as it complicate sother functions
    # df.rename(columns={"track_popularity": "Popularity", "album_release_date": "Release Date",
    #                    "track_duration": "Track Lenght", "artist_name": "Artist",
    #                    "track_name": "Track Name"}, inplace=True)

    bubfig = px.scatter(df, x="album_release_date", y="track_popularity",
                        size="track_duration", color="artist_name",
                        hover_name="track_name", size_max=30)

    bubfig.update_layout(yaxis=dict(gridcolor='#53f34a'),
                    xaxis=dict(gridcolor='#000000'), plot_bgcolor='#232323',
                    legend=dict(
                        xanchor='center',
                        yanchor='top',
                        y=-0.3,
                        x=0.5,
                        orientation='h')
                    )

    # update axis labels:
    bubfig.update_xaxes(title_text='Release Date')
    bubfig.update_yaxes(title_text='Current Popularity')
    bubfig.update
    return bubfig







    # user_all_top_tracks = pd.concat([user_top_tracks_data_long_term, user_top_tracks_data_medium_term,
    #                                  user_top_tracks_data_short_term])
    # user_top_albums = user_all_top_tracks.groupby('album_name')['song_name']. \
    #     count().to_frame().reset_index().sort_values(by='song_name', ascending=False).head()
    # user_top_albums = user_top_albums.merge(user_all_top_tracks.drop(['song_name'], axis=1),
    #                                         how='left', on='album_name')[['album_name', 'artist_name', 'song_name']]
    # user_top_albums = user_top_albums.rename(
    #     columns={'album_name': 'Album', 'artist_name': 'Artist',
    #              'song_name': 'Tracks'}).drop_duplicates()

def sb_decades_format(df):
    '''Strip top track dataframes of everything except
    - artist
    - trackname
    - release date
    chop everything after year, then add decade column
    deprecated: turn release date into datetime format. pandas doesn't seem to recognize iso8601 format correctly'''

    print(df.columns)

    dfres = df[["artist_name", "track_name", "album_release_date"]]

    # leave only the first 4 characters of the album release date with a lambda function
    dfres["album_release_date"] = dfres["album_release_date"].apply(lambda x: x[:4])

    # change album release date column name to album release year
    dfres.rename(columns={"album_release_date": "album_release_year"}, inplace=True)

    # add decade column
    dfres["album_release_decade"] = dfres["album_release_year"].apply(lambda x: x[:3] + "0s")

    # deprecated ISO8601 approach:
    # dfres["album_release_date"] = pd.to_datetime(dfres["album_release_date"], format="ISO8601")


    print(dfres.dtypes)
    return dfres

def sb_decades_data(df, topyears):
    tr, year, dec, art, count = [], [], [], [], []

    for index, row in df.iterrows():
        for y, value in zip(topyears.index, topyears.values):
            if y in row["album_release_year"]:
                art.append(row["artist_name"])
                year.append(y)
                count.append(value)
                tr.append(row["track_name"])
                dec.append(row["album_release_decade"])

    res = pd.DataFrame({"track": tr, "year": year, "decade": dec, "artist": art, "count": count})

    return res

    # with pd.option_context('display.max_rows', 1000, 'display.max_columns', 1000):
    #     display(res)


# MAIN for testing genres barchart
t1, t2, t3 = (fake_API_call_top_artists())
f1 = count_genres(t1)
print(f1)

# MAIN for testing decades sunburst
# t1, t2, t3 = (fake_API_call_top_tracks())
# f1 = sb_decades_format(t1)
# yc1 = count_years(f1)
# dat = sb_decades_data(f1, yc1)
# print("\n\nDAT:")
# print(dat)




## Deprecated function, use merge_tops_into_big_df_by_id instead:
def merge_tops_into_big_df(df_lt, df_mt, df_st, entity="artist"):
    '''Deprecated as of 21 May 2023, ID-based function should be used instead. Keeping in case something breaks, this one works'''

    '''Function to merge the three dataframes of artists depending on the period into a single dataframe,
    featuring the columns: artist, all time, last 6 months, last month'''

    # print("Got into function")

    # Deffro's code has this "entity" addition, I think it is to make the function work for songs as well
    entity_name = 'name' if entity.lower() == "artist" else "track_name"

    # print("Entity name is: ", entity_name)

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

## Deprecated function, converts genres list from object to string (unnecesary) and then counts genres
def count_genres_deprecated(df):
    gcount = {}
    for genre_object in df['genres']:
        genre_string = genre_object#.to_string(index=False)
        # print(type(genre_string))
        if genre_string == "Series([], )" or genre_string == "[]":
            genre_list = ["Uncategorized"]
        else:
            genre_list = genre_string[1:-1].replace("'","").replace(", ", ",").split(",")
        for genre in genre_list:
            if genre not in gcount:
                gcount[genre] = 1
            else:
                gcount[genre] += 1
    gcount = pd.Series(gcount).sort_values(ascending=False)
    return gcount



# MAIN for creating data for fake api calls
# API_call_top_artists()
# API_call_top_tracks()
