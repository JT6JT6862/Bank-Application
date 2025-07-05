from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox as mb
from Bankdatabase import Database

window = Tk()
bg_color = "#1b262c"
db = Database(window, "filename.txt")

current_amount = 0

#############################function##########################################

def earn():
    db.earn()
    populate_list()

def spent():
    db.spent()
    populate_list()

def delete():
    if len(entry_listbox.curselection()) == 0:
        mb.showerror("Error", "Pls select an entry to delete")
    else:
        db.delete(entry_listbox.curselection()[0])
        entry_listbox.delete(entry_listbox.curselection())
        populate_list()

def edit():
    if len(entry_listbox.curselection()) == 0:
        mb.showerror("Error", "You need to select an entry to edit!")
    else:
        db.edit(entry_listbox.curselection()[0])
        populate_list()

def clear_all():
    db.clear_all()
    populate_list()

def populate_list():
    db.read()
    global current_amount
    current_amount = 0 
    entry_listbox.delete(0, END)

    for entry in db.entries:
        if entry[0] == "earn":
            data = entry[1] + ": You earned $" + entry[2]
            entry_listbox.insert(END, data)
            current_amount += float(entry[2])
        
        if entry[0] == "spent":
            data = entry[1] + ": You spent $" + entry[2] + " on " + entry[3]
            entry_listbox.insert(END, data)
            current_amount -= float(entry[2])

    # Update the current amount label
    cur.config(text="$" + format(current_amount, '.2f'))

#########################################TOP FRAME#############################################
topframe = Frame(window, bg = bg_color)
#photo
profile_photo = ImageTk.PhotoImage(Image.open("Images 3/profile.png").resize((80,80), Image.LANCZOS))
pplabel = Label(topframe, image = profile_photo, bg = bg_color)

#Name
name_label = Label(topframe, text = "Name:", font = ("", 13), bg = "#1b262c", fg = "white", width = 15)
name = Label(topframe, text = "Jayden", font = ("", 20, "bold"), bg = "#1b262c", width = 15, fg = "white")
#ammount
curlabel = Label(topframe,text = "Current ammount:", font = ("", 13), bg = "#1b262c", width = 15, fg = "white")
cur = Label(topframe, text="$0.00", font = ("", 20, "bold"), bg = "#1b262c", width = 15, fg = "white")

pplabel.grid(row = 0, column = 0, rowspan = 2, padx = 50, pady = 20)
name_label.grid(row = 0, column = 1)
name.grid(row = 0, column = 2)
curlabel.grid(row = 1, column = 1)
cur.grid(row = 1, column = 2)

topframe.grid(row = 0, column = 0, columnspan = 3, sticky = "nsew")

########################################LEFT FRAME###############################################
leftframe = Frame(window, bg = bg_color)
#earn
earn_image = ImageTk.PhotoImage(Image.open("Images 3/add.png").resize((100,100), Image.LANCZOS))
earn_button = Button(leftframe, image = earn_image, bg = "#ffa372", width = 200, height = 150, command = earn)
earn_label = Label(leftframe, text = "Earn Money", bg = "#1b262c", fg = "white")
#spent
spent_image = ImageTk.PhotoImage(Image.open("Images 3/minus.png").resize((100,100), Image.LANCZOS))
spent_button = Button(leftframe, image = spent_image, bg = "#ffa372", width = 200, height = 150, command = spent)
spent_label = Label(leftframe, text = "Spend Money", bg = "#1b262c", fg = "white")
#clear
clear_image = ImageTk.PhotoImage(Image.open("Images 3/clear.png").resize((100,100), Image.LANCZOS))
clear_button = Button(leftframe, image = clear_image, bg = "#ffa372", width = 200, height = 150, command = clear_all)
clear_label = Label(leftframe, text = "Clear All Entries", bg = "#1b262c", fg = "white")

earn_button.grid(row = 0, column = 0)
earn_label.grid(row = 1, column = 0)
spent_button.grid(row = 2, column = 0)
spent_label.grid(row = 3, column = 0)
clear_button.grid(row = 4, column = 0)
clear_label.grid(row = 5, column = 0)

leftframe.grid(row = 1, column = 0, sticky = "ns")

#####################################MID FRAME#####################################################
midframe = Frame(window, bg = bg_color)
#Entries
entry_title = Label(midframe, text = "History", bg = bg_color, fg = "white", font = ("", 20, "bold"))
entry_listbox = Listbox(midframe, font = ("", 12), bg = bg_color, fg = "white", width = 40, height = 27)

entry_title.grid(row = 0, column = 0)
entry_listbox.grid(row = 1, column = 0, sticky = "news")

midframe.grid(row = 1, column = 1, sticky = "news")

######################################RIGHT FRAME#####################################################
rightframe = Frame(window, bg = bg_color)
#edit
edit_image = ImageTk.PhotoImage(Image.open("Images 3/edit.png").resize((100,100), Image.LANCZOS))
edit_button = Button(rightframe, image = edit_image, bg = "#ffa372", width = 200, height = 150, command = edit)
edit_label = Label(rightframe, text = "Edit Entry", bg = "#1b262c", fg = "white")
#delete
delete_image = ImageTk.PhotoImage(Image.open("Images 3/delete.png").resize((100,100), Image.LANCZOS))
delete_button = Button(rightframe, image = delete_image, bg = "#ffa372", width = 200, height = 150, command = delete)
delete_label = Label(rightframe, text = "Delete Entry", bg = "#1b262c", fg = "white")

edit_button.grid(row = 0, column = 2)
edit_label.grid(row = 1, column = 2)
delete_label.grid(row = 3, column = 2)
delete_button.grid(row = 2, column = 2)

rightframe.grid(row = 1, column = 2, sticky = "ns")

populate_list()

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
midframe.grid_rowconfigure(1, weight=1)
midframe.grid_columnconfigure(0, weight=1)

window.mainloop()