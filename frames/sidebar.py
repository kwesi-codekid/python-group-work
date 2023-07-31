import customtkinter

# sidebar frame
class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master, show_add_new_frame):
        super().__init__(master)

        # create title label
        self.title_label = customtkinter.CTkLabel(self, text="Tasks Management", font=("Sen", 20, "bold"))
        self.title_label.pack(pady=10)

        # create add task button
        self.add_task_button = customtkinter.CTkButton(self, text="Add New Task", command=show_add_new_frame)
        self.add_task_button.pack(pady=10)

        # create view tasks button
        self.view_tasks_button = customtkinter.CTkButton(self, text="View Tasks")
        self.view_tasks_button.pack(pady=10)

        # create exit button
        self.exit_button = customtkinter.CTkButton(self, text="Exit")
        self.exit_button.pack(pady=10)

    # create functions for buttons