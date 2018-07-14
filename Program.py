"""
This solution was programmed by Chaotic Doom to meet the exam-board requirements of
OCR GCSE (9-1) Computer Science
J276/03 Programming project - Task 2, June 2018 series.
"""
from BasicUtils import *
from SQLController import *
from DataObjects import *

# variables to be used in every aspect of our program - global variables.
db_url = "Database.db"
db_user_table = "Users"
db_playlist_table = "Playlists"

users = {}
# -- form a connection to our user database. --
db = SQLManager(db_url)


#  playlist_db = SQLManager(playlist_db)

# --  retrieve all data from user database. --
# db.create_table(name=db_user_table, fields=[""])


def main():
    start_menu = Menu(35)
    start_menu.setTitle("Start Menu")
    start_menu.addItem("Manage Account")  # option 1
    start_menu.addItem("Manage Playlists")  # option 2

    answer = int(start_menu.getOption)
    if answer == 1:
        print("Ah so the user wants to manage accounts eh ?")
        manageAccounts()
    else:
        print("Ah so the user wants to manage playlist's eh ?")


def manageAccounts():
    account_menu = Menu(35)
    account_menu.setTitle("Manage Account")
    account_menu.addItem("Sign in")  # option 1
    account_menu.addItem("Sign up")  # option 2
    account_menu.addItem("Edit Account Settings")  # option 3
    answer = int(account_menu.getOption)
    if answer == 1:
        print("Going to sign in section!")
    elif answer == 2:
        print("Going to sign up section!")
    else:
        print("Going to edit account section!")


if __name__ == '__main__':
    print(["1", "2", "3"])
    print(['1', '2', '3'])
    #   main()
