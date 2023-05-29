from server import top_art, top_songs, genre_analysis, top_releases
import streamlit as st
import plotly.express as px
import seaborn as sns
import pandas as pd

# Dataframes from server.py
big_art_df, top_art_lt_df, top_art_mt_df, top_art_st_df = top_art() # Top artists ¦ WARNING: API CALLS ARE MADE HERE
big_tr_df, top_tr_lt_df, top_tr_mt_df, top_tr_st_df = top_songs() # Top tracks ¦ WARNING: API CALLS ARE MADE HERE
sb_df_lt, sb_df_lt_top, sb_df_mt, sb_df_mt_top, sb_df_st, sb_df_st_top = genre_analysis(top_art_lt_df, top_art_mt_df, top_art_st_df) # Sunburst data
top_rel_lt, top_rel_mt, top_rel_st = top_releases(top_tr_lt_df, top_tr_mt_df, top_tr_st_df) # Top releases

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

# Top artists and tracks
col1, col2 = st.columns(2)
cm = sns.light_palette("seagreen", reverse=True, as_cmap=True)

# Top artists
with col1:
    st.subheader("Top Artists")
    big_art_df_display = big_art_df.drop("Artist ID", axis=1) # .style.background_gradient(cmap=cm)
    st.write(big_art_df_display)

with col2:
    # Top tracks
    st.subheader("Top Tracks")
    big_tr_df_display = big_tr_df.drop("Track ID", axis=1)
    st.dataframe(big_tr_df_display)

st.markdown("""---""")

# Sunburst and other graph

col3, col4 = st.columns(2)

with col3:
    # Sunburst
    st.subheader("Genre Analysis")

    chosen_sb = st.radio("Choose a time frame:", ("All Time", "Last 6 Months", "Last Month"), horizontal=True, label_visibility="hidden")
    # st.subheader(f"Top Genres - {chosen_sb}")

    if chosen_sb == "All Time":
        fig = px.sunburst(sb_df_lt_top, path=['genres', "artists"], values="count")
        fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
        st.plotly_chart(fig, use_container_width=True)

    elif chosen_sb == "Last 6 Months":
        fig = px.sunburst(sb_df_mt_top, path=['genres', "artists"], values="count")
        fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
        st.plotly_chart(fig, use_container_width=True)

    elif chosen_sb == "Last Month":
        fig = px.sunburst(sb_df_st_top, path=['genres', "artists"], values="count")
        fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
        st.plotly_chart(fig, use_container_width=True)

with col4:
    st.subheader("Most listened releases")
    chosen_df = st.radio("Choose a time frame:", ("all Time", "last 6 Months", "last Month"), horizontal=True, label_visibility="hidden")

    if chosen_df == "all Time":
        st.write(top_rel_lt)
    elif chosen_df == "last 6 Months":
        st.write(top_rel_mt)
    elif chosen_df == "last Month":
        st.write(top_rel_st)

st.markdown("""---""")




# col3, col4, col5 = st.columns(3)
# with col3:
#     st.subheader("Long Term")
#     fig = px.sunburst(sb_df_lt_top, path=['genres', "artists"], values="count")
#     fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
#     st.plotly_chart(fig, use_container_width=True)


# with col4:
#     st.subheader("Medium Term")
#     fig = px.sunburst(sb_df_mt_top, path=['genres', "artists"], values="count")
#     fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
#     st.plotly_chart(fig, use_container_width=True)

# with col5:
#     st.subheader("Short Term")
#     fig = px.sunburst(sb_df_st_top, path=['genres', "artists"], values="count")
#     fig.update_layout(margin=dict(t=0, l=10, r=10, b=0))
#     st.plotly_chart(fig, use_container_width=True)



# '''tres opciones para solucionar problema de grafico crowdded
# 1. graficar solo generos, sin artistas, tomar solo los 10 mas escuchados
# 2. graficar solo los 10 generos mas escuchados, con artistas
# 3, por cada artista, tomar el genero mas counteado y graficar eso'''
