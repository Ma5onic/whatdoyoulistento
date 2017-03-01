# whatdoyoulistento

## Description

This project is another example of a data driven approach to answering another question that often pops up in life; What do you listen to?

The real purpose behind this project is to satisfy my curiosity, answer other music related questions that have surfaced, and as always **have fun and become a better analyst**.

## Contents

`util` directory will contain all the Python code used to wrangle and manipulate our data

`What Do You Listen To Notebook.ipynb` is the Jupyter Notebook where I walk through the process outlined below. This contains the answers to the questions and some nice Tableau charts

## Process

### Defining Questions

1) What genres do I listen to?

2) How have your tastes changed over time?

3) Can we visualize differences between genres by audio feature?

4) Based on my taste profile, who should I see and who should I avoid at Coachella this year?

### Setting Measurements

1) What genres do I listen to?

- This will be measured by querying each track in Spotify and saving its genre(s) value from the API response

- I will then look at the frequency counts for these genres and select the top 50%

2) How have your tastes changed over time?

- I will group my saved songs by 'date discovered' (either by year or combine a few years) and view my top ten genres in those groupings and compare. I suspect my 2011/2012 genres will be full of indie/folk and we should see a gradual transition to more electronic music


3) Can we visualize different genres by similar audio features?

- I am suspecting the answer to this is yes and it is likely how Spotify themselves classify music. Regardless, we will pick 3-4 different genres from my Top N Genres list, find features that the genres share amongst themselves (but not the other genres; i.e. rock has avg loudness of 77 but ambient has avg loudness of 22) and use an ANOVA test to find if they are statistically significant at the p = .005 level


4) Based on my taste profile, who should I see and who should I avoid at Coachella this year?

- To measure this I will look at an artist's genre property and see which artists have the most genre's in common with my Top N. I know this will favor those with more genres but it is rare that Spotify assigns 1-2 genres an artist so I suspect, while not perfect, this should generate some accurate results with bands I already know I want to see and potentially some I haven't listened to and will like

### Collecting Data

- Where are we getting our data?

  - My Spotify account saved playlists will account for most of our data. My saved songs are mostly music that has been recommended to me that I either listen to or don't, which wouldn't make it a good measure of my taste as a lot of it falls under the latter. I do have a master playlist of all my Discover Weekly playlists dating back to early 2016 that is the best indicator of my tastes.

  - To answer question 4, I have already created a playlist of artists playing Coachella this year and their top 10 most popular songs that I used for another personal project a few weeks back. This data was collected using BeautifulSoup and the playlist was of course built using the Spotify Web API.

- How are we going to store our data?

  - I will be collecting my data in a list of python dictionaries, storing it more permanently by writing out to a csv file, and performing my data manipulation using the pandas module


### Analysis, Visualizations, Results, and Limitations are in the notebook.ipynb file. ENJOY!
