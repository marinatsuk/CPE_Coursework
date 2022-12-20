from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pandas as pd
import cv2

root = Tk()
root.title('Database manager')
root.geometry("1000x550")

def query_database():
    for record in my_tree.get_children():
        my_tree.delete(record)

    conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
    c = conn.cursor()
    c.execute("SELECT * FROM videos")
    records = c.fetchall()
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2]),
                           tags=('oddrow',))
        count += 1

    conn.commit()
    conn.close()

def search_records():
    lookup_record = search_entry.get()
    search.destroy()
    for record in my_tree.get_children():
        my_tree.delete(record)
    conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
    c = conn.cursor()
    c.execute("SELECT * FROM videos WHERE name like ?", (lookup_record,))
    records = c.fetchall()

    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2]),
                           tags=('oddrow',))
        count += 1

    conn.commit()
    conn.close()

def lookup_records():
    global search_entry, search

    search = Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")

    search_frame = LabelFrame(search, text="Name")
    search_frame.pack(padx=10, pady=10)

    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(pady=20, padx=20)

    search_button = Button(search, text="Search Records", command=search_records)
    search_button.pack(padx=20, pady=20)

def remove_one():
    try:
        x = my_tree.selection()[0]
        my_tree.delete(x)
        conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
        cursor = conn.cursor()
        cursor.execute("DELETE from videos WHERE oid = " + id_entry.get())
        id_entry.delete(0, END)
        conn.commit()
        conn.close()
        deselect()
        messagebox.showinfo('showinfo', 'Record successfully deleted')
    except sqlite3.DatabaseError:
        deselect()
        messagebox.showerror('showerror', 'DatabaseError')

def remove_many():
    response = messagebox.askyesno('Confirm', 'Do you want to delete these records?')
    if response == 1:
        try:
            x = my_tree.selection()
            ids_to_delete = []
            for record in x:
                ids_to_delete.append(my_tree.item(record, 'values')[2])
            for record in x:
                my_tree.delete(record)

            conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
            cursor = conn.cursor()
            cursor.executemany("DELETE from videos WHERE id = ?", [(a,) for a in ids_to_delete])
            id_entry.delete(0, END)
            conn.commit()
            conn.close()
            deselect()
            messagebox.showinfo('showinfo', 'Records successfully deleted')
        except sqlite3.DatabaseError:
            deselect()
            messagebox.showerror('showerror', 'DatabaseError')

def play_video():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(
        id_entry.get(), name_entry.get(), address_entry.get()))

    conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
    cursor = conn.cursor()

    cap = cv2.VideoCapture(address_entry.get())
    if (cap.isOpened() == False):
        print("Error opening video file")

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()

def select_record(e):
    try:
        id_entry.configure(state='normal')
        name_entry.delete(0, END)
        id_entry.delete(0, END)
        address_entry.delete(0, END)

        selected = my_tree.focus()
        values = my_tree.item(selected, 'values')

        id_entry.insert(0, values[0])
        name_entry.insert(0, values[1])
        address_entry.insert(0, values[2])
        id_entry.configure(state='readonly')
    except sqlite3.DatabaseError:
        deselect()
        messagebox.showerror('showerror', 'DatabaseError')

def update_record():
    id_entry.configure(state='normal')
    selected = my_tree.focus()
    print(selected)
    if len(name_entry.get()) == 0 or len(address_entry.get()) == 0:
        deselect()
        messagebox.showerror("showerror", "Please fill entry boxes")
    else:
        my_tree.item(selected, text="", values=(
            id_entry.get(), name_entry.get(), address_entry.get()))
        try:
            conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
            cursor = conn.cursor()

            cursor.execute("""UPDATE videos SET name = :name, address = :address
                                    WHERE oid = :oid""",
                           {
                               'name': name_entry.get(),
                               'address': address_entry.get(),
                               'oid': id_entry.get()
                           })
            conn.commit()
            conn.close()
            deselect()
            messagebox.showinfo('showinfo', 'Record was edited')
        except sqlite3.DatabaseError:
            deselect()
            messagebox.showerror('showerror', 'DatabaseError')

def add_record():
    if len(name_entry.get()) == 0 or len(address_entry.get()) == 0:
        messagebox.showerror("showerror", "Please fill entry boxes")
        name_entry.delete(0, END)
        address_entry.delete(0, END)
    else:
        try:
            conn = sqlite3.connect('C:\\Users\\serg\\PycharmProjects\\CPE_Coursework_Tsukanova\\video_db.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO videos (name, address) VALUES (:name, :address)",
                      {
                          'name': name_entry.get(),
                          'address': name_entry.get(),
                      })
            conn.commit()
            conn.close()
            deselect()
            messagebox.showinfo('showinfo', 'Record successfully added')
            query_database()
        except sqlite3.DatabaseError:
            deselect()
            messagebox.showerror('showerror', 'DatabaseError')

def deselect():
    id_entry.configure(state='normal')
    selected = my_tree.focus()
    my_tree.selection_remove(selected)
    name_entry.delete(0, END)
    address_entry.delete(0, END)
    id_entry.delete(0, END)
    id_entry.configure(state='readonly')


my_menu = Menu(root)
root.config(menu=my_menu)
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=option_menu)
option_menu.add_command(label="Search", command=lookup_records)
option_menu.add_command(label="Reset", command=query_database)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=root.quit)


style = ttk.Style()
style.configure("Treeview", background="#D3D3D3", foreground="black",
                rowheight=25, fieldbackground="#D3D3D3")
tree_frame = Frame(root)
tree_frame.pack(pady=10)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()
tree_scroll.config(command=my_tree.yview)

my_tree['columns'] = ("ID", "Name", "Address")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=CENTER, width=50)
my_tree.column("Name", anchor=CENTER, width=300)
my_tree.column("Address", anchor=CENTER, width=600)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)


button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

watch_selected = Button(button_frame, text="Watch Selected Video", command=play_video)
watch_selected.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

deselect_button = Button(button_frame, text="Deselect/Clear entries", command=deselect)
deselect_button.grid(row=0, column=7, padx=10, pady=10)


data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(data_frame, width=10)
id_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = Label(data_frame, text="Name")
name_label.grid(row=0, column=2, padx=10, pady=10)
name_entry = Entry(data_frame, width=30)
name_entry.grid(row=0, column=3, padx=10, pady=10)

address_label = Label(data_frame, text="Address")
address_label.grid(row=0, column=4, padx=10, pady=10)
address_entry = Entry(data_frame, width=70)
address_entry.grid(row=0, column=5, padx=10, pady=10)

add_button = Button(data_frame, text="Add Record", command=add_record)
add_button.grid(row=1, column=1, padx=10, pady=10)

update_button = Button(data_frame, text="Update Record", command=update_record)
update_button.grid(row=1, column=2, padx=10, pady=10)

selected = my_tree.bind("<ButtonRelease-1>", select_record)
print(selected)

query_database()
root.mainloop()
