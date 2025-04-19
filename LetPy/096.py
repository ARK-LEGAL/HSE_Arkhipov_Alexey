import tkinter
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()

rect = canvas.create_rectangle(10, 10, 50, 50)
canvas.update()
time.sleep(2)
canvas.coords(rect, 50, 50, 100, 100)
window.mainloop()