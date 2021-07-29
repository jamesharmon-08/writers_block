from tkinter import *
from tkinter import messagebox
import time

COLOR = ['red','red','orange2','black','black']
TIMER = None
FONT = ('San Serif', 24)

def current_milli_time():
    return round(time.time() * 1000)

def change_text(delay):
    delay -= 1
    print(delay)
    global TIMER
    if delay == 0:
        text.configure(state='normal')
        text.delete(1.0, 'end')
        text.configure(state='disabled')
        update_status()
        return
    text.configure(foreground=COLOR[delay])
    TIMER = window.after(1000, change_text,delay)

def onKeyPress(event):
    global start
    try:
        ascii = ord(event.char)
    except TypeError:   # Non displayable key hit such as CMD, CTRL, Option ..
        print('Non displayable key hit')
        ascii=0

    if ascii >= 32:
        text.configure(state='normal')
        if ascii == 127: # Backspace
            text.delete('end-2c','end-1c')
        else:
            if TIMER:
                window.after_cancel(TIMER)
            text.insert('end', event.char)
            change_text(5)
            start = current_milli_time()
        text.configure(state='disabled')
        update_status()


def update_status():
    char_count = len(list(text.get(1.0,'end'))) - 1
    status_bar = Label(window, text=f"Characters: {char_count}", width=60, background='green', foreground='white', font=FONT).place(
        x=10, y=765)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Writer's Block Assassin")
window.geometry('1000x800')

text = Text(window, width=60, background='White', foreground='black', font=FONT, wrap=WORD)
text.place(x=10, y=10)
text.configure(state='disabled')
update_status()


window.bind('<KeyPress>', onKeyPress)

window.mainloop()
