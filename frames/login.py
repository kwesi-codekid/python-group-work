import customtkinter
import bcrypt

from database import Database


# add new task frame
class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, switch_to_register, show_contacts_frame):
        super().__init__(master)
        self.database = Database("phonebook.db")
        self.switch_to_register = switch_to_register
        self.show_contacts_frame = show_contacts_frame

        # heading
        self.heading = customtkinter.CTkLabel(self, text="Login to Your Account", font=(
            'Sen', 36, 'bold'), fg_color="transparent")
        self.heading.pack(pady=20)

        # email
        self.emailLabel = customtkinter.CTkLabel(
            self, text="Email", font=('Sen', 19), fg_color="transparent")
        self.emailLabel.pack(padx=10)
        self.emailEntry = customtkinter.CTkEntry(
            self, placeholder_text="Email", width=300, height=40, )
        self.emailEntry.pack(pady=10,  padx=10)

        self.passwordLabel = customtkinter.CTkLabel(self, text="Password",  font=(
            'Sen', 19), fg_color="transparent")
        self.passwordLabel.pack(padx=10)
        self.passwordEntry = customtkinter.CTkEntry(
            self, placeholder_text="Password", width=300, height=40, )
        self.passwordEntry.pack(pady=2,  padx=10)

        customtkinter.CTkButton(self, text="Login", height=32, font=(
            'Poppins', 18), corner_radius=12, command=self.login).pack(pady=19)

        customtkinter.CTkButton(
            self, text="Don't have an Account? Register", bg_color="transparent", hover=False, fg_color="transparent", command=self.switch_to_register).pack()

    def login(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()

        user = self.database.login_user(email, password)

        if user is None:
            # User not found
            print("Invalid username or password.")
        else:
            print(user)
            user_data = {'id': user[0], 'email': user[1],
                         'first_name': user[2], 'last_name': user[3], 'password': user[4]}
            # Verify a password
            if bcrypt.checkpw(password.encode('utf-8'), user_data["password"]):
                print("Password matches!")
                self.show_contacts_frame()
            else:
                print("Invalid username or password.")
