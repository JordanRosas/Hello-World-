import tkinter

window = tkinter.Tk()
window.title('Make Red or Make Blue')
window.geometry('300x100')


def make_red():
    window.configure(bg = 'red')
btn1 = tkinter.Button(window, text = 'red', command=make_red)
btn1.pack()


def make_blue():
    window.configure(bg = 'blue')
btn2 = tkinter.Button(window, text = 'blue', command=make_blue)
btn2.pack()

window.mainloop()


    
