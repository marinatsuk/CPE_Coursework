import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import *

import pandas as pd


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        main_label = tk.Label(
            self, text="Main page", bg='#D9D9D9', fg="#232323", font=("Calibri", 24))
        database_page = tk.Button(
            self, text="Database", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(DatabasePage))
        add_video = tk.Button(
            self, text="Watch video", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(Videos))
        analyse = tk.Button(
            self, text="Start analysing", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(PreAnalysisPage))
        exit_button = tk.Button(self, text="Exit", command=self.quit)

        # Placing widgets on the screen
        main_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
        database_page.grid(row=2, column=0)
        add_video.grid(row=2, column=1, pady=10)
        analyse.grid(row=4, column=0)
        exit_button.grid(row=4, column=1, pady=10)

class DatabasePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
        cursor = conn.cursor()
        options = ["Add new record", "Delete record", "Edit record", "Show all results"]

        def action(choice):
            chosen = clicked.get()
            if chosen == options[0]:  # Add new record
                def submit():
                    if len(name_entry.get()) == 0 or len(address_entry.get()) == 0:
                        messagebox.showerror("showerror", "Please fill entry boxes")
                        name_entry.delete(0, END)
                        address_entry.delete(0, END)
                    else:
                        conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
                        c = conn.cursor()
                        c.execute("INSERT INTO videos (name, address) VALUES (:name, :address)",
                                  {
                                      'name': name_entry.get(),
                                      'address': name_entry.get(),
                                  })
                        conn.commit()
                        conn.close()
                        name_entry.delete(0, END)
                        address_entry.delete(0, END)
                        messagebox.showinfo('showinfo', 'Record successfully added')

                def clear():
                    name_label.destroy()
                    address_label.destroy()
                    name_entry.destroy()
                    address_entry.destroy()
                    submit_btn.destroy()
                    clear_btn.destroy()
                    clicked.set("Select an Option")

                name_label = Label(self, text="Name")
                name_label.grid(row=1, column=0, pady=(10, 0))
                address_label = Label(self, text="Address")
                address_label.grid(row=2, column=0)
                name_entry = Entry(self, width=30)
                name_entry.grid(row=1, column=1, padx=20, pady=(10, 0))
                address_entry = Entry(self, width=30)
                address_entry.grid(row=2, column=1)
                submit_btn = Button(self, text="Add Record To Database", command=submit)
                submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
                clear_btn = Button(self, text="Clear window", command=clear)
                clear_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

            elif chosen == options[1]:  # Delete
                conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
                cursor = conn.cursor()
                df = pd.read_sql_query("SELECT id from videos", conn)
                id_list = df['id'].values.tolist()
                def delete():
                    if len(id_entry.get()) == 0:
                        messagebox.showerror("showerror", "Please fill entry box")
                        id_entry.delete(0, END)
                    elif id_entry.get().isnumeric() == False:
                        messagebox.showerror("showerror", "ID should be numeric")
                        id_entry.delete(0, END)
                    else:
                        if id_entry in id_list:
                            conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
                            cursor = conn.cursor()
                            cursor.execute("DELETE from videos WHERE oid = " + id_entry.get())
                            id_entry.delete(0, END)
                            conn.commit()
                            conn.close()
                            messagebox.showinfo('showinfo', 'Record successfully deleted')
                        else:
                            messagebox.showerror('showerror', "Record with this ID was not found. Try again")
                            id_entry.delete(0, END)


                def clear():
                    id_label.destroy()
                    id_entry.destroy()
                    delete_btn.destroy()
                    clear_btn.destroy()
                    clicked.set("Select an Option")

                id_label = Label(self, text="Select ID")
                id_label.grid(row=2, column=0, pady=5)
                id_entry = Entry(self, width=30)
                id_entry.grid(row=2, column=1, pady=5)
                delete_btn = Button(self, text="Delete Record", command=delete)
                delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
                clear_btn = Button(self, text="Clear window", command=clear)
                clear_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

            elif chosen == options[2]:
                conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
                cursor = conn.cursor()
                df = pd.read_sql_query("SELECT id from videos", conn)
                id_list = df['id'].values.tolist()
                def edit():
                    if len(name_entry.get()) == 0 or len(address_entry.get()) == 0 or len(id_entry.get()) == 0:
                        messagebox.showerror("showerror", "Please fill entry boxes")
                        name_entry.delete(0, END)
                        address_entry.delete(0, END)
                        id_entry.delete(0, END)
                    elif id_entry.get().isnumeric() == False:
                        messagebox.showerror("showerror", "ID should be numeric")
                        name_entry.delete(0, END)
                        address_entry.delete(0, END)
                        id_entry.delete(0, END)
                    else:
                        record_id = int(id_entry.get())
                        if record_id in id_list:
                            cursor.execute("""UPDATE videos SET name = :name, address = :address
                                    WHERE oid = :oid""",
                                      {
                                          'name': name_entry.get(),
                                          'address': address_entry.get(),
                                          'oid': record_id
                                      })
                            name_entry.delete(0, END)
                            address_entry.delete(0, END)
                            id_entry.delete(0, END)
                            conn.commit()
                            conn.close()
                            messagebox.showinfo('showinfo', 'Record successfully edited')
                        else:
                            messagebox.showerror('showerror', "Record with this ID was not found. Try again")
                            name_entry.delete(0, END)
                            address_entry.delete(0, END)
                            id_entry.delete(0, END)

                def clear():
                    id_label.destroy()
                    id_entry.destroy()
                    name_label.destroy()
                    address_label.destroy()
                    name_entry.destroy()
                    address_entry.destroy()
                    edit_btn.destroy()
                    clear_btn.destroy()
                    clicked.set("Select an Option")

                name_label = Label(self, text="Name")
                name_label.grid(row=1, column=0, pady=(10, 0))
                name_entry = Entry(self, width=30)
                name_entry.grid(row=1, column=1, padx=20, pady=(10, 0))
                address_label = Label(self, text="Address")
                address_label.grid(row=2, column=0)
                address_entry = Entry(self, width=30)
                address_entry.grid(row=2, column=1)
                id_label = Label(self, text="Select ID")
                id_label.grid(row=3, column=0, pady=5)
                id_entry = Entry(self, width=30)
                id_entry.grid(row=3, column=1, pady=5)
                edit_btn = Button(self, text="Edit Record", command=edit)
                edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
                clear_btn = Button(self, text="Clear window", command=clear)
                clear_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

            else:
                def query():
                    conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
                    cursor = conn.cursor()
                    cursor.execute("SELECT id, name FROM videos LIMIT 0, 10")

                    i=3
                    records = cursor.fetchall()
                    for record in records:
                        for j in range(len(record)):
                            mystr = StringVar()
                            mystr.set(record[j])
                            entry = tk.Entry(self, textvariable=mystr, state=DISABLED)
                            entry.grid(row=i, column=j)
                        i = i+1
                    conn.commit()
                    conn.close()
                query()

        clicked = StringVar()
        clicked.set("Select an Option")
        drop = OptionMenu(self, clicked, *options, command=action)
        drop.grid(row=0, column=0)

        conn.commit()
        conn.close()




