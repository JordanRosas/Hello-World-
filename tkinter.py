import tkinter

window = tkinter.Tk()
window.title('simple gui')
window.geometry('400x200')
window.configure(background = 'powder blue')

intlabel = tkinter.Label(window, text = 'Please login to continue', bg = 'powder blue', font = 'cambria' '16pt')
label = tkinter.Label(window, text = 'Username', bg = 'powder blue', font = 'arial' '16pt')
ent = tkinter.Entry(window)
lbl = tkinter.Label(window, text = 'Password', bg = 'powder blue', font = 'arial' '16pt' )
enter = tkinter.Entry(window)
btn = tkinter.Button(window, text = 'Submit', bg = 'powder blue', font = 'arial' '16pt')

intlabel.pack()
label.pack()
ent.pack()
lbl.pack()
enter.pack()
btn.pack()

window.mainloop()

