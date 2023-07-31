import customtkinter
import sqlite3


# add new task frame
class AddTaskFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # create title label
        self.title_label = customtkinter.CTkLabel(self, text="Add New Task", font=("Sen", 20, "bold"))
        self.title_label.pack(pady=10)

        # create add task form widgets
        self.task_name_label = customtkinter.CTkLabel(self, text="Task Name")
        self.task_name_label.pack(pady=10)

        self.task_name_entry = customtkinter.CTkEntry(self)
        self.task_name_entry.pack(pady=10)

        self.task_description_label = customtkinter.CTkLabel(self, text="Task Description")
        self.task_description_label.pack(pady=10)

        self.task_description_entry = customtkinter.CTkEntry(self)
        self.task_description_entry.pack(pady=10)

        self.task_due_date_label = customtkinter.CTkLabel(self, text="Task Due Date")
        self.task_due_date_label.pack(pady=10)

        self.task_due_date_entry = customtkinter.CTkEntry(self)
        self.task_due_date_entry.pack(pady=10)

        self.task_status_label = customtkinter.CTkLabel(self, text="Task Status")
        self.task_status_label.pack(pady=10)

        self.task_status_entry = customtkinter.CTkEntry(self)
        self.task_status_entry.pack(pady=10)

        # create add task button
        self.add_task_button = customtkinter.CTkButton(self, text="Add Task")
        self.add_task_button.pack(pady=10)

        # create back button
        self.back_button = customtkinter.CTkButton(self, text="Back")
        self.back_button.pack(pady=10)

    # create functions for buttons
