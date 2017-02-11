# whatdoyoulistento

## Description

This project is another example of a data driven approach to answering another question that often pops up in life; What do you listen to?

The real purpose behind this project is to satisfy my curiosity, answer other music related quesions that have surfaced, and as always **have fun and become a better analyst**.

## Process

### Defining Questions

1) What genres do I listen to?

2) Based on my taste profile, who should I see and who should I avoid at Coachella this year?

3) Can we visualize different genres by similar audio features?

### Setting Measurements

1) What genres do I listen to?

- This will be measured by querying each track in Spotify and saving its genre(s) value from the API response

- I will then look at the frequency counts for these genres and select the top N%

2) Based on my taste profile, who should I see and who should I avoid at Coachella this year?

- I will query the artist profile from the Spotify API, collect their genre(s). Next I can classify artists into 3 groups, those who's genres are in my top N% listened to genres, those who have a partial match with my top N% listened to genres, and those who have no intersection. Those who have no intersection are not likely to be bands I will want to see. Those with complete matches are definitely on my list to see, those with partial matches we will have to investigate further

- Another idea might be to filter my saved tracks by the genres the given artist belongs to and examine how well their audio features match up

3) Can we visualize different genres by similar audio features?

- I am suspecting the answer to this is yes and it is likely how Spotify themselves classify music. Regardless, we will pick 3 different genres from my Top N Genres list, find features that the genres share amongst themselves (but not the other genres; i.e. rock has avg loudness of 77 but ambient has avg loudness of 22) and use an ANOVA test to find if they are statistically significant at the p = .05 level

### Collecting Data

- How are we going to store our data?

- What does our data model look like?

### Analysis

### Interpret Results

s s
