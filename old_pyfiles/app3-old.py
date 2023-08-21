# IMPORT

import streamlit as st
import plotly.express as px
import seaborn as sns
import pandas as pd
import wordcloud

from server import top_art, top_songs, genre_sb_analysis, top_releases,\
    top_tracks_vs_release, decades_sb_analysis, genre_barchart_analysis,\
    top_table_noindex, wcloud, tinker_bigdfs_fordisplay





### DATA FROM SERVER.PY ###

# API CALLS ARE MADE HERE #
big_art_df, top_art_lt_df, top_art_mt_df, top_art_st_df = top_art() # Top artists
print("Top artists API calls invoked from server")

big_tr_df, top_tr_lt_df, top_tr_mt_df, top_tr_st_df = top_songs() # Top tracks
print("Top tracks  API calls invoked from server")

## DATA TRANSFORMATION ##

# TOP GENRES #
sb_df_lt, sb_df_lt_top, sb_df_mt,\
sb_df_mt_top, sb_df_st, sb_df_st_top = genre_sb_analysis(top_art_lt_df, top_art_mt_df, top_art_st_df) # Genre sunburst
print("Top genres sunburst data calculated")

gen_bc_lt, gen_bc_mt, gen_bc_st = genre_barchart_analysis(top_art_lt_df, top_art_mt_df, top_art_st_df) # Genre barchart
print("Top genres barchart data calculated")

wc_lt, wc_mt, wc_st = wcloud(top_art_lt_df, top_art_mt_df, top_art_st_df) # Wordcloud
print("Wordcloud data generated")

# TOP RELEASES #
top_rel_lt, top_rel_mt, top_rel_st = top_releases(top_tr_lt_df, top_tr_mt_df, top_tr_st_df) # Top releases
print("Top releases data calculated")

tr_vs_date_lt, tr_vs_date_mt, tr_vs_date_st = top_tracks_vs_release(top_tr_lt_df, top_tr_mt_df, top_tr_st_df) # Top tracks vs release date
print("Top tracks vs. top releases data calculated")

# TOP DECADES #
lt_dec, mt_dec, st_dec = decades_sb_analysis(top_tr_lt_df, top_tr_mt_df, top_tr_st_df)
print("Decades sunburns data calculated")



### PAGE CONFIGURATION ###

# Streamlit page configuration
st.set_page_config(page_title="Spotify Data Analysis",
                   page_icon="frontend/tasti1-transp2.png",
                   layout="wide", initial_sidebar_state="expanded",
                   menu_items={"Report a bug": "https://github.com/julianr-data/spotify-stats",
                               "About": "https://github.com/julianr-data/spotify-stats"})

# Background image CSS
page_bg_img = f"""<style>[data-testid="stAppViewContainer"] > .main {{
background: rgb(0,0,0);background: linear-gradient(93deg,
rgba(0,0,0,1) 70%, rgba(29,185,84,1) 94%, rgba(30,215,96,1) 100%);}}
</style>"""

# Set background image
st.markdown(page_bg_img, unsafe_allow_html=True)


### SIDEBAR ###

st.sidebar.image("frontend/app3-logo-whiteltter-transparent-narrow.png")
st.sidebar.title("Visualize your music taste")
timeframe = st.sidebar.radio("Choose a time frame:", ("All Time", "Last 6 Months", "Last Month"), horizontal=False, label_visibility="collapsed")

st.sidebar.markdown("Get an analysis of your Spotify listening habits: top artists, songs, genres, saved items, etc. with colorful charts and graphs.", unsafe_allow_html=True)
st.sidebar.markdown("To use this app, you need to have a Spotify account. If you don't have an account, you can create one [here](https://www.spotify.com/signup/).", unsafe_allow_html=True)
st.sidebar.markdown("Your data comes from the [Spotify API](https://developer.spotify.com/documentation/web-api/).", unsafe_allow_html=True)

st.sidebar.markdown("The code for this app can be found [here](https://github.com/julianr-data/spotify-stats). [Contact me](https://www.linkedin.com/in/julianr-data/) if you have any questions!")
st.sidebar.markdown("V 0.3 | ©2023 | Created by [Julián Rodríguez](https://www.linkedin.com/in/julianr-data/)")



### MAIN PAGE ###

# Title
col1a, col1b = st.columns([0.7, 0.6], gap="small")
with col1a:
    st.title(f"Your Spotify data analysis:")
with col1b:
    st.title(f"{timeframe}")
st.markdown("""---""")

# ALL TIME #
# if timeframe == "All Time":

top_art = top_table_noindex(big_art_df, "All Time", "art")
toptr = top_table_noindex(big_tr_df, "All Time", "tr")

col2a, col2b, col2c  = st.columns([0.45, 0.1, 0.45], gap="small")
with col2a:
    st.subheader("Top artists")
    st.dataframe(top_art, use_container_width = True)
with col2b:
    # Just to create space
    pass
with col2c:
    st.subheader("Top genres")
    wcimage = wc_lt.to_image() # create an image for the wordcloud
    st.image(wcimage, use_column_width=True) # display the image in the streamlit app

st.markdown("")
st.markdown("")

col3a, col3b, col3c = st.columns([0.45, 0.1, 0.45], gap="small")
with col3c:
    st.subheader("Top tracks")
    st.dataframe(toptr, use_container_width = True)
with col3b:
    # Just to create space
    pass
