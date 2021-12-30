from tkinter import * 

def create_window():
    new_window = Toplevel()
    new_window.geometry("300x200")


window = Tk(className="ISS Tracker")
window.geometry("300x200")
window.configure(bg="#4a4a4a")

a = Button(window, text = "Create a new window", command=create_window).pack()


window.mainloop()