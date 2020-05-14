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

    def get_title(self):
        return self.title

    # function find_object look for name in object. since song uses title instead of name
    # you can use read only property -- this will  allow create read-only property name "name" for title
    # which can be use in find_object
    name = property(get_title)


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
            # remvoing refrence back to Artist by not assigning Artist['Various Artists']
            self.artist = 'Various Artists'
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Add a song to the track list

        Args:
            song (Song): Title of the song to add
            position(optional(int)): If specified the song will be added to that  position
                in the track list otherwise itll be added to end of the track list

        Returns:None

        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


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

    def add_song(self, name, year, title):
        """Adds new song to collections of album
        This method will add the data in collection if it doesnt exits

        Args:
            name (str): the name of the album
            year(int): Release year
            title(str): Title of the song

        Returns:

        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + "not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found Album " + name)
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
    # # new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field), sep=":")

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            new_artist.add_song(album_field, year_field, song_field)


    return artist_list


def check_list(artist_list):
    with open ('check_file.txt', 'w') as check_file:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.name}".format(new_artist, new_album, new_song), file=check_file)

if __name__ == '__main__':
    artist = load_data()
    check_list(artist)
    print(len(artist))



