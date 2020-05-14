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

        self.name = name
        self.year = year
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

    def add_song(self, album_name, year, title):
        """Adds new song to collections of album
        This method will add the data in collection if it doesnt exits

        Args:
            album_name (str): the name of the album
            year(int): Release year
            title(str): Title of the song

        Returns:

        """
        album_found = find_object(album_name, self.albums)
        if album_found is None:
            print(album_name + "not found")
            album_found = Album(album_name, year, self)
            self.add_album(album_found)
        else:
            print("Found Album " + album_name)
        album_found.add_song(title)




def find_object(field, object_list):
    """check Object_list to see if an with a 'name' attribute equals to field exists. return it if do"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    """Load_data


        # logic is if artist_name is none it will create an Artist object. move on to if album is none
        # which creates an object of album which takes the artist name, year and album name
        # than moving to the songs which will be added( all four if statement wont execute) until
        # new row of album and artist comes which will set the album to none --
        # eventuall all of the artist songs will be added. last one will be added after the whole execution

    Returns: artist_list

    """
    # part of previous version
    # new_artist = None
    # new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field), sep=":")


            new_artist=find_object(new_artist,artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
            new_artist.add_song(album_field, year_field, song_field)


            # part of previous version (kept it here for reference
            # # Create Artist Object and add it's Album
            # if new_artist is None:
            #     new_artist = Artist(artist_field)
            #     artist_list.append(new_artist)
            #     # print("new_artistobject.name: {}\n new_artistobject.albums: {}".format(new_artist.name, new_artist.albums))
            # elif new_artist.name != artist_field:
            #     # check if artist is already in list
            #     new_artist = find_object(artist_field, artist_list)
            #     if new_artist is None:
            #         new_artist = Artist(artist_field)
            #         artist_list.append(new_artist)
            #     new_album=None
            #
            #     # new_artist= find_object(artist_field, artist_list)
            #     # print("object new_artist_ name : ", new_artist.name)
            #
            # # adds Album
            # if new_album is None:
            #     new_album = Album(album_field, year_field, new_artist)
            #     new_artist.add_album(new_album)
            #     # print("album_none", new_album.name, sep=':')
            # elif new_album.name != album_field:
            #     # We gonna check if album already exists if not than create another
            #     # same process as artist. check for album if already exist in list
            #     new_album = find_object(album_field, new_artist.albums)
            #     if new_album is None:
            #         new_album = Album(album_field, year_field, new_artist)
            #         new_artist.add_album(new_album)
            #
            #     # print("album_!=", new_album.name, sep=':')
            # new_song = Song(song_field, new_artist)
            # new_album.add_song(new_song)

    return artist_list


def check_list(artist_list):
    with open ('check_file.txt', 'w') as check_file:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=check_file)


if __name__ == '__main__':
    artist = load_data()
    check_list(artist)
    print(len(artist))



