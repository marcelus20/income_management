import sqlite3
from repository import User_Income_repository
from models import Income
from controller import System


class Income_repository:
    def __init__(self):
        db = "DB/application.db"
        self.conn = sqlite3.connect(db)

    def ins_trans(self, user_id):
        inc = Income.Income

        inc.id = User_Income_repository.DB_dealing().last_id_retriever("income")
        inc.date = System.System().date_time_generator()
        inc.income = System.System().text_capture("Insert your income: ", True)
        inc.expense = System.System().text_capture("Insert your expense: ", True)
        inc.bal_t = System.System().sub(inc.income, inc.expense)

        inc.balance = System.System().sum(User_Income_repository.DB_dealing().last_balance_retriever(inc.id),
                                          inc.bal_t)

        inc.bal_t = "{:.2f}".format(inc.bal_t)
        inc.balance = "{:.2f}".format(inc.balance)
        inc.description = System.System().text_capture("Insert the description: ", False)

        User_Income_repository.DB_dealing().income_insert(
            inc.id+1, inc.date, inc.income, inc.expense,
            inc.bal_t, inc.balance, inc.description, user_id
        )



        if inc.bal_t == None:
            inc.bal_t = 0
        print(inc.id, inc.date,
              inc.income, inc.expense,
              inc.bal_t, inc.balance,
              inc.description)

    def see_trans(self, id):
        print("|{:^10}||{:^10}||{:^10}||{:^10}||{:^10}||{:^10}||{:^10}||{:^10}|".format("id", "Date",
                                                                                            "Income", "Expense",
                                                                                            "t_balance",
                                                                                            "balance",
                                                                                            "description", "user_name"))
        table = User_Income_repository.DB_dealing().tables_selection("income", id)

        System.System().print_tables_nicely(table)
        System.System().balance_sum(table)

    def see_trans_b_ids(self, id):
        self.see_trans("")
        date_1 = System.System().text_capture("Insert id 1: ", False)
        date_2 = System.System().text_capture("Insert id 2: ", False)
        data = User_Income_repository.DB_dealing().tables_selector_by_date(date_1, date_2, "")
        System.System().print_tables_nicely(data)
        System.System().balance_sum(data)

    def see_balance(self):

        print("The current all user balance is : ")
        print("{:.2f}".format(User_Income_repository.DB_dealing().last_balance_retriever(
            User_Income_repository.DB_dealing().last_id_retriever("income")
        )))
        print("to check only your balance, select 'just yours' in the see_menu")

        #print(Data_base_tables.DB_dealing().last_id_retriever("income"))

    def see_trans_b_id_user(self, id):
        self.see_trans(id)
        date_1 = System.System().text_capture("Insert id 1: ", False)
        date_2 = System.System().text_capture("Insert id 2: ", False)
        data = User_Income_repository.DB_dealing().tables_selector_by_date(date_1, date_2, id)

        print("|{:^10}||{:^20}||{:^10}||{:^10}||{:^10}||{:^10}||{:^10}||{:^10}|".format("id", "Date",
                                                                                        "Income", "Expense",
                                                                                        "t_balance", "balance",
                                                                                        "description", "user_name"))
        System.System().print_tables_nicely(data)
        System.System().balance_sum(data)

    def see_by_description(self, id):
        desc = System.System().text_capture("Insert the description you want to search: ", False)
        table = User_Income_repository.DB_dealing().select_data_by_desc("", desc)
        System.System().print_tables_nicely(table)


    def update_desc(self):
        self.see_trans("")
        valid = False
        while not valid:
            id = System.System().text_capture(
                "Which id of the table above you want to change the description from: ",
            False
            )
            line = User_Income_repository.DB_dealing().select_table_line(id)
            if line != []:
                break
            else:
                print("ID does not exists, try again: ")
        print("the description of this line is {} ".format(line[0][-2]))
        new_desc = System.System().text_capture("Insert new description: ", False)

        User_Income_repository.DB_dealing().updater(new_desc, id, "income", "description")
        print("Description successfully updated")

