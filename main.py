import customtkinter

#  import frames
from frames.sidebar import SidebarFrame
from frames.new_contact import NewContactFrame
from frames.edit_contact import EditContactFrame
from frames.contacts import ContactsFrame
from frames.register import RegisterFrame
from frames.login import LoginFrame
# main class


class Main:
    def __init__(self):
        super().__init__()
        self.root = customtkinter.CTk()
        self.root.geometry("1000x600")
        self.root.title("Phonebook")
        self.root._set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")

        self.sidebar = SidebarFrame(
            self.root, self.show_new_contact_frame, self.show_contacts_frame, self.logout, user_data=None)

        self.new_contact_frame = NewContactFrame(
            self.root, self.show_contacts_frame, user_data=None)

        self.register_frame = RegisterFrame(self.root, self.switch_to_login)
        self.register_frame.pack(fill="both", expand=True)

        # frame instances
        self.login_frame = LoginFrame(
            self.root, self.switch_to_register, self.show_contacts_frame)
        self.edit_contact_frame = EditContactFrame(
            self.root, self.show_contacts_frame)
        self.contacts_frame = ContactsFrame(
            self.root, self.show_contacts_frame, self.show_edit_contact_frame)

        self.root.mainloop()

    def show_new_contact_frame(self, user_data):
        self.contacts_frame.pack_forget()
        self.edit_contact_frame.pack_forget()
        self.new_contact_frame = NewContactFrame(
            self.root, self.show_contacts_frame, user_data)
        self.new_contact_frame.pack(fill="both", expand=True)

    def show_edit_contact_frame(self, show_contacts_frame,  contact_id):
        self.contacts_frame.pack_forget()
        self.edit_contact_frame.set_contact_id(contact_id)
        self.edit_contact_frame.pack(fill="both", expand=True)

    def show_contacts_frame(self, user_data):
        self.sidebar.pack_forget()
        self.new_contact_frame.pack_forget()
        self.contacts_frame.pack_forget()
        self.edit_contact_frame.pack_forget()
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()

        self.sidebar = SidebarFrame(
            self.root, self.show_new_contact_frame, self.show_contacts_frame, self.logout, user_data)
        self.sidebar.pack(fill="y", side="left")

        self.contacts_frame = ContactsFrame(
            self.root, self.show_contacts_frame, self.show_edit_contact_frame, user_data)
        self.contacts_frame.pack(fill="both", expand=True)

    def switch_to_login(self):
        self.register_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    def switch_to_register(self):
        self.login_frame.pack_forget()
        self.register_frame.pack(fill="both", expand=True)

    def logout(self):
        self.contacts_frame.pack_forget()
        self.edit_contact_frame.pack_forget()
        self.new_contact_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)
        self.sidebar.pack_forget()


# run main class
if __name__ == '__main__':
    Main()
