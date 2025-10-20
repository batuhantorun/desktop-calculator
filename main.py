# main.py

import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Ana pencere
root = tk.Tk()
root.title("Desktop Calculator")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=5, relief="sunken")
screen.pack(fill="both", ipadx=8, pady=10, padx=10)

# Butonlar
buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(buttons_frame, text=btn_text, font="Arial 18", width=5, height=2)
        btn.grid(row=i, column=j, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
