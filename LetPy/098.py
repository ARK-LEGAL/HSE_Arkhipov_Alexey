import tkinter
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

rect = canvas.create_rectangle(0, 0, 50, 50)
x = 0
delta = 2

while True:
    x = x + delta
    if x > 200:
        delta = -delta
    elif x < 0:
        delta = -delta
    canvas.update()
    time.sleep(0.01)
    canvas.coords(rect, x, 0, x+20, 50)
window.mainloop()