import customtkinter

# database class
from database import Database


# add new task frame
class NewContactFrame(customtkinter.CTkFrame):
    def __init__(self, master, show_contacts_frame):
        super().__init__(master)
        self.database = Database("phonebook.db")
        self.show_contacts_frame = show_contacts_frame

        # create title label
        self.title_label = customtkinter.CTkLabel(
            self, text="Add Contact", font=("Sen", 36, "bold"))
        self.title_label.pack(pady=10)

        # create add task form widgets
        self.firstNameLabel = customtkinter.CTkLabel(self, text="First Name", font=(
            'Sen', 20), fg_color="transparent", compound="left")
        self.firstNameLabel.pack(anchor="w", padx=10)
        self.firstNameEntry = customtkinter.CTkEntry(
            self, placeholder_text="First Name", width=300, height=40, )
        self.firstNameEntry.pack(pady=10, anchor="w", padx=10)

        self.lastNameLabel = customtkinter.CTkLabel(self, text="Last Name", font=(
            'Sen', 20), fg_color="transparent", compound="left")
        self.lastNameLabel.pack(anchor="w", padx=10)
        self.lastNameEntry = customtkinter.CTkEntry(
            self, placeholder_text="Last Name", width=300, height=40, )
        self.lastNameEntry.pack(pady=10, anchor="w", padx=10)

        self.emailLabel = customtkinter.CTkLabel(self, text="Email", font=(
            'Sen', 20), fg_color="transparent", compound="left")
        self.emailLabel.pack(anchor="w", padx=10)
        self.emailEntry = customtkinter.CTkEntry(
            self, placeholder_text="Email", width=300, height=40, )
        self.emailEntry.pack(pady=10, anchor="w", padx=10)

        self.phoneLabel = customtkinter.CTkLabel(self, text="Phone Number", font=(
            'Sen', 20), fg_color="transparent", compound="left")
        self.phoneLabel.pack(anchor="w", padx=10)
        self.phoneEntry = customtkinter.CTkEntry(
            self, placeholder_text="phone", width=300, height=40, )
        self.phoneEntry.pack(pady=10, anchor="w", padx=10)

        login_button = customtkinter.CTkButton(self, text="Add contact", height=32, font=(
            'Poppins', 18), corner_radius=12, command=self.add_contact)
        login_button.pack(pady=20, anchor="w")

    def add_contact(self):
        first_name = self.firstNameEntry.get()
        last_name = self.lastNameEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()

        self.database.add_contact(first_name, last_name, email, phone)
        self.show_contacts_frame()
