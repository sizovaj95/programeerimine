from tkinter import *

window = Tk()
window.title("The Ship")
area = Canvas(window, width=600, height=600, background="white")
area.grid()  # this geometry manager organizes widgets into a table-like structure

area.create_polygon(60,160, 270,160, 240,200, 90,200, fill="#593c0e", outline="black")
area.create_line(165,160, 165,40, width=5)
area.create_polygon(165,40, 165,150, 233,150, fill="#d8dedc", outline="black")

window.mainloop()