import tkinter

window = tkinter.Tk()
window.title('Colors')

colors = ['red','orange','yellow','green','blue','purple']

for c in colors:
    b = tkinter.Button(text = c, bg = c)
    b.pack(fill=tkinter.X)