# class Videos(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#
#         def delete():
#             conn = sqlite3.connect('video_db.db')
#             cursor = conn.cursor()
#             cursor.execute("DELETE from videos WHERE oid = " + delete_box.get())
#             delete_box.delete(0, END)
#             conn.commit()
#             conn.close()
#
#         # Create Submit Function For database
#         def submit():
#             conn = sqlite3.connect('video_db.db')
#             c = conn.cursor()
#             c.execute("INSERT INTO videos (name, address) VALUES (:name, :address)",
#                       {
#                           'f_name': name.get(),
#                           'address': address.get(),
#                       })
#             conn.commit()
#             conn.close()
#             name.delete(0, END)
#             address.delete(0, END)
#
#         # Create Query Function
#         def query():
#             conn = sqlite3.connect('video_db.db')
#             cursor = conn.cursor()
#             cursor.execute("SELECT id, name, oid FROM video_db.db")
#             records = cursor.fetchall()
#             print_records = ''
#             for record in records:
#                 print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"
#
#             query_label = Label(self, text=print_records)
#             query_label.grid(row=12, column=0, columnspan=2)
#             conn.commit()
#             conn.close()
#
#         name = Entry(self, width=30)
#         name.grid(row=0, column=1, padx=20, pady=(10, 0))
#         address = Entry(self, width=30)
#         address.grid(row=1, column=1)
#         delete_box = Entry(self, width=30)
#         delete_box.grid(row=2, column=1, pady=5)
#
#         # Create Text Box Labels
#         name_label = Label(self, text="Name")
#         name_label.grid(row=0, column=0, pady=(10, 0))
#         address_label = Label(self, text="Address")
#         address_label.grid(row=1, column=0)
#         delete_box_label = Label(self, text="Select ID")
#         delete_box_label.grid(row=2, column=0, pady=5)
#
#         submit_btn = Button(self, text="Add Record To Database", command=submit)
#         submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
#
#         query_btn = Button(self, text="Show Records", command=query)
#         query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
#
#         delete_btn = Button(self, text="Delete Record", command=delete)
#         delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
#
#         # edit_btn = Button(self, text="Edit Record", command=edit)
#         # edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
#
#
#
#
# # class All_Videos(tk.Frame):
# #     def __init__(self, parent, controller):
# #         tk.Frame.__init__(self, parent)
# #
# #         def delete():
# #             conn = sqlite3.connect('video_db.db')
# #             cursor = conn.cursor()
# #             cursor.execute("DELETE from videos WHERE oid = " + delete_box.get())
# #             delete_box.delete(0, END)
# #             conn.commit()
# #             conn.close()
# #
# #         # Create Submit Function For database
# #         def submit():
# #             conn = sqlite3.connect('video_db.db')
# #             c = conn.cursor()
# #             c.execute("INSERT INTO videos (name, address) VALUES (:name, :address)",
# #                       {
# #                           'f_name': name.get(),
# #                           'address': address.get(),
# #                       })
# #             conn.commit()
# #             conn.close()
# #             name.delete(0, END)
# #             address.delete(0, END)
# #
# #         # Create Query Function
# #         def query():
# #             conn = sqlite3.connect('video_db.db')
# #             cursor = conn.cursor()
# #             cursor.execute("SELECT id, name, oid FROM video_db.db")
# #             records = cursor.fetchall()
# #             print_records = ''
# #             for record in records:
# #                 print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"
# #
# #             query_label = Label(self, text=print_records)
# #             query_label.grid(row=12, column=0, columnspan=2)
# #             conn.commit()
# #             conn.close()
# #
# #         all_videos()
# #         main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
# #         show_button = tk.Button(self, text="Show all videos", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=delete)
# #         delete_button = tk.Button(self, text="Delete", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=delete)
# #         delete_label = tk.Label(self, text="Enter ID", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
# #         delete_entry = tk.Entry(self, font=("Calibri", 16))
# #         quit_button = tk.Button(self, text="Exit", command=self.quit)
# #         main_button.grid(row=1, column=0)
# #         delete_label.grid(row=2, column=0)
# #         delete_entry.grid(row=3, column=0)
# #         delete_button.grid(row=4, column=0)
# #         quit_button.grid(row=5, column=0)
#
# class All_Videos(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         def delete():
#             conn = sqlite3.connect('video_db.db')
#             cursor = conn.cursor()
#             cursor.execute('DELETE FROM videos WHERE oid=' + delete_entry.get())
#             all_videos()
#             conn.commit()
#             conn.close()
#
#         def all_videos():
#             conn = sqlite3.connect('video_db.db')
#             cursor = conn.cursor()
#             cursor.execute('SELECT * FROM videos')
#             i=3
#             records = cursor.fetchall()
#             for record in records:
#                 for j in range(len(record)):
#                     mystr = StringVar()
#                     mystr.set(record[j])
#                     e = tk.Entry(self, textvariable=mystr, state=DISABLED)
#                     e.grid(row=i, column=j)
#                 i = i+1
#
#             conn.commit()
#             conn.close()
#
#         all_videos()
#         main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
#         show_button = tk.Button(self, text="Show all videos", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=delete)
#         delete_button = tk.Button(self, text="Delete", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=delete)
#         delete_label = tk.Label(self, text="Enter ID", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
#         delete_entry = tk.Entry(self, font=("Calibri", 16))
#         quit_button = tk.Button(self, text="Exit", command=self.quit)
#         main_button.grid(row=1, column=0)
#         delete_label.grid(row=2, column=0)
#         delete_entry.grid(row=3, column=0)
#         delete_button.grid(row=4, column=0)
#         quit_button.grid(row=5, column=0)
#
# class Add_Video(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         def submit():
#             conn = sqlite3.connect('video_db.db')
#             cursor = conn.cursor()
#             cursor.execute('INSERT INTO videos (name, address) VALUES (:name_entry, :video_entry)',
#                            {
#                                'name_entry': name_entry.get(),
#                                'video_entry': video_entry.get()
#                            })
#             name_entry.delete(0, 'end')
#             video_entry.delete(0, 'end')
#             conn.commit()
#             conn.close()
#         main_label = tk.Label(
#             self, text="Add new video", bg='#D9D9D9', fg="#232323", font=("Calibri", 24))
#         name_label = tk.Label(self, text="Enter name", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
#         name_entry = tk.Entry(self, font=("Calibri", 16))
#         video_label = tk.Label(self, text="Enter root to video", bg='#D9D9D9', fg="#232323", font=("Calibri", 16))
#         video_entry = tk.Entry(self, font=("Calibri", 16))
#         main_button = tk.Button(self, text="Main page", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=lambda: controller.show_frame(MainPage))
#         all_vid_button = tk.Button(self, text="All videos", bg="#232323", fg="#FFFFFF", font=("Calibri", 16),
#                                     command=lambda: controller.show_frame(All_Videos))
#         submit_button = tk.Button(self, text="Submit", bg="#232323", fg="#FFFFFF", font=("Calibri", 16), command=submit)
#         quit_button = tk.Button(self, text="Exit", command=self.quit)
#         main_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)
#         name_label.grid(row=1, column=0)
#         name_entry.grid(row=1, column=1, pady=10)
#         video_label.grid(row=2, column=0)
#         video_entry.grid(row=2, column=1, pady=10)
#         all_vid_button.grid(row=3, column=0)
#         main_button.grid(row=4, column=0)
#         submit_button.grid(row=4, column=1)
#         quit_button.grid(row=4, column=2)

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

        window = tk.Frame(self, bg='#D9D9D9', width=600, height=400)
        window.pack()

        self.frames = {}
        for F in (MainPage, DatabasePage, PreAnalysisPage, AnalysisPage, ResultsPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.minsize(600, 400)
app.mainloop()
