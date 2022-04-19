from tkinter import *
from tkinter import messagebox
from pandas import *

# Where we store contacts
contact_list = {}


def search(name=None, number=None):

    if (name == None and number == None) or (name not in contact_list.keys() and number not in contact_list.values()):
        messagebox.showwarning(title="WOW", message="Contact Not Found")
        return

    # New search Window
    search_window = Tk()
    search_window.title("Contact Found")
    search_window.geometry("300x300")

    # making separate list to print the name/number associated with name/number using index
    contact_key_list = list(contact_list.keys())
    contact_value_list = list(contact_list.values())

    if name in contact_key_list:
        info = Label(search_window, text=f"{name} : {contact_value_list[contact_key_list.index(name)]}", font=17)
        info.grid()
        return
    elif number in contact_value_list:
        info = Label(search_window, text=f"{contact_key_list[contact_value_list.index(number)]} : {number}", font=17)
        info.grid()
        return


def update(name, number):

    contact_key_list = list(contact_list.keys())
    contact_value_list = list(contact_list.values())

    if name in contact_key_list:
        if number not in contact_value_list:
            contact_list.pop(name)
            contact_list[name] = number
            messagebox.showinfo("Done..", "Successfully Updated...")
            return
    elif number in contact_value_list:
        if name not in contact_key_list:
            contact_list.pop(contact_key_list[contact_value_list.index(number)])
            contact_list[name] = number
            messagebox.showinfo("Done..", "Successfully Updated...")
            return


def delete(name=None, number=None):

    contact_key_list = list(contact_list.keys())
    contact_value_list = list(contact_list.values())

    if name in contact_key_list and number in contact_value_list:
        contact_list.pop(name)
        messagebox.showinfo("Done..", "Successfully Deleted...")
        return

    if name in contact_key_list:
        if number not in contact_value_list and number != None:
            contact_list.pop(name)
            messagebox.showinfo("Done..", "Successfully Deleted...")
        return

    elif number in contact_value_list:
        if name not in contact_key_list and name != None:
            contact_list.pop(contact_key_list[contact_value_list.index(number)])
            messagebox.showinfo("Done..", "Successfully Deleted...")
        return

    messagebox.showwarning("WOW", "Contact is not present in the list")


def add(name=None, number=None):

    contact_key_list = list(contact_list.keys())
    contact_value_list = list(contact_list.values())

    if name == None or name == "":
        messagebox.showwarning("Wait", "Fields cannot be empty !")
        return

    elif number == None or number == "":
        messagebox.showwarning("Wait", "Fields cannot be empty !")
        return

    elif (name == None and name == "") and (number == None and number == ""):
        messagebox.showwarning("Wait", "Fields cannot be empty !")
        return

    elif name in contact_key_list and (number != None and number not in contact_value_list):
        messagebox.showwarning("Wait", "Name already exist !")
        return

    elif number in contact_value_list and (name != None and name not in contact_key_list):
        messagebox.showwarning("Wait", "Number already exist !")
        return

    elif name in contact_key_list and number in contact_value_list:
        messagebox.showwarning("Wait", "Contact already exist !")
        return

    else:
        contact_list[name] = number
        messagebox.showinfo("Done..", "Successfully Added...")
    return


def view_contact():

    # Making separate window to see contact list
    view = Tk()
    view.geometry("620x600")
    view.title("Contacts")
    contacts = contact_list.values()
    row_value = 6
    for contacts_name, contacts_number in contact_list.items():
        info = Label(view, text=f"{contacts_name} : {contacts_number}", font=16)
        info.grid(row=row_value, column=1)
        row_value += 1


root = Tk()
root.title("PhoneBook")
root.geometry("760x500")

welcome = Label(root, text="Welcome to the PhoneBook I'm ready to work... 😊😊", font=16).grid(row=1, column=1, columnspan=5, pady=10)

names = Label(root, text="Name :", font=14).grid(row=3, column=1, pady=20)
name_entry = Entry(root, font=18)
name_entry.grid(row=3, column=2, pady=20)

numbers = Label(root, text="Number :", font=14).grid(row=3, column=3, pady=20)
number_entry = Entry(root, font=18)
number_entry.grid(row=3, column=4, pady=20)


add_button = Button(root, font=14, text="Add", command=lambda: add(name_entry.get(), number_entry.get())).grid(row=5, column=1, pady=10)
search_button = Button(root, font=14, text="Search", command=lambda: search(name_entry.get(), number_entry.get())).grid(row=5, column=2, pady=10)
update_button = Button(root, font=14, text="Update", command=lambda: update(name_entry.get(), number_entry.get())).grid(row=5, column=3, pady=10)
delete_button = Button(root, font=14, text="Delete", command=lambda: delete(name_entry.get(), number_entry.get())).grid(row=5, column=4, pady=10)
view_button = Button(root, font=14, text="View Contacts", command=view_contact).grid(row=5, column=5, pady=10)


root.mainloop()
