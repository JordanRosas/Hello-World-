import tkinter

window = tkinter.Tk()

for num in range(10):
    btn = tkinter.Button(window, text = num)
    btn.pack(side = tkinter.LEFT)
    
