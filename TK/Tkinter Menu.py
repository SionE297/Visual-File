import tkinter
import ctypes

# Enable high DPI awareness for roots to prevent scaling issues
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Use "2" for full DPI awareness (Windows 10+)
except:
    pass

bg0 = '#000000'
fg0 = '#ffffff'

# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to create the main menu
def open_menu():
    menu = tkinter.Tk()
    menu.title("Options")
    menu.configure(bg=bg0)
    center_window(menu, 800, 500)

    # Main frame
    menu_frame = tkinter.Frame(menu, bg='#333333', height=200, width=400)
    menu_frame.pack()

    # Options
    option_0 = tkinter.Label(menu_frame, bg=bg0, fg=fg0, font=('arial rounded mt bold', 20), text='Option 1')
    option_0.pack()
    option_1 = tkinter.Label(menu_frame, bg=bg0, fg=fg0, font=('arial rounded mt bold', 20), text='Option 2')
    option_1.pack()
    option_2 = tkinter.Label(menu_frame, bg=bg0, fg=fg0, font=('arial rounded mt bold', 20), text='Option 3')
    option_2.pack()
    option_3 = tkinter.Label(menu_frame, bg=bg0, fg=fg0, font=('arial rounded mt bold', 20), text='Option 4')
    option_3.pack()

    # Keep track of current option
    current_option = 0
    options = [option_0, option_1, option_2, option_3]

    # Update option color
    def highlight_option(option_index):
        for i, option in enumerate(options):
            if i == option_index:
                option.config(bg='#ffffff', fg='#000000')
            else:
                option.config(bg=bg0, fg=fg0)

    # Set initial highlight
    highlight_option(current_option)

    # Define what happens when "Enter" is pressed
    def press():
        nonlocal current_option
        if current_option == 0:
            menu.destroy()
            open_opt0()
        elif current_option == 1:
            menu.destroy()
            # Additional actions for Option 2
        elif current_option == 2:
            menu.destroy()
            # Additional actions for Option 3
        elif current_option == 3:
            menu.destroy()
            # Additional actions for Option 4

    # Event handling for up/down keys
    def on_key_press(event):
        nonlocal current_option
        if event.keysym == 'Up':
            current_option = (current_option - 1) % len(options)
        elif event.keysym == 'Down':
            current_option = (current_option + 1) % len(options)
        highlight_option(current_option)
        if event.keysym == 'Return':
            press()

    # Bind arrow keys and Enter to window
    menu.bind("<Up>", on_key_press)
    menu.bind("<Down>", on_key_press)
    menu.bind("<Return>", on_key_press)

    menu.mainloop()

# Function to create the opt0 window
def open_opt0():
    opt0 = tkinter.Tk()
    opt0.title("Messages")
    opt0.configure(bg=bg0)
    center_window(opt0, 400, 200)

    # Message label
    message_label = tkinter.Label(opt0, text="This is Option 1", font=('arial rounded mt bold', 20), fg=fg0, bg=bg0)
    message_label.pack(pady=20)

    # Button to go back to menu
    back_button = tkinter.Button(opt0, text="Back to Menu", bg='#333333', fg='#ff0000', command=lambda: [opt0.destroy(), open_menu()])
    back_button.pack(pady=10)

    opt0.mainloop()

# Start by opening the menu
open_menu()
