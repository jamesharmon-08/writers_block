from tkinter import *


COLOR = ['red', 'red', 'orange2', 'black', 'black']
TIMER = None
FONT = ('San Serif', 24)


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
    TIMER = window.after(1000, change_text, delay)


def on_key_press(event):

    try:
        char_code = ord(event.char)
    except TypeError:   # Non displayable key hit such as CMD, CTRL, Option ..
        print('Non displayable key hit')
        char_code = 0
    if char_code == 27:   # user hit ESC
        save_info()
        window.quit()

    if char_code >= 32:
        text.configure(state='normal')
        if char_code == 127:  # Backspace
            text.delete('end-2c', 'end-1c')
        else:
            if TIMER:
                window.after_cancel(TIMER)
            text.insert('end', event.char)
            change_text(5)

        text.configure(state='disabled')
        update_status()


def save_info():
    with open("writing.txt", mode='w') as f:
        f.write(text.get("1.0", 'end'))


def update_status():
    char_count = len(list(text.get(1.0, 'end')))
    if char_count % 100 == 0 and char_count > 1:  # save the last 100 characters to a file
        save_info()
    Label(window, text=f"Characters: {char_count}", width=67, background='green', foreground='white', font=FONT).place(
        x=0, y=765)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Writer's Block Assassin")
window.geometry('1000x800')

text = Text(window, width=66, background='White', foreground='black', font=FONT, wrap=WORD)
text.place(x=10, y=10)
text.configure(state='disabled')
update_status()


window.bind('<KeyPress>', on_key_press)

window.mainloop()
