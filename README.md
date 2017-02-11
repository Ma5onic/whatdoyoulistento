# whatdoyoulistento

## Description

This project is another example of a data driven approach to answering another question that often pops up in life; What do you listen to?

The real purpose behind this project is to satisfy my curiosity, answer other music related questions that have surfaced, and as always **have fun and become a better analyst**.

## Contents

## Process

### Defining Questions

1) What genres do I listen to?

2) Based on my taste profile, who should I see and who should I avoid at Coachella this year?

3) Can we visualize different genres by similar audio features?

4) How have your tastes changed over time?

### Setting Measurements

1) What genres do I listen to?

- This will be measured by querying each track in Spotify and saving its genre(s) value from the API response

- I will then look at the frequency counts for these genres and select the top N%

2) Based on my taste profile, who should I see and who should I avoid at Coachella this year?

- I will query the artist profile from the Spotify API, collect their genre(s). Next I can classify artists into 3 groups, those who's genres are in my top N% listened to genres, those who have a partial match with my top N% listened to genres, and those who have no intersection. Those who have no intersection are not likely to be bands I will want to see. Those with complete matches are definitely on my list to see, those with partial matches we will have to investigate further

- Another idea might be to filter my saved tracks by the genres the given artist belongs to and examine how well their audio features match up

3) Can we visualize different genres by similar audio features?

- I am suspecting the answer to this is yes and it is likely how Spotify themselves classify music. Regardless, we will pick 3 different genres from my Top N Genres list, find features that the genres share amongst themselves (but not the other genres; i.e. rock has avg loudness of 77 but ambient has avg loudness of 22) and use an ANOVA test to find if they are statistically significant at the p = .05 level

4) How have your tastes changed over time?

- Once I started looking through Spotify I noticed that I have many, lets call them 'legacy' playlists. I have been a religious Spotify since 2011 and I believe I should have enough data to measure change in music taste by examining the genre/saved song proportions year to year. Ex: In 2011 80% of my saved tracks were indie folk, in 2012 60% and 40% electronica etc)

### Collecting Data

- Where are we getting our data?

  - My Spotify account saved playlists will account for most of our data. My saved songs are mostly music that has been recommended to me that I either listen to or don't, which wouldn't make it a good measure of my taste as a lot of it falls under the latter. I do have a master playlist of all my Discover Weekly playlists dating back to early 2016 that is the best indicator of my tastes.

  - To answer question 2, I have already created a playlist of artists playing Coachella this year and their top 10 most popular songs that I used for another personal project a few weeks back. This data was collected using BeautifulSoup and the playlist was of course built using the Spotify Web API.

- How are we going to store our data?

  - I will be collecting my data in a list of python dictionaries, storing it more permanently by writing out to a csv file, and performing my data manipulation using the pandas module

- What does our data model look like?

### Analysis

### Interpret Results
