#imprt tkinter 
import tkinter
#create a window
window = tkinter.Tk()
window.title ('Commands')
#dunction that changes the text of a label
def callback():
    lbl.configure(text = 'Button Clicked')
#create a label to display a message 
lbl = tkinter.Label(window, text = 'Nothing happened yet!')
#create a new button to provide an argument called 'command'
#which in this case calls the callback function
btn = tkinter.Button(window, text = 'Click Me', command = callback)
#pack the text in the window
lbl.pack()
btn.pack()

window.mainloop()
