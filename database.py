import sqlite3
import bcrypt

# database class


class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        self.create_contacts_table()
        self.create_users_table()

    # create table
    def create_tasks_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            task_name TEXT,
                            task_description TEXT,
                            task_due_date TEXT,
                            task_status TEXT
                        )""")
        self.connection.commit()

    def create_users_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.connection.commit()

    def create_contacts_table(self):
        self. cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                user_id TEXT NOT NULL
            )
        """)
        self.connection.commit()

    # register user
    def register_user(self, email, first_name, last_name, password):
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())

        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        userExist = self.cursor.fetchone()

        if userExist:
            print("Email already taken!")
        else:
            self.cursor.execute("INSERT INTO users (email, first_name, last_name, password) VALUES (?, ?, ?, ?)",
                                (email, first_name, last_name, hashed_password))
            self.connection.commit()

    def login_user(self, email, password):
        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return self.cursor.fetchone()

    def insert_task(self, name, description, due_date, status):
        self.cursor.execute("INSERT INTO tasks (task_name, task_description, task_due_date, task_status) VALUES (?, ?, ?, ?)",
                            (name, description, due_date, status))
        self.connection.commit()

    def add_contact(self, first_name, last_name, email, phone, user_id):
        self.cursor.execute("SELECT * FROM contacts WHERE email = ?", (email,))
        userExist = self.cursor.fetchone()

        if userExist:
            print("Email already taken!")
        else:
            self.cursor.execute("INSERT INTO contacts (email, first_name, last_name, phone_number, user_id) VALUES (?, ?, ?, ?, ?)",
                                (email, first_name, last_name, phone, user_id))
            self.connection.commit()

    # fetch data
    def fetch_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        data = self.cursor.fetchall()
        return data

    def fetch_single_data(self, table_name, condition):
        self.cursor.execute(f"SELECT * FROM {table_name} WHERE {condition}")
        data = self.cursor.fetchone()
        return data

    # delete data
    def delete_data(self, table_name, condition):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.connection.commit()

    # update data
    def update_data(self, table_name, condition, new_value):
        self.cursor.execute(
            f"UPDATE {table_name} SET {condition} WHERE {new_value}")
        self.connection.commit()

    # close connection
    def close_connection(self):
        self.connection.close()
