# Songs

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. Inside `hw` folder, create a new folder `songs`. Within the `songs` folder, create files named `1.sql` through `9.sql`.
3. Download `songs.db` file from [`songs.db`](./songs/songs.db) on GitHub. Copy the downloaded file `songs.db` into the `data` folder, which should be inside the main `OIM3600` folder.

## Understanding

Provided to you is a file called `songs.db`, a SQLite database that stores data from Spotify about songs and their artists. This dataset contains the top 100 streamed songs on Spotify in 2018. In a terminal window, run `sqlite3 songs.db` so that you can begin executing queries on the database.

First, when `sqlite3` prompts you to provide a query, type `.schema` and press <kbd>enter</kbd>. This will output the `CREATE TABLE` statements that were used to generate each of the tables in the database. By examining those statements, you can identify the columns present in each table.

Notice that every `artist` has an `id` and a `name`. Notice, too, that every `song` has a `name`, an `artist_id` (corresponding to the `id` of the artist of the song), as well as values for the danceability, energy, key, loudness, speechiness (presence of spoken words in a track), valence, tempo, and duration of the song (measured in milliseconds).

The challenge ahead of you is to write SQL queries to answer a variety of different questions by selecting data from one or more of these tables. After you do so, you’ll reflect on the ways Spotify might use this same data in their annual [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) campaign to characterize listeners’ habits.

## Implementation Details

For each of the following problems, you should write a single SQL query that outputs the results specified by each problem. Your response must take the form of a single SQL query, though you may nest other queries inside of your query. You **should not** assume anything about the ids of any particular songs or artists: your queries should be accurate even if the id of any particular song or person were different. Finally, each query should return only the data necessary to answer the question: if the problem only asks you to output the names of songs, for example, then your query should not also output each song’s tempo.

1. In `1.sql`, write a SQL query to list the distinct artist names from the database.
   - Your query should output a table with a single column for the name of each artist.
2. In `2.sql`, write a SQL query to count the number of songs in the database.
   - Your query should output a single row with the count of songs.
3. In `3.sql`, write a SQL query to find the artist with the most songs in the database.
   - Your query should output the name of the artist and the number of songs they have.
4. In `4.sql`, write a SQL query that returns the average energy of all the songs.
   - Your query should output a table with a single column and a single row containing the average energy.
5. In `5.sql`, write a SQL query that lists the names of songs that are by Drake.
   - Your query should output a table with a single column for the name of each song.
   - You should not make any assumptions about what Drake’s `artist_id` is.
6. In `6.sql`, write a SQL query to find the song with the highest energy among the songs by Drake.
   - Your query should output the name of the song and its energy value.
   - You should not make any assumptions about what Drake’s `artist_id` is.
7. In `7.sql`, write a SQL query to list the names of songs with a tempo above the average tempo of all songs.
   - Your query should output a table with a single column for the name of each song.
   - You should not make any assumptions about what the average tempo of all songs is.
8. In `8.sql`, write a SQL query that lists the names of the songs that feature other artists.
   - Songs that feature other artists will include “feat.” in the name of the song.
   - Your query should output a table with a single column for the name of each song.
9. **Your Query Challenge**: In `9.sql`, create your own SQL query that uses at least one JOIN operation to extract specific information from the database. Write the SQL query, state your purpose, and provide a brief explanation.

<details>
<summary>Hints:</summary>

See this [SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!
  
</details>

## Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) is a feature presenting Spotify users’ 100 most played songs from the past year. In 2021, Spotify Wrapped calculated an “[Audio Aura](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/)” for each user, a “reading of [their] two most prominent moods as dictated by [their] top songs and artists of the year.” Suppose Spotify determines an audio aura by looking at the average energy, valence, and danceability of a person’s top 100 songs from the past year. Create `answers.txt` inside the `songs` folder, reflect on the following questions:

1. If songs.db contains the top 100 songs of one listener from 2018, how would you characterize their audio aura?
2. Hypothesize about why the way you’ve calculated this aura might not be very representative of the listener. What better ways of calculating this aura would you propose?

Be sure to submit `answers.txt` along with your `.sql` files!

## How to Submit

- Save all the files opened in VS Code. Format your Python code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.

---

### Acknowledgements

Dataset from [Kaggle](https://www.kaggle.com/nadintamer/top-spotify-tracks-of-2018).
