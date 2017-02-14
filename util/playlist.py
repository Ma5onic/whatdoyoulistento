class Playlist():
    """
    Playlist object that holds songs
    """

    def __init__(self, name, playlist_id, user):
        self.name = name
        self.id = playlist_id
        self.user = user
        self.tracks = []

    def add_song(self, song):
        from song import Song

        print "Adding {} by {}".format(song.track_name.encode("utf-8"), song.artist_name.encode("utf-8"))
        self.tracks.append(song.to_dictionary())

    def to_csv(self, filename, mode=None):
        import unicodecsv as csv

        filename = filename + ".csv"
        keys = self.tracks[0].keys()

        print "Writing {}\n".format(filename)
        if mode:
            with open(filename, mode) as file:
                dict_writer = csv.DictWriter(file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(self.tracks)
        else:
            with open(filename, "wb") as file:
                dict_writer = csv.DictWriter(file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(self.tracks)

    def request_songs(self, spotify_instance):
        from song import Song
        import spotipy

        offset = 0
        track_listing = spotify_instance.user_playlist_tracks(
            user=self.user, playlist_id=self.id, offset=offset)["items"]

        while len(track_listing) == 100:
            for track in track_listing:
                song = Song(self.id, self.name, track)
                song.add_all_song_features(spotify_instance)
                self.add_song(song)

            offset += 100
            track_listing = spotify_instance.user_playlist_tracks(
                user=self.user, playlist_id=self.id, offset=offset)["items"]

        for track in track_listing:
            song = Song(self.id, self.name, track)
            song.add_all_song_features(spotify_instance)
            self.add_song(song)
