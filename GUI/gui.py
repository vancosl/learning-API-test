import tkinter


def show_info():
    print("U have already click")


top = tkinter.Tk()
B = tkinter.Button(top, text="this is a button", command=show_info)
B.pack()
top.mainloop()

