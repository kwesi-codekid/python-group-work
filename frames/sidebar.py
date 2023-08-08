import customtkinter

# sidebar frame


class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master, show_new_contact_frame, show_contacts_frame, user_data, navigate_logout):
        super().__init__(master)
        self.user_data = user_data
        # create title label
        self.title_label = customtkinter.CTkLabel(
            self, text="Phonebook", font=("Sen", 20, "bold"))
        self.title_label.pack(pady=10)

        print("from sidebar frame")
        print(user_data)
        print("from sidebar frame")
        # create view tasks button
        self.view_tasks_button = customtkinter.CTkButton(self, text="View Contacts", height=32, font=(
            'Poppins', 18), command=show_contacts_frame).pack(pady=10)

        # create add task button
        self.new_contact_button = customtkinter.CTkButton(
            self, text="New Contact", height=32, font=('Poppins', 18), command=lambda: show_new_contact_frame(self.user_data)).pack(pady=10)

        # create exit button
        self.exit_button = customtkinter.CTkButton(self, text="Logout", height=32, command=navigate_logout, font=(
            'Poppins', 18),).pack(pady=10)

    # create functions for buttons
