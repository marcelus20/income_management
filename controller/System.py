import datetime
import hashlib

from controller import Income_controller, User_controller
from repository import User_Income_repository


class System:

    def __init__(self):
        pass

    def text_capture(self, msg, numeric):


        valid = False



        if not numeric:
            while (not valid):
                value = input(msg)
                if value == "":
                    print("You haven't typed anything, please, try again")
                    valid = False
                else:
                    break
        else:
            value = input(msg)
            value = value.replace(",", ".")
            if value == "":
                value = 0


        return value

    def hashing_pass(self, word):
        return hashlib.sha256(word.encode('ascii')).hexdigest()

    def print_tables_nicely(self, table):
        text = ""

        for i in range(len(table)):  # Lines of the Table
            for j in range(len(table[i])):  # columns of the table
                if j < len(table[i]):

                    if j == 6:
                        text += "|{:^40}|".format(table[i][j])

                    else:
                        if j == 4 or j == 5:
                            text += "|{:^10.2f}|".format(table[i][j])
                        else:
                            text += "|{:^10}|".format(table[i][j])
                    if j == len(table[i]) - 1:  # If column is the last column, break one line!
                        text += "\n"

        print(140 * "_")

        print(text)

    def sum(self, a, b):
        return float(a)+ float(b)

    def sub(self, a, b):
        return float(a)- float(b)

    def date_time_generator(self):
        return datetime.datetime.today().strftime('%d/%m/%Y')

    def welcome(self):

        lines = ["WELCOME"," TO THE ", "INCOME", "MANAGEMENT"]
        print(int(21-len(lines[-1]))*"==")
        for i in range(len(lines)):
            print("||{:^18}||".format(lines[i]))
        print(int(21 - len(lines[-1])) * "==")

    def home(self, id):
        options = ["Insert Transaction", "See Transactions", "Settings", "Close Application"]
        print(25*"=")
        for i in range(len(options)):
            print("||{}. {:^15}{}".format(i+1, options[i], "||"))
        print(25 * "=")
        result = self.text_capture("", False)
        if result == "1":
            self.ins_menu(id)
            self.home(id)
        elif result == "2":
            self.see_menu(id)
            self.home(id)
        elif result== "3":
            self.see_setting_menu(id)
            self.home(id)
        elif result == "4":
            exit()
        else:
            print("Type numbers between 1 and {}".format(len(options)))
            self.home(id)

    def see_menu(self, id):

        options = ["See All Data", "See Dat Between 2 Dates",
                   "See Balance", "See by description","Back to Menu"]
        print(25 * "=")
        for i in range(len(options)):
            print("||{}. {:^15}{}".format(i + 1, options[i], "||"))
        print(25 * "=")
        result = self.text_capture("", False)
        if result == "1":
            self.see_submenu(id)
            self.home(id)
        elif result == "2":
            self.see_dates_submenu(id)
            self.home(id)
        elif result == "3":
            Income_controller.Income_repository().see_balance()
        elif result == "4":
            Income_controller.Income_repository().see_by_description(id)
            self.home(id)
        elif result == "5":
            Income_controller.Income_repository().see_by_description(id)
            self.home(id)
        else:
            print("Type numbers between 1 and {}".format(len(options)))
            self.see_menu(id)

    def see_dates_submenu(self, id):
        options = ["See All Users", "See just Yours", "Back to Menu"]
        for i in range(len(options)):
            print("||{}. {:^15}{}".format(i + 1, options[i], "||"))
        print(25 * "=")
        result = self.text_capture("", False)
        if result == "1":
            Income_controller.Income_repository().see_trans_b_dates()
            self.home(id)
        elif result == "2":
            Income_controller.Income_repository().see_trans_b_dates_user(id)
            self.home(id)
        elif result == "3":
            self.home(id)
        else:
            print("Type numbers between 1 and {}".format(len(options)))
            self.see_dates_submenu(id)

    def ins_menu(self, id):
        options = ["Insert Transaction", "Update Description", "Back To Menu"]
        print(25 * "=")
        for i in range(len(options)):
            print("||{}. {:^15}{}".format(i + 1, options[i], "||"))
        print(25 * "=")
        result = self.text_capture("", False)
        if result == "1":
            Income_controller.Income_repository().ins_trans(id)
            self.home(id)
        elif result == "2":
            Income_controller.Income_repository().update_desc()
            self.home(id)
        elif result == "3":
            self.home(id)
        else:
            print("Type numbers between 1 and {}".format(len(options)))
            self.home(id)

    def see_setting_menu(self, id):
        options = ["Create a new User", "Update Your Password", "See all users and attributes", "Back to Menu"]
        print(25 * "=")
        for i in range(len(options)):
            print("||{}. {:^15}{}".format(i + 1, options[i], "||"))
        print(25 * "=")
        result = self.text_capture("", False)
        if result == "1":
            User_controller.User_repository().create_user()
            self.home(id)
        elif result == "2":
            User_controller.User_repository().pass_updater()
            self.home(id)
        elif result == "3":
            User_controller.User_repository().see_users()
        elif result == "4":
            self.home(id)
        else:
            print("Type numbers between 1 and {}".format(len(options)))
            self.see_menu(id)

    def see_submenu(self, id):
        options = ["See All Users Data", "See Just Yours", "Back to Menu"]
        print(25 * "=")
        for i in range(len(options)):
            print("||{}. {:^15}{}".format(i + 1, options[i], "||"))
        print(25 * "=")
        result = self.text_capture("", False)
        if result == "1":
            Income_controller.Income_repository().see_trans("")
            self.home(id)
        elif result == "2":
            Income_controller.Income_repository().see_trans(id)
            self.home(id)
        elif result == "3":
            self.home(id)
        else:
            print("Type numbers between 1 and {}".format(len(options)))
            self.see_menu(id)

    def balance_sum(self, table):

        balance = 0
        total_income = 0
        total_expense = 0

        for i in range(len(table)):
            balance += table[i][4]
            total_expense += table[i][3]
            total_income +=table[i][2]

        print(42 * " " + "Total Income: ", total_income)
        print(42 * " " + "Total Expense: ", total_expense)
        print(42 * " " + "Balance: ", balance)


