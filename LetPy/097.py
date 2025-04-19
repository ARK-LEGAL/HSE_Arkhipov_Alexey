import tkinter
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

rect = canvas.create_rectangle(0, 0, 50, 50)
x = 0
while x < 200:
    x += 2
    x2 = x + 50
    canvas.update()
    time.sleep(0.01)
    canvas.coords(rect, x, 0, x2, 50)
window.mainloop()