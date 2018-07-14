class User:
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

# class Playlist:
#   def
