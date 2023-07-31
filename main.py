import customtkinter 

#  import frames
from frames.sidebar import SidebarFrame
from frames.add_task import AddTaskFrame

# main class
class Main:
    def __init__(self):
        super().__init__()
        self.root = customtkinter.CTk()
        self.root.geometry("1000x600")
        self.root.title("Tasks Management")
        self.root._set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        # create sidebar frame
        self.sidebar = SidebarFrame(self.root, self.show_add_new_frame)
        self.sidebar.pack(side="left", fill="y")

        # frame instances
        self.add_task_frame = AddTaskFrame(self.root)


        # create content frame
        self.content = customtkinter.CTkFrame(self.root)
        self.content.pack(side="right", fill="both", expand=True)

        self.root.mainloop()

    def show_add_new_frame(self):
        self.add_task_frame.pack(fill="both", expand=True)




# run main class
if __name__ == '__main__':
    Main()