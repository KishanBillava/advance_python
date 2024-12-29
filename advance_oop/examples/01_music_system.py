class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist}, Duration: {self.duration}s"

class Album:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.songs = []  # Composition: Album has a list of Song objects

    def add_song(self, song):
        """Add a song object to the album."""
        if isinstance(song, Song):
            self.songs.append(song)
        else:
            raise TypeError("Expected a Song object")

    def show_songs(self):
        """Display all songs in the album."""
        for song in self.songs:
            print(song)

# Using the classes
song1 = Song("Shape of You", "Ed Sheeran", 263)
song2 = Song("Blinding Lights", "The Weeknd", 200)

album = Album("Best Hits", 2020)
album.add_song(song1)  # Adding a Song object to Album
album.add_song(song2)

album.show_songs()  # Display all songs in the album

# output
# Shape of You by Ed Sheeran, Duration: 263s
# Blinding Lights by The Weeknd, Duration: 200s