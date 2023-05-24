from server import top_art, top_songs, genre_analysis
import streamlit as st
import plotly.express as px

# Dataframes from server.py
big_art_df, top_art_lt_df, top_art_mt_df, top_art_st_df = top_art() # Top artists ¦ WARNING: API CALLS ARE MADE HERE
big_tr_df, top_tr_lt_df, top_tr_mt_df, top_tr_st_df = top_songs() # Top tracks ¦ WARNING: API CALLS ARE MADE HERE
sb_df = genre_analysis(top_art_lt_df, top_art_mt_df, top_art_st_df) # Sunburst data

# Sidebar
st.sidebar.title("Spotify Data Analysis")
st.sidebar.markdown("This app is a data analysis of your Spotify account. It will show you your top artists, top songs and a sunburst chart with your music taste.")
st.sidebar.markdown("To use this app, you need to have a Spotify account and log in with your credentials. If you don't have an account, you can create one [here](https://www.spotify.com/signup/).")
st.sidebar.markdown("If you have any questions, you can contact me on [LinkedIn](https://www.linkedin.com/in/alejandro-fernandez-fernandez/).")
st.sidebar.markdown("This app was created by [Alejandro Fernández](https://www.linkedin.com/in/alejandro-fernandez-fernandez/).")
st.sidebar.markdown("The code for this app can be found [here]")
st.sidebar.markdown("The data for this app comes from the [Spotify API](https://developer.spotify.com/documentation/web-api/).")

# Main page
st.title("Spotify Data Analysis")
st.markdown("This app is a data analysis of your Spotify account. It will show you your top artists, top songs and a sunburst chart with your music taste.")
st.markdown("To use this app, you need to have a Spotify account and log in with your credentials. If you don't have an account, you can create one [here](https://www.spotify.com/signup/).")
st.markdown("If you have any questions, you can contact me on [LinkedIn](https://www.linkedin.com/in/alejandro-fernandez-fernandez/).")
st.markdown("This app was created by [Alejandro Fernández](https://www.linkedin.com/in/alejandro-fernandez-fernandez/).")
st.markdown("The code for this app can be found [here]")
st.markdown("The data for this app comes from the [Spotify API](https://developer.spotify.com/documentation/web-api/).")

# Top artists
st.header("Top Artists")
st.markdown("Here you can see your top artists. You can choose between the last 4 weeks, the last 6 months or all time.")
st.markdown("You can also choose how many artists you want to see. The default is 10.")
st.markdown("You can hover over the bars to see the name of the artist and the number of times you have listened to them.")
st.markdown("You can also click on the legend to hide or show the artists you want.")
st.markdown("If you want to see the top artists of a different time period, you can change the time period and click on the button again.")
st.markdown("If you want to see more artists, you can change the number of artists and click on the button again.")
st.write(big_art_df)

# Top tracks
st.header("Top Tracks")
st.markdown("Here you can see your top tracks. You can choose between the last 4 weeks, the last 6 months or all time.")
st.markdown("You can also choose how many tracks you want to see. The default is 10.")
st.markdown("You can hover over the bars to see the name of the track and the number of times you have listened to it.")
st.markdown("You can also click on the legend to hide or show the tracks you want.")
st.markdown("If you want to see the top tracks of a different time period, you can change the time period and click on the button again.")
st.markdown("If you want to see more tracks, you can change the number of tracks and click on the button again.")
st.write(big_tr_df)

# Sunburst
st.header("Sunburst")
st.markdown("Here you can see a sunburst chart with your music taste.")
st.markdown("The chart shows the genres you listen to and the artists that belong to each genre.")
st.markdown("The size of the arcs represents the number of times you have listened to the genre or artist.")
st.markdown("You can hover over the arcs to see the name of the genre or artist and the number of times you have listened to it.")
st.markdown("You can also click on the legend to hide or show the genres or artists you want.")
st.markdown("If you want to see the top artists of a different time period, you can change the time period and click on the button again.")
st.markdown("If you want to see more artists, you can change the number of artists and click on the button again.")

fig = px.sunburst(sb_df, path=['genres', "artists"], values="count")
fig.update_layout(margin=dict(t=10, l=0, r=0, b=0), title={'text': "visualizing your music taste",'x': 0.5, 'y': 0.92})
st.plotly_chart(fig)


# '''tres opciones para solucionar problema de grafico crowdded
# 1. graficar solo generos, sin artistas, tomar solo los 10 mas escuchados
# 2. graficar solo los 10 generos mas escuchados, con artistas
# 3, por cada artista, tomar el genero mas counteado y graficar eso'''
