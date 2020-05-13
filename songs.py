class Song:
    """ Class to represent a song

    Attributes:
        title (str): The title of te song
        artist (Artist): An artist object representing the songs creator.
        duration (in): The duration of the song in seconds
    """
    def __init__(self, title, artist, duration=0):
        """Song init method

            :param title: Initialises the 'title' attribute
            :param artist: An Artist object representing the song creator.
            :param duration: (Optional) Initial value for the duration attribute -- default value is zero
            :return: None"""
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represt Album, using it's track

        Attributes:
            name (str): name of the album
            year (int): release year
            artist (Artist) : name of the artist


    """

    def __init__(self, name, year, artist=None):

        self.name = name,
        self.year = year,
        if artist is None:
            self.artist = Artist['Various Artists']
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """
        :param song (Song): name of the song
        :param position: if specified song will added to position in track list, otherwise song will be
                        added to end of the list
        :return:None
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """ Basic Class to store Artist detail

        Attributes:
            name (str): name of the artist
            albums (Lits[Album]): a list of album by artist

        Methods:
            add_album: Use to add a new album to the artist's album list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new Album to the list

        :param album: an object of album to add to the list.
                        If the album is already present, it will not be added (although it is yet to implemented)
        :return:None
        """
        self.albums.append(album)


def load_data():
    """Load_data
        logic is if artist_name is none it will create an Artist object. move on to if album is none
        which creates an object of album which takes the artist name, year and album name
        than moving to the songs which will be added( all four if statement wont execute) until
        new row of album and artist comes which will set the album to none --
        eventuall all of the artist songs will be added. last one will be added after the whole execution

    Returns: artist_list

    """
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            # print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field), sep=":")

            # Create Artist Object and add it's Album
            if new_artist is None:
                new_artist = Artist(artist_field)
                # print("new_artistobject.name: {}\n new_artistobject.albums: {}".format(new_artist.name, new_artist.albums))
            elif new_artist.name != artist_field:
                # print("object new_artist_ name : ", new_artist.name)
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            # adds Album
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                # print("album_none", new_album.name, sep=':')
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)
                # print("album_!=", new_album.name, sep=':')

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


if __name__ == '__main__':
    artist = load_data()

    print(len(artist))
