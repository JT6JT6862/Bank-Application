from tkinter import*
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
from datetime import date

class Database:
    def __init__(self, window, filename):
        self.window = window
        self.filename = filename
        self.entries = []

    def earn(self):
        isValid = True
        while isValid:
            amount = sd.askfloat("Earn", "How much did you earn?\n(range from $0.10 to $100.00)", minvalue = 0.1, maxvalue = 100)
            print(amount)
            if amount == "":
                mb.showerror("Empty field", "The input field is empty")
            elif amount == None:
                return
            else:
                isValid = False
                data = "earn:" + str(date.today().strftime("%d/%m/%Y")) + ":" + format(amount, '.2f') + "\n"
                print(data)
        file = open(self.filename, "a")
        file.write(data)
        file.close()

    def read(self):
        file = open(self.filename, "r")
        data = file.read()
        file.close()

        self.entries = data.split("\n")
        self.entries.pop()

        for index in range(len(self.entries)):
            self.entries[index] = self.entries[index].split(":")

    def spent(self):
        isValid = True
        while isValid:
            amount = sd.askfloat("Spent", "How much did you spend?\n(range from $0.10 to $100.00)", minvalue = 0.1, maxvalue = 100)
            if amount == "":
                mb.showerror("Empty field", "The input field is empty")
            elif amount == None:
                return
            else:
                isValid = False

        isValid = True
        while isValid:
            item = sd.askstring("Spent", "What did you spend on ?")
            if item == "":
                mb.showerror("Empty field", "The input field is empty")
            elif item == None:
                return
            else:
                isValid = False

        data = "spent:" + str(date.today().strftime("%d/%m/%Y")) + ":" + format(amount, '.2f') + ":" + item + "\n"

        file = open(self.filename, "a")
        file.write(data)
        file.close()

    def clear_all(self):
        file = open(self.filename, "w")
        file.write("")
        file.close()

    def delete(self, index):
        self.entries.pop(index)
        data = ""
        for entry in self.entries:
            if entry[0] == "earn":
                data += entry[0] + ":" + entry[1] + ":" + format(float(entry[2]), '.2f') + "\n"
            elif entry[0] == "spent":
                data += entry[0] + ":" + entry[1] + ":" + format(float(entry[2]), '.2f') + ":" + entry[3] + "\n"
        
        file = open(self.filename, "w")
        file.write(data)
        file.close()

    def edit(self, index):
        if self.entries[index][0] == "earn":
            isValid = True
            while isValid:
                new_amount = sd.askfloat("Edit Earn", "Please enter a new amount for this earn entry", minvalue = 0.1, maxvalue = 100)
                if new_amount == "":
                    mb.showerror("Empty field", "The input field is empty")
                elif new_amount == None:
                    return
                else:
                    self.entries[index][2] = new_amount
                    isValid = False

        elif self.entries[index][0] == "spent":
            isValid = True
            while isValid:
                new_amount = sd.askfloat("Edit spent", "Please enter a new amount for this spent entry", minvalue = 0.1, maxvalue = 100)
                if new_amount == "":
                    mb.showerror("Empty field", "The input field is empty")
                elif new_amount == None:
                    return
                else:
                    self.entries[index][2] = new_amount
                    isValid = False
            
            isValid = True
            while isValid:
                new_item = sd.askstring("Edit spent", "Please enter a new item for this spent entry")
                if new_item == "":
                    mb.showerror("Empty field", "The input field is empty")
                elif new_item == None:
                    return
                else:
                    self.entries[index][3] = new_item
                    isValid = False

        data = ""
        for entry in self.entries:
            if entry[0] == "earn":
                data += entry[0] + ":" + entry[1] + ":" + format(float(entry[2]), '.2f') + "\n"
            
            elif entry in self.entries:
                if entry[0] == "spent":
                    data += entry[0] + ":" + entry[1] + ":" + format(float(entry[2]), '.2f') + ":" + entry[3] + "\n"

        file = open(self.filename, "w")
        file.write(data)
        file.close()