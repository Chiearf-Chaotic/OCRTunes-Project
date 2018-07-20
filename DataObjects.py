class User:
    """
    Note:
    This class may be changed into a user manager, controlling the extraction and boolean logics.
    """
    def __init__(self, name, password, dob, artist, genre):
        self.username = name
        self.password = password
        self.dob = dob
        self.artist = artist
        self.genre = genre

    def confirmUser(self, username, password):
        if (self.username == username) and (self.password == password):
            return True
        return False

    def get_name(self):
        return self.username

    def get_password(self):
        return self.password

    def get_fav_artist(self):
        return self.artist

    def get_fav_genre(self):
        return self.genre


class Song:
    def __init__(self, title, length, genre, artist):
        self.title = title
        self.length = length
        self.genre = genre
        self.artist = artist

    def get_title(self):return self.title
    def get_length(self): return self.length
    def get_genre(self): return self.genre
    def get_artist(self): return self.artist

    def set_title(self, new_title): self.title = new_title
    def set_length(self, new_length): self.length = new_length
    def set_genre(self, new_genre): self.genre = new_genre
    def set_artist(self, new_artist): self.artist = new_artist


class Playlist:
    def __init__(self, title, length, genre, artist):
        self.title = title
        self.songs = []
        self.length = length
        self.genre = genre
        self.artist = artist

    def auto_generate(self, songs):
        return False
