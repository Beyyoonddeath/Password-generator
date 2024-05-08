from tkinter import Checkbutton, IntVar, Radiobutton, W, Label, Button, Tk
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choices


class passGen:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("170x250")
        master.resizable(False, False)

        self.checkboxes = []
        self.password_length = IntVar()
        self.password_length.set(5)

        for i, char_type in enumerate(["a-z", "A-Z", "Digits", "Special", "Curly Brackets", "Round Brackets", "Square Brackets"]):
            var = IntVar()
            checkbox = Checkbutton(master, text=char_type, variable=var)
            checkbox.grid(row=i, column=0, sticky=W)
            self.checkboxes.append((char_type, var))

        for i, length in enumerate([5, 10, 20]):
            radio = Radiobutton(master, text=str(length), variable=self.password_length, value=length)
            radio.grid(row=i, column=1, sticky=W)

        self.length_label = Label(master, textvariable=self.password_length)
        self.length_label.grid(row=len(self.checkboxes) + 1, column=0, columnspan=2)

        self.password_label = Label(master, text="")
        self.password_label.grid(row=len(self.checkboxes) + 2, column=0, columnspan=2)

        self.generate_button = Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=len(self.checkboxes) + 3, column=0, columnspan=2)

    def generate_password(self):
        sets = {
            "a-z": ascii_lowercase,
            "A-Z": ascii_uppercase,
            "Digits": digits,
            "Special": punctuation,
            "Curly Brackets": "}{",
            "Round Brackets": ")(",
            "Square Brackets": "]["
        }
        selected = ''
        for char_type, var in self.checkboxes:
            if var.get() == 1:
                char_set = sets.get(char_type, "")
                selected += char_set

            try:
                password = ''.join(choices(selected, k=self.password_length.get()))
            except IndexError:
                password = ''
                
        self.password_label.config(text=password)


root = Tk()
app = passGen(root)
root.mainloop()