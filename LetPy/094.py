from tkinter import *
window = Tk()
window.title('Работа на LETPY.COM')
canvas = Canvas(window,width=600,height=600,bg="gray",
          cursor="pencil")
canvas.create_line(0,0,600,600,width=5,fill="yellow")
canvas.create_line(0,600,600,0,width=5,fill="yellow")
canvas.create_rectangle(50,250,300,500,fill="white",outline="blue")
canvas.create_oval([400,250],[450,300],fill="pink")
canvas.create_polygon([400,400],[300,400],[350,300],fill="gray", outline="yellow")
canvas.create_text(250,280,text="Normanramm",
          font="Verdana 12",justify=CENTER,fill="red")
canvas.pack()
window.mainloop()