with col3a:
    st.write("")
    st.subheader("Genre analysis (detail)")
    sbfig = px.sunburst(sb_df_lt_top, path=['genres', "artists"], values="count", color="count",
                hover_data=['genres'],
                color_continuous_scale='Emrld')
    sbfig.update_layout(margin=dict(t=0, l=10, r=10, b=10))
    st.plotly_chart(sbfig, use_container_width=True)

col4a, col4b, col4c = st.columns([0.55, 0.05, 0.4], gap="small")

with col4c:
    st.subheader("Top Decades")
    decadesbar = px.bar(lt_dec, x="decade", y="count", color="decade", color_discrete_sequence=px.colors.qualitative.Pastel,
                        labels={'decade':'Decades', "count": "Nº of songs"}, height=450)
    st.plotly_chart(decadesbar, use_container_width=True, margin=dict(l=20, r=25, t=10, b=10))

with col4b:
    # Just to create space
    pass
with col4a:
    st.subheader("Top releases")
    st.dataframe(top_rel_lt, use_container_width = True)

st.markdown("")
st.markdown("")

st.subheader(f"Top songs release date vs. current popularity")
st.write("ie. how your musical taste in this period compares to the general public current musical preferences")
st.plotly_chart(tr_vs_date_lt, use_container_width=True)

st.markdown("""---""")
st.subheader(f"Detailed comparison of your musical taste in different time frames")

col5a, col5b = st.columns(2, gap="small")

with col5a:
    st.subheader("Top Artists")
    big_art_df_display = tinker_bigdfs_fordisplay(big_art_df, "Artist")
    st.dataframe(big_art_df_display)

with col5b:
    st.subheader("Top Tracks")
    big_tr_df_display =  tinker_bigdfs_fordisplay(big_tr_df, "Track")
    st.dataframe(big_tr_df_display)






# # Top artists & tracks
# col1, col2 = st.columns(2)
# cm = sns.light_palette("seagreen", reverse=True, as_cmap=True)
# with col1:
#     st.subheader("Top Artists")
#     big_art_df_display = big_art_df.drop("Artist ID", axis=1) # .style.background_gradient(cmap=cm)
#     st.write(big_art_df_display)

# with col2:
#     st.subheader("Top Tracks")
#     big_tr_df_display = big_tr_df.drop("Track ID", axis=1)
#     st.dataframe(big_tr_df_display)

# st.markdown("""---""")

# # Sunburst decades, top albums, top songs vs. release date
# chosen_time = st.radio("Choose a time frame:", ("All Time", "Last 6 Months", "Last Month"), horizontal=True, label_visibility="hidden")


# if chosen_time == "All Time":
#     col5, col6 = st.columns(2)
#     with col5:
#         st.subheader(f"Distribution of decades among top tracks ({chosen_time})")
#         fig = px.sunburst(lt_dec, path=["decade", "year", "artist", "track"], values="count")
#         fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
#         st.plotly_chart(fig, use_container_width=True)
#     with col6:
#         st.subheader(f"Most listened releases ({chosen_time})")
#         st.write(top_rel_lt)

#     st.markdown("""---""")

#     st.subheader(f"Genres ({chosen_time})")
#     genrechart_fig = px.pie(gen_bc_lt, values='count', names='genre', title='Genres')
#     st.plotly_chart(genrechart_fig, use_container_width=True)

#     st.markdown("""---""")
#     st.subheader(f"Top songs release date vs. current popularity ({chosen_time})")
#     st.write("ie. how your musical taste in this period compares to the general public current musical preferences")
#     st.plotly_chart(tr_vs_date_lt, use_container_width=True)

# elif chosen_time == "Last 6 Months":
#     col5, col6 = st.columns(2)
#     with col5:
#         st.subheader(f"Genre Analysis ({chosen_time})")
#         fig = px.sunburst(sb_df_mt_top, path=['genres', "artists"], values="count")
#         fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
#         st.plotly_chart(fig, use_container_width=True)
#     with col6:
#         st.subheader(f"Most listened releases ({chosen_time})")
#         st.write(top_rel_mt)

#     st.markdown("""---""")
#     st.subheader(f"Top songs release date vs. current popularity ({chosen_time})")
#     st.write("ie. how your musical taste in this period compares to the general public current musical preferences")
#     st.plotly_chart(tr_vs_date_mt, use_container_width=True)

# elif chosen_time == "Last Month":
#     col5, col6 = st.columns(2)
#     with col5:
#         st.subheader(f"Genre Analysis ({chosen_time})")
#         fig = px.sunburst(sb_df_st_top, path=['genres', "artists"], values="count")
#         fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
#         st.plotly_chart(fig, use_container_width=True)
#     with col6:
#         st.subheader(f"Most listened releases: ({chosen_time})")
#         st.write(top_rel_st)

#     st.markdown("""---""")
#     st.subheader(f"Top songs release date vs. current popularity ({chosen_time})")
#     st.write("ie. how your musical taste in this period compares to the general public current musical preferences")
#     st.plotly_chart(tr_vs_date_st, use_container_width=True)

# st.markdown("""---""")


# # DEPRECATED: Sunburst genre analysis
# # with col5:
# #         st.subheader(f"Genre Analysis ({chosen_time})")
# #         fig = px.sunburst(sb_df_lt_top, path=['genres', "artists"], values="count")
# #         fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
# #         st.plotly_chart(fig, use_container_width=True)
