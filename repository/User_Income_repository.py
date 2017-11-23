import os
import sqlite3


class DB_dealing:

    def __init__(self):

        #print("CONNECTING TO DB...")

        db = 'DB/application.db'
        if not os.path.isfile("DB/application.db"):
            print("CREATING DB...")
            self.conn = sqlite3.connect(db)
            from controller import User_controller
            repo = User_controller.User_repository()
            print("CREATING TABLES...")
            self.tables_creating()
            print("DB AND TABLES CREATED SUCCESSFULLY")
            print("CREATING ADMIN USER...")
            repo.create_admin()
            print("ADMIN CREATED!")
        else:
            self.conn = sqlite3.connect(db)


    def tables_creating(self):
        print("CREATING TABLE USERS")
        c = self.conn.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER UNIQUE NOT NULL PRIMARY KEY,
            username VARCHAR(250) NOT NULL UNIQUE,
            name VARCHAR(250),
            last_name VARCHAR(250),
            password VARCHAR(250)
            )
        """)

        print("CREATING TABLE INCOME")

        c.execute("""
            CREATE TABLE IF NOT EXISTS income(
            id INT UNIQUE NOT NULL,
            date REAL,
            income REAL,
            expense REAL,
            bal_t REAL,
            balance REAL,
            description VARCHAR(250),
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        self.conn.commit()
        c.close()

    def tables_selection(self, tb, user_id):
        c = self.conn.cursor()
        if user_id != "":
            table = c.execute(
                """
                                SELECT
                	            i.id, i.date, i.income, i.expense, i.bal_t, i.description,
                	            u.name
                	            FROM users u
                	            JOIN income i ON i.user_id = u.id
                	            WHERE u.id = "{}"
                                """.format(user_id)).fetchall()
        else:
            if tb != "users":

                table = c.execute(
                    """
                    SELECT
                    i.id, i.date, i.income, i.expense, i.bal_t, i.balance, i.description,
                    u.name
                    FROM users u
                    JOIN income i ON i.user_id = u.id
                    """).fetchall()
            else:
                table = c.execute("SELECT * FROM '{}'".format(tb)).fetchall()

        c.close()
        return table

    def last_id_retriever(self, type):
        c = self.conn.cursor()
        value = c.execute("""
        SELECT MAX(id) FROM {}
        """.format(type)).fetchall()[0]
        for id in value:
            if id == None:
                return 1
            else:
                return id

    def insert_user(self, id, username, name, last_name, password):
        c = self.conn
        c.execute("""
        INSERT INTO users VALUES(?, ?, ?, ?, ?)
        """, (id, username, name, last_name, password))
        self.conn.commit()
        c.close()

    def updater(self, element, id, table, column_name):
        c = self.conn.cursor()
        c.execute("""
        UPDATE "{}"
        SET "{}" = "{}"
        WHERE id = "{}"
        """.format(table, column_name, element, id))
        self.conn.commit()
        c.close()

    def last_balance_retriever(self, id):
        c = self.conn.cursor()
        empt = c.execute("SELECT COUNT(*) from income").fetchall()[0][0]
        if empt != 0:
            value = c.execute("""
            SELECT balance FROM income
            WHERE id = "{}"
            """.format(id))
            for balance in value:
                return balance[0]
        else:
            return 0

    def select_data_by_desc(self, id, desc):
        c = self.conn.cursor()
        if id == "":
            table = c.execute("SELECT * FROM income WHERE description LIKE '%{}%'".format(desc)).fetchall()
        else:
            table = c.execute(
                "SELECT * FROM income WHERE description = '{}' AND user_id = '{}'".format(desc, id)).fetchall()
        c.close()
        return table

    def income_insert(self, id, date, income, expense, bal_t, balance, description, u_id):
        c = self.conn.cursor()
        c.execute("""
            INSERT INTO income
            VALUES(?,?,?,?,?,?,?,?)
        """,(id, date, income, expense, bal_t, balance, description, u_id))
        self.conn.commit()
        c.close()

    def data_selector(self, element):
        c = self.conn.cursor()
        data = c.execute("""
        SELECT * FROM users
        WHERE username = "{}"
        """.format(element))

        return data.fetchall()

    def tables_selector_by_date(self, date_a, date_b, user):
        c = self.conn.cursor()
        if user == "":

            table = c.execute("SELECT * FROM income WHERE date BETWEEN '{}' AND '{}'".format(
                date_a, date_b)).fetchall()


        else:
            table =  c.execute("SELECT * FROM income WHERE date BETWEEN '{}' AND '{}' AND user_id = {}".format(
                date_a, date_b, user)).fetchall()

        c.close()
        return table

    def select_table_line(self, id):
        c = self.conn.cursor()

        line = c.execute("SELECT * FROM income WHERE id = '{}'".format(id)).fetchall()

        c.close()
        return line





