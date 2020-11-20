from tkinter import *

root = Tk()
root.title("Hello World")
root.geometry("400x400")

my_label = Label(root, text="Hello World", fg="white", bg="black", font=("Helvtica", 32), width=200)
my_label.pack()

my_label2 = Label(root, text="I'm Ritchie!")
my_label2.pack()






root.mainloop()