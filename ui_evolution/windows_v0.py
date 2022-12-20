import tkinter as tk
from tkinter import messagebox

class AuthPage(tk.Frame):
    def __init__(self, parent, controller):
        def login():
            username = "admin"
            password = "12345"
            if username_entry.get() == username and password_entry.get() == password:
                messagebox.showinfo(title="Login Success", message="You successfully logged in.")
                controller.show_frame(MainPage)
            else:
                messagebox.showerror(title="Error", message="Invalid login.")

        tk.Frame.__init__(self, parent)
        login_label = tk.Label(self, text="Login", bg='#D9D9D9', fg="#232323", font=("Calibri", 24))
        username_label = tk.Label(
            self, text="Username", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        username_entry = tk.Entry(self, font=("Calibri", 16))
        password_entry = tk.Entry(self, show="*", font=("Calibri", 16))
        password_label = tk.Label(
            self, text="Password", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        login_button = tk.Button(
            self, text="Login", bg="#232323", fg="#FFFFFF", font=("Calibri", 24), command=login)

        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1, pady=10)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1, pady=10)
        login_button.grid(row=3, column=0, columnspan=2, pady=20)

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_label = tk.Label(
            self, text="Main page", bg='#D9D9D9', fg="#232323", font=("Calibri", 24))
        all_characters = tk.Button(
            self, text="All Characters", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(All_Characters))
        add_characters = tk.Button(
            self, text="Add new character", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(Add_Character))
        all_videos = tk.Button(
            self, text="Videos", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(All_Videos))
        add_video = tk.Button(
            self, text="Add new video", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(Add_Video))
        analyse = tk.Button(
            self, text="Start analysing", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(PreAnalysisPage))
        exit_button = tk.Button(self, text="Exit", command=self.quit)

        # Placing widgets on the screen
        main_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
        all_characters.grid(row=1, column=0)
        add_characters.grid(row=1, column=1, pady=10)
        all_videos.grid(row=2, column=0)
        add_video.grid(row=2, column=1, pady=10)
        analyse.grid(row=3, column=0)
        exit_button.grid(row=3, column=1, pady=10)

class All_Characters(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_label = tk.Label(
            self, text="Тут будет табличка с кнопочками", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
        quit_button = tk.Button(self, text="Exit", command=self.quit)
        main_label.grid(row=0, column=0)
        main_button.grid(row=1, column=0)
        quit_button.grid(row=2, column=0)

class Add_Character(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_label = tk.Label(
            self, text="Add new character", bg='#D9D9D9', fg="#232323", font=("Calibri", 24))
        name_label = tk.Label(self, text="Enter name", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        name_entry = tk.Entry(self, font=("Calibri", 16))
        surname_label = tk.Label(self, text="Enter surname", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        surname_entry = tk.Entry(self, font=("Calibri", 16))
        main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
        all_char_button = tk.Button(self, text="All characters", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(All_Characters))
        submit_button = tk.Button(self, text="Submit", bg="#232323", fg="#FFFFFF", font=("Calibri", 16))
        quit_button = tk.Button(self, text="Exit", command=self.quit)
        main_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
        name_label.grid(row=1, column=0)
        name_entry.grid(row=1, column=1, pady=10)
        surname_label.grid(row=2, column=0)
        surname_entry.grid(row=2, column=1, pady=10)
        all_char_button.grid(row=3, column=0)
        main_button.grid(row=4, column=0)
        submit_button.grid(row=4, column=1)
        quit_button.grid(row=4, column=2)

class All_Videos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_label = tk.Label(
            self, text="Тут будет табличка с кнопочками", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
        quit_button = tk.Button(self, text="Exit", command=self.quit)
        main_label.grid(row=0, column=0)
        main_button.grid(row=1, column=0)
        quit_button.grid(row=2, column=0)

class Add_Video(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_label = tk.Label(
            self, text="Add new video", bg='#D9D9D9', fg="#232323", font=("Calibri", 24))
        name_label = tk.Label(self, text="Enter name", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        name_entry = tk.Entry(self, font=("Calibri", 16))
        video_label = tk.Label(self, text="Here will be a video entry form", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        video_entry = tk.Entry(self, font=("Calibri", 16))
        main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
        all_vid_button = tk.Button(self, text="All videos", bg="#232323", fg="#FFFFFF", font=("Calibri", 16),
                                    command=lambda: controller.show_frame(All_Videos))
        submit_button = tk.Button(self, text="Submit", bg="#232323", fg="#FFFFFF", font=("Calibri", 16))
        quit_button = tk.Button(self, text="Exit", command=self.quit)
        main_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
        name_label.grid(row=1, column=0)
        name_entry.grid(row=1, column=1, pady=10)
        video_label.grid(row=2, column=0)
        video_entry.grid(row=2, column=1, pady=10)
        all_vid_button.grid(row=3, column=0)
        main_button.grid(row=4, column=0)
        submit_button.grid(row=4, column=1)
        quit_button.grid(row=4, column=2)

class PreAnalysisPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_label = tk.Label(
            self, text="Choose a video", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
        submit_button = tk.Button(self, text="Continue", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(AnalysisPage))
        quit_button = tk.Button(self, text="Exit", command=self.quit)
        main_label.grid(row=0, column=0)
        main_button.grid(row=1, column=0)
        quit_button.grid(row=2, column=0)
        submit_button.grid(row=3, column=0)

class AnalysisPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_label = tk.Label(
            self, text="Тут будет анализ", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
        submit_button = tk.Button(self, text="Continue", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(ResultsPage))
        quit_button = tk.Button(self, text="Exit", command=self.quit)
        main_label.grid(row=0, column=0)
        main_button.grid(row=1, column=0)
        quit_button.grid(row=2, column=0)
        submit_button.grid(row=3, column=0)

class ResultsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_label = tk.Label(
            self, text="Тут будут результаты", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
        main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
        submit_button = tk.Button(self, text="Another test", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(PreAnalysisPage))
        quit_button = tk.Button(self, text="Exit", command=self.quit)
        main_label.grid(row=0, column=0)
        main_button.grid(row=1, column=0)
        quit_button.grid(row=2, column=0)
        submit_button.grid(row=3, column=0)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self, bg='#D9D9D9')
        window.pack()

        self.frames = {}
        for F in (AuthPage, MainPage, All_Characters, Add_Character, All_Videos, Add_Video, PreAnalysisPage, AnalysisPage, ResultsPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AuthPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(800, 500)
app.mainloop()
