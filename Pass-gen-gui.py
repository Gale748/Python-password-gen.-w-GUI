import string
import random
import tkinter as tk

def generate_password(length):
    password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

def generate_password_cmd():
    length = length_scale.get()
    password = generate_password(length)
    password_label.config(text="Password: " + password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password_cmd():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

root = tk.Tk()
root.title("Random Password Generator")

length_frame = tk.Frame(root)
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Password Length:")
length_label.pack(side="left")

length_scale = tk.Scale(length_frame, from_=16, to=32, orient="horizontal", resolution=1)
length_scale.set(16)
length_scale.pack(side="left")

password_frame = tk.Frame(root)
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="Password: ")
password_label.pack(side="left")

password_entry = tk.Entry(password_frame, width=30)
password_entry.pack(side="left")

generate_button = tk.Button(root, text="Generate Password", command=generate_password_cmd)
generate_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy Password", command=copy_password_cmd)
copy_button.pack()

root.mainloop()