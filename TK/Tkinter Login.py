import tkinter
import ctypes
import sys

# Enable high DPI awareness for Windows to prevent scaling issues
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Use "2" for full DPI awareness (Windows 10)
except:
    pass

user = {
        'joness':'078',
        'sion':'123'
    }
input_user=None
input_password=None
mode = tkinter.NORMAL


def login():
    if user_entry.get().lower() in user and password_entry.get() == user[user_entry.get().lower()]:
        sys.exit()
    else:
        print('Access Denied')

def switch_state():
    global mode
    if mode == tkinter.DISABLED:
        mode = tkinter.NORMAL
    else:
        mode = tkinter.DISABLED
    user_entry.config(state=mode)

window = tkinter.Tk()
window.title("Login")
window.geometry('600x400')
window.configure(bg='#000000')

frame=tkinter.Frame(bg='#000000', pady=20)
frame.pack()

label = tkinter.Label(frame, fg='#20C20E', bg='#000000', text="Login", font=('arial rounded mt bold',30), pady=30)
label.grid(row=0, column=0, columnspan=3)
user_entry = tkinter.Entry(frame, font=('arial rounded mt bold',14), state=mode)
user_entry.grid(row=1, column=1, pady=10, padx=50)
password_entry = tkinter.Entry(frame, show='•', font=('arial rounded mt bold',14), state=mode)
password_entry.grid(row=2, column=1, pady=10, padx=50)
submit = tkinter.Button(frame, font=('arial rounded mt bold',10), text="Enter", command=login)
submit.grid(row=3, column=1, )

window.mainloop()