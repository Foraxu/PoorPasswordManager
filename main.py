import pyperclip  # Will serve to send some value to clipboard
import json
from tkinter import *
from tkinter import messagebox
from password import PasswordGenerator

DATA_FILE = 'data.json'

password_gen = PasswordGenerator()

# ------ | ------ | WINDOW | ------ | ------ | #

root = Tk()
root.title('Password Manager')
root.config(padx=20, pady=20)
root.resizable(False, False)

logo_img = PhotoImage(file='logo.png')

canvas = Canvas()
canvas.config(width=200, height=190)
logo_canvas = canvas.create_image(100, 95, image=logo_img)
canvas.grid(column=1, row=1)


# ------ | ------ | LABELS | ------ | ------ | #

site_label = Label(text='Site:')
email_label = Label(text='Email/Username:')
password_label = Label(text='Password:')

# ------ | ------ | ENTRIES | ------ | ------ | #

site_input = Entry(width=24)
email_input = Entry(width=35)
password_input = Entry(width=24)

# ------ | ------ | BUTTONS | ------ | ------ | #

gen_button = Button(text='Create')
save_button = Button(text='Save', width=34)
search_button = Button(text='Search')

# ------ | ------ | POSITIONING ITEMS ON THE WINDOW | ------ | ------ | #

site_label.grid(column=0, row=2)
email_label.grid(column=0, row=3)
password_label.grid(column=0, row=4)

site_input.grid(column=1, row=2)
email_input.grid(column=1, row=3, columnspan=2)
password_input.grid(column=1, row=4)

gen_button.grid(column=2, row=4)
save_button.grid(column=1, row=5, columnspan=2)
search_button.grid(column=2, row=2)

# ------ | ------ | BUTTONS FUCTIONS AND LOGIC | ------ | ------ | #


def gen_password():
    generated_password = password_gen.create_random_password()
    password_input.delete(0, END)
    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)
    

def save_data():
    site = site_input.get()
    email = email_input.get()
    password = password_input.get()
    contents = [site,email,password]
    confirm = None

    is_empty = False

    for entry in contents:
        if len(entry) == 0:
            is_empty = True

    if is_empty:
        messagebox.showerror(title='INPUT ERROR', message='Fill all the empty fields before saving.')
    else:
        confirm = messagebox.askquestion(title='', message='Confirm the entered data and click "yes" to proceed.')

    if confirm == 'yes':
                        
        new_data = {
            site:{
                'Email/Username': email,
                'Password': password,
            }
        }

        with open(DATA_FILE, 'r') as file:
            try:
                data = json.load(file)
            except json.decoder.JSONDecodeError:
                # File is empty
                data = new_data
            else:
                if site in data:
                        answer = messagebox.askyesno(message=f'The data related with the Website "{site}" is already saved.\nDo you want to overwrite it?')
                        if answer == 'yes':
                            return
                data.update(new_data)
            
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=2)


        # Delete all the content of the entries
        entries = [site_input, email_input, password_input]
        for entry in entries:
            entry.delete(0, END)


def search():
    site = site_input.get()

    if len(site) == 0:
        messagebox.showerror(message="Oops! You've wrote nothing in the Website field.")
        return

    with open(DATA_FILE) as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            messagebox.showerror(message='No information was saved yet.')
        else:
            try:
                data[site]
            except KeyError as wrong_key:
                messagebox.showerror(message=f'There is no site called {wrong_key} saved in the database.')
            else:
                messagebox.showinfo(title=site, message=f"Email/Username: {data[site]['Email/Username']}\nPassword: {data[site]['Password']}")


gen_button.config(command=gen_password)
save_button.config(command=save_data)
search_button.config(command=search)

root. mainloop()
