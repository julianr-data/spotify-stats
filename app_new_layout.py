from server import top_art, top_songs, genre_analysis, top_releases, top_tracks_vs_release
import streamlit as st
import plotly.express as px
import seaborn as sns
import pandas as pd

# Dataframes from server.py
big_art_df, top_art_lt_df, top_art_mt_df, top_art_st_df = top_art() # Top artists ¦ WARNING: API CALLS ARE MADE HERE
big_tr_df, top_tr_lt_df, top_tr_mt_df, top_tr_st_df = top_songs() # Top tracks ¦ WARNING: API CALLS ARE MADE HERE
sb_df_lt, sb_df_lt_top, sb_df_mt, sb_df_mt_top, sb_df_st, sb_df_st_top = genre_analysis(top_art_lt_df, top_art_mt_df, top_art_st_df) # Sunburst data
top_rel_lt, top_rel_mt, top_rel_st = top_releases(top_tr_lt_df, top_tr_mt_df, top_tr_st_df) # Top releases
tr_vs_date_lt, tr_vs_date_mt, tr_vs_date_st = top_tracks_vs_release(top_tr_lt_df, top_tr_mt_df, top_tr_st_df) # Top tracks vs release date

# Page config
st.set_page_config(page_title="Spotify Data Analysis",
                   page_icon="frontend/tasti1-transp2.png",
                   layout="wide", initial_sidebar_state="expanded",
                   menu_items={"Report a Bug": "https://github.com/julianr-data/spotify-stats",
                               "About": "https://github.com/julianr-data/spotify-stats"})

# Sidebar
st.sidebar.image("frontend/tasti1-transp3.png")
st.sidebar.title("Visualize your music taste")

st.sidebar.markdown("Get an analysis of your Spotify listening habits: top artists, songs, genres, saved items, etc. with colorful charts and graphs.", unsafe_allow_html=True)
st.sidebar.markdown("To use this app, you need to have a Spotify account. If you don't have an account, you can create one [here](https://www.spotify.com/signup/).", unsafe_allow_html=True)
st.sidebar.markdown("Your listening data comes from the [Spotify API](https://developer.spotify.com/documentation/web-api/).", unsafe_allow_html=True)

st.sidebar.markdown("© 2023 | Created by [Julián Rodríguez](https://www.linkedin.com/in/julianr-data/)")
st.sidebar.markdown("[Contact me](https://www.linkedin.com/in/julianr-data/) if you have any questions!")
st.sidebar.markdown("The code for this app can be found [here](https://github.com/julianr-data/spotify-stats)")

# Main page
st.title("Spotify Data Analysis")
st.markdown("""---""")

# Top artists
col1, col2 = st.columns(2)
cm = sns.light_palette("seagreen", reverse=True, as_cmap=True)
with col1:
    st.subheader("Top Artists")
    big_art_df_display = big_art_df.drop("Artist ID", axis=1) # .style.background_gradient(cmap=cm)
    st.write(big_art_df_display)

with col2:
    st.write("placeholder")

# Top tracks
col3, col4 = st.columns(2)
with col3:
    st.subheader("Top Tracks")
    big_tr_df_display = big_tr_df.drop("Track ID", axis=1)
    st.dataframe(big_tr_df_display)
with col4:
    st.write("placeholder")

st.markdown("""---""")

# Sunburst, top albums, top songs vs. release date
chosen_time = st.radio("Choose a time frame:", ("All Time", "Last 6 Months", "Last Month"), horizontal=True, label_visibility="hidden")


if chosen_time == "All Time":
    col5, col6 = st.columns(2)
    with col5:
        st.subheader(f"Genre Analysis: {chosen_time}")
        fig = px.sunburst(sb_df_lt_top, path=['genres', "artists"], values="count")
        fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
        st.plotly_chart(fig, use_container_width=True)
    with col6:
        st.subheader(f"Most listened releases: {chosen_time}")
        st.write(top_rel_lt)

    st.subheader(f"Top songs release date vs. current popularity ({chosen_time})")
    st.write("ie. how your musical taste in this period compares to the general public current musical preferences")
    st.plotly_chart(tr_vs_date_lt, use_container_width=True)

elif chosen_time == "Last 6 Months":
    col5, col6 = st.columns(2)
    with col5:
        st.subheader(f"Genre Analysis: {chosen_time}")
        fig = px.sunburst(sb_df_mt_top, path=['genres', "artists"], values="count")
        fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
        st.plotly_chart(fig, use_container_width=True)
    with col6:
        st.subheader(f"Most listened releases: {chosen_time}")
        st.write(top_rel_mt)

    st.subheader(f"Top songs release date vs. current popularity ({chosen_time})")
    st.plotly_chart(tr_vs_date_mt, use_container_width=True)

elif chosen_time == "Last Month":
    col5, col6 = st.columns(2)
    with col5:
        st.subheader(f"Genre Analysis: {chosen_time}")
        fig = px.sunburst(sb_df_st_top, path=['genres', "artists"], values="count")
        fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
        st.plotly_chart(fig, use_container_width=True)
    with col6:
        st.subheader(f"Most listened releases: {chosen_time}")
        st.write(top_rel_st)

    st.subheader(f"Top songs release date vs. current popularity ({chosen_time})")
    st.plotly_chart(tr_vs_date_st, use_container_width=True)

st.markdown("""---""")
