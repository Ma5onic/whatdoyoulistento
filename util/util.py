def create_auth_session():
    """
    Returns authorizes spotify session
    """
    import sys
    import spotipy
    import spotipy.util as util

    scope = 'user-library-read'

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print "Usage: %s username" % (sys.argv[0],)
        sys.exit()

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
    else:
        print "Can't get token for", username
    return sp


def read_csv_to_list_of_dictionaries(filename):
    """
    input - list of dictionaries as data, filename to be read from
    output - list of dictionaries
    """
    import unicodecsv as csv

    data = []

    with open(filename, "rb") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data


def write_list_of_dictionaries_to_file(data, filename, mode=None):
    """
    input - list of dictionaries as data, filename to be written to
    output - none, out file.
    """
    import unicodecsv as csv

    keys = data[0].keys()

    if mode:
        with open(filename, mode) as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    else:
        with open(filename, "wb") as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)


def get_songs_from_playlist(user, playlist_id, spotify_instance):
    tracks = []
    fields = "items"
    offset = 0
    result = spotify_instance.user_playlist_tracks(
        user, playlist_id, fields, offset=offset)["items"]

    while len(result) == 100:
        offset += 100
        result = spotify_instance.user_playlist_tracks(
            user, playlist_id, fields, offset=offset)["items"]
        tracks.extend(result)

    offset += 100
    result = spotify_instance.user_playlist_tracks(
        user, playlist_id, fields, offset=offset)["items"]
    tracks.extend(result)

    return tracks


def deconstruct_genre(filename):
    from util.util import read_csv_to_list_of_dictionaries, write_list_of_dictionaries_to_file

    data = read_csv_to_list_of_dictionaries(filename)
    genre_data = []

    # for each item in the row 'genre' field, create a new row with only the
    # genre changing
    for row in data:
        genre_list = row['genres'].replace("[", "").replace("]", "").split(",")

        # append these rows to genre_blast
        for genre in genre_list:
            row['genre'] = genre
            genre_data.append(row.copy())

    # write genre blast to its own csv
    outfile = filename.split(".")[0] + "_genre.csv"
    write_list_of_dictionaries_to_file(genre_data, outfile)
