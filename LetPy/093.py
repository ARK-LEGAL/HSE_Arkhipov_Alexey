import tkinter
window = tkinter.Tk()
canvas = tkinter.Canvas(window)
canvas.pack()
canvas.create_rectangle(10, 60, 100, 50)
canvas.create_rectangle(30, 70, 200, 150)
window.mainloop()