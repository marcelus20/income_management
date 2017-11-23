import sqlite3
from controller import System
from repository import User_Income_repository
from models import User_
import getpass


class User_repository:

    def __init__(self):
        db = 'DB/application.db'
        self.conn = sqlite3.connect(db)

    def create_admin(self):

        c = self.conn.execute("""
        INSERT INTO users VALUES(?, ?, ?, ?, ?)
        """, (1, "admin", "admin", "admin", System.System().hashing_pass("admin")))
        self.conn.commit()
        c.close()

    def create_user(self):
        #c = self.conn.cursor()
        print("creating a new user")
        user = User_


        #retrieveing the last id:

        user.id = int(User_Income_repository.DB_dealing().last_id_retriever("users")) + 1
        user.username = System.System().text_capture("type the USERNAME: ", False)
        user.name = System.System().text_capture("Type the NAME of this user: ", False)
        user.last_name = System.System().text_capture("Type the LAST NAME of this user: ", False)
        user.password = System.System().text_capture("Type the Password: ", False)

        hashedWord = System.System().hashing_pass(user.password)

        print("REGISTERING USER: ")

        print(
            user.id, user.username, user.name,
            user.last_name, hashedWord
        )
        User_Income_repository.DB_dealing().insert_user(
            user.id, user.username, user.name,
            user.last_name, hashedWord
        )
        print("User created successfully")

    def pass_updater(self):

        new_pass = System.System().text_capture("type your new password: ", False)
        hashed_pass = System.System().hashing_pass(new_pass)
        hashed_pass = str(hashed_pass)
        User_Income_repository.DB_dealing().updater(hashed_pass, 2, "users", "password")
        print("Password updated successfully!")

    def see_users(self):
        print("|{:^10}||{:^10}||{:^10}||{:^10}||{:^10}|".format("id", "User Name", "Name", "Last_Name", "Password"))
        table = User_Income_repository.DB_dealing().tables_selection("users","")
        System.System().print_tables_nicely(table)

    def login(self):
        print("PLEASE, LOG INTO THE SYSTEM")
        username = System.System().text_capture("Username: ", False)

        data = User_Income_repository.DB_dealing().data_selector(username)
        valid = False
        counter = 0
        while not valid:
            if counter !=3:

                password = getpass.getpass("Password: ")
                hashed = System.System().hashing_pass(password)


                if data != []:

                    if hashed == data[0][-1]:
                        print("pass correct")
                        return data[0][0]
                        break
                    else:
                        counter +=1
                        print("username or pass not correct")
                else:
                    counter += 1
                    print("username or pass not correct")
            else:
                print("System is closing after many log in attempts")
                exit()




