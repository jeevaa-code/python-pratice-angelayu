# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

import tkinter

windows = tkinter.Tk()
windows.title("pomodoro")
windows.config(padx=100,pady=50)
canvas = tkinter.Canvas(width=220,height=223)
tomato_pic = tkinter.PhotoImage(file = "tomato.png")
canvas.create_image(105,112,image=tomato_pic)
canvas.create_text(105,112 ,text="00:00",font=FONT_NAME)
canvas.pack()



windows.mainloop()
