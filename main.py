from tkinter import *

window = Tk()
window.iconbitmap("Icon/Tick.ico")
window.title("Seznam úkolů")
window.geometry("400x400")
window.resizable(False, False)

main_font = ("Arial", 12)
main_color = "#0c805b"
button_color = "#07003a"
button_fg_color = "white"
window.config(bg=main_color)


def tasks_to_tasktxt():
    with open("tasks.txt", "w") as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(one_task)
            else:
                file.write(f"{one_task}\n")


def add_text():
    if user_input.get() != "":
        list_box.insert(END, user_input.get())
        user_input.delete(0, END)


def open_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for one_task in file:
                list_box.insert(END, one_task)
    except:
        pass


def remove_item():
    list_box.delete(ANCHOR)


def clear_list():
    list_box.delete(0, END)


# Framy
input_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg=main_color)
button_frame = Frame(window, bg=main_color)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# Vstup od uživatele a přidání úkolu
user_input = Entry(input_frame, font=main_font, borderwidth=3, width=28)
user_input.focus()
user_input.grid(row=0, column=0, pady=(5, 3), padx=(7, 5))
add_button = Button(input_frame, font=main_font, borderwidth=3, text="Add text", bg=button_color, fg=button_fg_color,
                    command=add_text, activebackground="#00cfc8")
add_button.grid(row=0, column=1, pady=5, padx=5)

# přidání úkolu pomocí enteru
window.bind("<Return>", lambda event: add_text())

# seznam a scrollbar
scrollbar = Scrollbar(text_frame)
scrollbar.grid(row=0, column=1, sticky=N+S)

list_box = Listbox(text_frame, borderwidth=3, width=40, height=15, yscrollcommand=scrollbar.set, font=main_font,
                   bg="#9697a2")
list_box.grid(row=0, column=0)
scrollbar.config(command=list_box.yview)

# buttony
clear_list_button = Button(button_frame, text="Clear list", font=main_font, bg=button_color, fg=button_fg_color,
                           borderwidth=3, command=clear_list, activebackground="#00cfc8")
remove_item_button = Button(button_frame, text="remove item", font=main_font, bg=button_color, fg=button_fg_color,
                            borderwidth=3, command=remove_item, activebackground="#00cfc8")
save_button = Button(button_frame, text="Save", font=main_font, bg=button_color, fg=button_fg_color, borderwidth=3,
                     command=tasks_to_tasktxt, activebackground="#00cfc8")
quit_button = Button(button_frame, text="QUIT", font=main_font, bg=button_color, fg=button_fg_color, borderwidth=3,
                     command=window.destroy, activebackground="#00cfc8")

clear_list_button.grid(row=0, column=0, pady=(12, 0), padx=5, ipadx=5, ipady=2)
remove_item_button.grid(row=0, column=1, pady=(12, 0), padx=5, ipady=2)
save_button.grid(row=0, column=2, pady=(12, 0), padx=5, ipadx=17, ipady=2)
quit_button.grid(row=0, column=3, pady=(12, 0), padx=5, ipadx=18, ipady=2)

open_tasks()

window.mainloop()
