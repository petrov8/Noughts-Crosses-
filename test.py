


from tkinter import *

rows = 3

root = Tk()
root.title("Noughts & Crosses")
root.configure(bg="white")


matrix = [["-" for x in range(rows)] for _ in range(rows)]

buttons = []
buttons_count = 0

for row_ in range(rows):
    for col_ in range(rows):
        buttons.append(Button(root, text="works", height=4, width=8, bg="black", activebackground="white",
                                      fg="white", font="Times 15 bold"))

        buttons[buttons_count]["command"] =lambda buttons_count= buttons_count: \
            change_value(buttons[buttons_count], row_, col_)

        buttons[buttons_count].grid(row = row_, column= col_)
        buttons_count += 1


def change_value(btn, r, c):


    print(btn["text"])


print(matrix)

root.mainloop()
print()