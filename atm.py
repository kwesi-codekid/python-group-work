import sqlite3


class ATM:
    def __init__(self):
        self.conn = sqlite3.connect('atm_database.db')
        self.c = self.conn.cursor()

        # Create SQLite database if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS accounts
                         (account_number TEXT PRIMARY KEY,
                          pin TEXT,
                          balance REAL)''')
        self.conn.commit()

    def create_account(self, account_number, pin, initial_balance):
        try:
            self.c.execute("INSERT INTO accounts VALUES (?, ?, ?)",
                           (account_number, pin, initial_balance))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def login(self, account_number, pin):
        self.c.execute("SELECT * FROM accounts WHERE account_number = ? AND pin = ?",
                       (account_number, pin))
        account = self.c.fetchone()
        return account

    def check_balance(self, account_number):
        self.c.execute("SELECT balance FROM accounts WHERE account_number = ?",
                       (account_number,))
        balance = self.c.fetchone()
        if balance:
            return balance[0]
        else:
            return None

    def withdraw(self, account_number, amount):
        current_balance = self.check_balance(account_number)
        if current_balance is not None and current_balance >= amount:
            new_balance = current_balance - amount
            self.c.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                           (new_balance, account_number))
            self.conn.commit()
            return new_balance
        else:
            return None

    def deposit(self, account_number, amount):
        current_balance = self.check_balance(account_number)
        if current_balance is not None:
            new_balance = current_balance + amount
            self.c.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                           (new_balance, account_number))
            self.conn.commit()
            return new_balance
        else:
            return None

    def close(self):
        self.conn.close()

    def _del_(self):
        self.conn.close()
