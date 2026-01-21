# 9. Aggregation (HAS-A, weaker 'whole-part')
# Concept: Whole has parts, but parts can exist independently
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f'"{self.title}" by {self.artist}'

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        if isinstance(song, Song):
            self.songs.append(song)
            print(f"Added {song} to playlist '{self.name}'.")
        else:
            print("Can only add Song objects to the playlist.")

    def display_playlist(self):
        print(f"\nPlaylist: {self.name}")
        if not self.songs:
            print("  (empty)")
            return
        for i, song in enumerate(self.songs):
            print(f"  {i+1}. {song}")

song1 = Song("Bohemian Rhapsody", "Queen")
song2 = Song("Stairway to Heaven", "Led Zeppelin")
song3 = Song("Hotel California", "Eagles")

rock_playlist = Playlist("Classic Rock Hits")
favorites_playlist = Playlist("My Favorites")

rock_playlist.add_song(song1)
rock_playlist.add_song(song2)

favorites_playlist.add_song(song1)
favorites_playlist.add_song(song3)

rock_playlist.display_playlist()
favorites_playlist.display_playlist()
