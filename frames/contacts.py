import customtkinter
from PIL import Image
from tkinter import messagebox
from database import Database


class ContactsFrame(customtkinter.CTkFrame):
    def __init__(self, master, show_contacts_frame, show_edit_contact_frame, user_data=None):
        super().__init__(master)
        self.database = Database("phonebook.db")
        self.show_contacts_frame = show_contacts_frame
        self.show_edit_contact_frame = show_edit_contact_frame
        self.contacts_list = []
        self.user_data = user_data
        self.fetch_data()

        print(user_data)
        # heading
        self.heading = customtkinter.CTkLabel(self, text="All Contacts", font=(
            'Sen', 36, 'bold'), fg_color="transparent")
        self.heading.pack(pady=20)

        for contact in self.contacts_list:
            self.contact_record_frame = customtkinter.CTkFrame(
                self, height=80)
            self.contact_record_frame.pack(
                expand=False, fill="x", padx=15, pady=10)

            self.contact_avatar = customtkinter.CTkImage(light_image=Image.open(
                "./images/user.png"), dark_image=Image.open("./images/user.png"), size=(30, 30,))
            self.contact_list_name = customtkinter.CTkLabel(self.contact_record_frame, text=f"{contact[2]} {contact[3]}", font=(
                'Sen', 18), compound="left", image=self.contact_avatar).pack(
                anchor="w", side="left", padx=15, pady=8)

            self.contact_list_phone = customtkinter.CTkLabel(
                self.contact_record_frame, text=contact[4], font=('Sen', 18)).pack(
                pady=8, side="left", fill="x", expand=True)

            edit_button = customtkinter.CTkButton(self.contact_record_frame, text="Edit", height=32, font=(
                'Poppins', 18), corner_radius=12, command=lambda contact_id=contact[0]: self.switch_frame(contact_id))
            edit_button.pack(pady=20, padx=10, anchor="w",
                             side="left", fill="x")

            delete_button = customtkinter.CTkButton(self.contact_record_frame, text="Delete", height=32, font=(
                'Poppins', 18), corner_radius=12)
            delete_button.pack(pady=20, anchor="w",  side="left", fill="x")
            delete_button.configure(command=lambda contact_id=contact[0]: self.delete_contact(
                contact_id))  # Passing the contact ID as an argument

    def delete_contact(self, contact_id):
        # Show a confirmation dialog before actually deleting the contact
        confirmation = messagebox.askyesno(
            "Delete Contact", "Are you sure you want to delete this contact?")
        if confirmation:
            # Perform the actual delete operation from the database
            self.database.delete_data('contacts', f"id={contact_id}")
            # Re-fetch the data after deletion to update the view
            self.fetch_data()
            self.show_contacts_frame(self.user_data)

    def fetch_data(self):
        contacts = self.database.fetch_data(
            "contacts", f"user_id = {self.user_data['id']}")
        self.contacts_list = contacts

    def switch_frame(self, contact_id):
        self.show_edit_contact_frame(self.show_contacts_frame, contact_id)
