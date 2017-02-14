class Song():
    """
    Song object to be used throughout this project
    """
    import spotipy

    def __init__(self, playlist_id, playlist_name, response_item):
        """
        Creates a song object from an API response
        """
        self.playlist_id = playlist_id
        self.playlist_name = playlist_name
        self.date_discovered = response_item['added_at']

        self.track_id = response_item["track"]["id"]
        self.track_name = response_item["track"]["name"]
        self.track_popularity = response_item["track"]["popularity"]

        self.album_id = response_item["track"]["album"]["id"]
        self.album_name = response_item["track"]["album"]["name"]

        self.artist_id = response_item["track"]["artists"][0]["id"]
        self.artist_name = response_item["track"]["artists"][0]["name"]

    def add_album_features(self, spotify_instance):
        """
        Adds album popularity from album request
        """
        self.album_popularity = spotify_instance.album(str(self.album_id))[
            "popularity"]

    def add_artist_features(self, spotify_instance):
        """
        Add artist features from request
        """
        response = spotify_instance.artist(str(self.artist_id))
        self.artist_popularity = response["popularity"]
        self.genres = response["genres"]

    def add_audio_features(self, spotify_instance):
        """
        Adds spotify audio features to Song
        """
        response = spotify_instance.audio_features(str(self.track_id))[0]
        self.acousticness = response["acousticness"]
        self.danceability = response["danceability"]
        self.duration_ms = response["duration_ms"]
        self.energy = response["energy"]
        self.instrumentalness = response["instrumentalness"]
        self.key = response["key"]
        self.liveness = response["liveness"]
        self.loudness = response["loudness"]
        self.mode = response["mode"]
        self.speechiness = response["speechiness"]
        self.tempo = response["tempo"]
        self.time_signature = response["time_signature"]
        self.valence = response["valence"]

    def add_all_song_features(self, spotify_instance):
        self.add_album_features(spotify_instance)
        self.add_artist_features(spotify_instance)
        self.add_audio_features(spotify_instance)

    def to_dictionary(self):
        """
        Convenience function to make a Song object write to csv easily
        """
        return self.__dict__
