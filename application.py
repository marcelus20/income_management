from controller import User_controller, System, Income_controller
from repository import User_Income_repository
import sqlite3
import os


class App():


    def __init__(self):

        s = System.System()

        u_i = User_Income_repository
        if not os.path.isfile("DB/application.db"):
            u_i.DB_dealing()

        user = User_controller.User_repository()



        s.welcome()



        user.id = user.login()
        if user.id != None:
            System.System().home(user.id)




app = App()
#a = Income_controller.Income_repository().see_trans(2)
