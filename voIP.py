import tkinter

window = tkinter.Tk()
window.geometry('500x300')

intlabel = tkinter.Label(window, text = 'Click the name of the person you with to call: ', font = 'Cambria' '18pt')
intlabel.pack()

lbl1 = tkinter.Label(window, text = 'Click to call Samantha')
btn1 = tkinter.Button(window, text = 'Call Samantha')

lbl2 = tkinter.Label(window, text = 'Click to call Jeffrey')
btn2 = tkinter.Button(window, text = 'Call Jeffrey')

lbl3 = tkinter.Label(window, text = 'Click to call Zach')
btn3 = tkinter.Button(window, text = 'Call Zach')

lbl4 = tkinter.Label(window, text = 'Click to call Hamilton')
btn4 = tkinter.Button(window, text = 'Call Hamilton')

lbl1.pack()
btn1.pack()

lbl2.pack()
btn2.pack()

lbl3.pack()
btn3.pack()

lbl4.pack()
btn4.pack()

window.mainloop()

