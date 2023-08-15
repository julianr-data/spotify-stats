# TASTIFY

**Spotify User Data Analysis:** join with your credentials and check out a ton of metrics about your listening habits.

![1](https://github.com/julianr-data/spotify-stats/assets/5545123/01d6b2ec-75d6-4b5e-a941-c08d5a72297a)

![2](https://github.com/julianr-data/spotify-stats/assets/5545123/1df780c8-f936-4f33-b455-25d82d8226dd)

[**CLICK HERE TO GO TO THE APP**](https://github.com/julianr-data/spotify-stats)

This app uses the official [Spotify API](https://developer.spotify.com/documentation/web-api) to retrieve your user data. This comes with a number of side effects:
- Depending on traffic, it might take several seconds to load (also consider that the app has to render a number of visualizations)
- If the data presented seems inaccurate, please note that the Spotify API tends to return relatively outdated or seemingly faulty/incomplete data. For example: albeit albums are supposed to have an assigned genre, [that field seems to be always empty by design](https://github.com/spotify/web-api/issues/157), and even famous artists turn out to be genre-less when asking Spotify for their details.
---
## Concepts and technologies used:
- Python: Plotly, Seaborn, Pandas
- Spotify API (via Spotipy)
- Streamlit
- Google Cloud
- OOP
- Git & Github
- OAuth
- HTML
---
I developed the idea for this app in late 2022. When I finally decided to do some research, I found out that, naturally, there were a lot of similar projects out there on Github. Out of all these, [this project by Deffro](https://github.com/Deffro/statify/blob/main/README.md) turned out to be a pretty complete version of what I wanted to do, at least in some aspects. So, while for learning purposes I wrote all the code, I did study his code as well, as a basis for the logic behind a number of features, to develop the structure of the app, and to make sure I was on the right track. Whenever I wrote code based on Deffro's work I made some contributions, such as:
- Commented functions and overall flow.
- Added requests to the API call to use in further analysis down the road.
- Modified the logic behind some functions dealing with tracks and artists to work by ID instead of name, therefore avoiding naming issues (eg. identically-named tracks).
- Added functions to write dataframes to csv and cat to terminal, to check data flow.
- Changed Top Albums logic: now it works by period.
- Wrote app in Streamlit.

Naming this app Statify seemed like the logical thing to do as well, but there are many similar projects our there sharing that name.

I will update this Readme as I continue adding features.
