import customtkinter

from database import Database

# add new task frame


class RegisterFrame(customtkinter.CTkFrame):
    def __init__(self, master, switch_to_login):
        super().__init__(master)
        self.database = Database("phonebook.db")
        self.switch_to_login = switch_to_login

        # heading
        self.heading = customtkinter.CTkLabel(self, text="Register Your Account", font=(
            'Sen', 36, 'bold'), fg_color="transparent")
        self.heading.pack(pady=20)

        # firstname
        self.firstNameLabel = customtkinter.CTkLabel(
            self, text="First Name", font=('Sen', 19), fg_color="transparent")
        self.firstNameLabel.pack(pady=2)
        self.firstNameEntry = customtkinter.CTkEntry(
            self, placeholder_text="First Name", width=300, height=40, )
        self.firstNameEntry.pack(pady=2,  padx=10)

        # lastname
        self.lastNameLabel = customtkinter.CTkLabel(
            self, text="Last Name", font=('Sen', 19), fg_color="transparent")
        self.lastNameLabel.pack(pady=2)
        self.lastNameEntry = customtkinter.CTkEntry(
            self, placeholder_text="Last Name", width=300, height=40, )
        self.lastNameEntry.pack(pady=2,  padx=10)

        # email
        self.emailLabel = customtkinter.CTkLabel(
            self, text="Email", font=('Sen', 19), fg_color="transparent")
        self.emailLabel.pack(pady=2)
        self.emailEntry = customtkinter.CTkEntry(
            self, placeholder_text="Email", width=300, height=40, )
        self.emailEntry.pack(pady=2,  padx=10)

        # password
        self.passwordLabel = customtkinter.CTkLabel(
            self, text="Password", font=('Sen', 19), fg_color="transparent")
        self.passwordLabel.pack(pady=2)
        self.passwordEntry = customtkinter.CTkEntry(
            self, placeholder_text="Password", width=300, height=40, )
        self.passwordEntry.pack(pady=2,  padx=10)

        customtkinter.CTkButton(
            self, text="Register User", height=32, font=(
                'Poppins', 18), corner_radius=12, command=self.register).pack(pady=19)

        customtkinter.CTkButton(
            self, text="Already have an Account? Login",  bg_color="transparent", hover=False, fg_color="transparent", command=self.switch_to_login).pack()

    def register(self):
        first_name = self.firstNameEntry.get()
        last_name = self.lastNameEntry.get()
        email = self.emailEntry.get()
        password = self.passwordEntry.get()

        self.database.register_user(email, first_name, last_name, password)
        self.switch_to_login()
