from tkinter import *


def cal():
    val = int(in_put.get())
    kms_val = int(val * 1.609)
    label3.config(text=kms_val)


window = Tk()
window.title("miles-kilometers calculator")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

in_put = Entry(width=10)
in_put.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label1.config(padx=20, pady=20)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)
label2.config(padx=20, pady=20)

label3 = Label(text="0")
label3.grid(column=1, row=1)
label3.config(padx=20, pady=20)

label4 = Label(text="Kms")
label4.grid(column=2, row=1)
label4.config(padx=20, pady=20)

button = Button(text="calculate", width="15", command=cal)
button.grid(column=1, row=2)

window.mainloop()
