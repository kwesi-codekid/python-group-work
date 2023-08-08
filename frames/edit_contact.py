import customtkinter

# database class
from database import Database


# add new task frame
class EditContactFrame(customtkinter.CTkFrame):
    def __init__(self, master, show_contacts_frame):
        super().__init__(master)
        self.database = Database("phonebook.db")
        self.show_contacts_frame = show_contacts_frame
        self.contact = {'id': "", 'first_name': "",
                        'last_name': "", 'email': "", 'phone': ""}
        self.contact_id = None
        # self.fetch_contact()

        # create title label
        self.title_label = customtkinter.CTkLabel(
            self, text="Edit Contact", font=("Sen", 36, "bold"))
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

        login_button = customtkinter.CTkButton(self, text="Update contact", height=32, font=(
            'Poppins', 18), corner_radius=12, command=self.update_contact)
        login_button.pack(pady=20, anchor="w")

    def update_contact(self):
        first_name = self.firstNameEntry.get()
        last_name = self.lastNameEntry.get()
        email = self.emailEntry.get()
        phone = self.phoneEntry.get()

        update_condition = f"id = {self.contact_id}"
        new_values = (
            f"email = '{email}', first_name = '{first_name}', last_name = '{last_name}', phone_number = '{phone}'"
        )

        self.database.update_data('contacts', update_condition, new_values)
        self.show_contacts_frame()



    def fetch_contact(self, contact_id):
        contact = self.database.fetch_single_data(
            'contacts', f"id={contact_id}")
        self.contact = {'id': contact[0], 'first_name': contact[1],
                        'last_name': contact[2], 'email': contact[3], 'phone': contact[4]}
        print(contact[1])
        # clear input fields
        self.firstNameEntry.delete(0, 'end')
        self.lastNameEntry.delete(0, 'end')
        self.emailEntry.delete(0, 'end')
        self.phoneEntry.delete(0, 'end')

        # append values to input fields 
        self.firstNameEntry.insert(0, contact[1])
        self.lastNameEntry.insert(0, contact[2])
        self.emailEntry.insert(0, contact[3])
        self.phoneEntry.insert(0, contact[4])

    def set_contact_id(self, contact_id):
        self.contact_id = contact_id
        self.fetch_contact(contact_id)
