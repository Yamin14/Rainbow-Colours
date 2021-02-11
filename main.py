from tkinter import *
root = Tk()

h = 45

Label(root, text="Red", font=("Comic Sans MS", h), fg="violet", bg="red", padx=700).pack()

Label(root, text="Orange", font=("Comic Sans MS", h), fg="indigo", bg="orange", padx=700).pack()

Label(root, text="Yellow", font=("Comic Sans MS", h), fg="blue", bg="yellow", padx=700).pack()

Label(root, text="Green", font=("Comic Sans MS", h), fg="lime", bg="green", padx=700).pack()

Label(root, text="Blue", font=("Comic Sans MS", h), fg="yellow", bg="blue", padx=700).pack()

Label(root, text="Indigo", font=("Comic Sans MS", h), fg="orange", bg="indigo", padx=700).pack()

Label(root, text="Violet", font=("Comic Sans MS", h), fg="red", bg="violet", padx=700).pack()


root.mainloop()
