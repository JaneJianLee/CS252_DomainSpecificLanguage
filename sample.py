from tkinter import *
master = Tk()
w = None
canvas_width = 300
canvas_height =300

def create():
    global w
    w = Canvas(master,width=canvas_width,height=canvas_height)
create()
w.pack()

y = int(canvas_height / 2)
#w.create_line(0, y, canvas_width, y, fill="#476042")
w.create_text(100,200,fill="black",font="Times 20 italic bold",text="judy")

mainloop()