
from tkinter import *
from tkinter import messagebox
from project.exit_game_options import ExitOptions
from project.winner_check_and_display import Winner


class InitBoard:

    ROWS = 3

    def __init__(self):
        self.root = Tk()
        self.board_matrix = [["" for _ in range(InitBoard.ROWS)] for _ in range(InitBoard.ROWS)]
        self.count = 0

    def tkinter_initialize(self):
        self.root.title("Noughts & Crosses")
        self.root.configure(bg="white")

        self.assign_labels()
        self.create_buttons()
        return self.root

    def assign_labels(self):
        l1 = Label(self.root, text="Player_1: X", height=3, font=('COMIC SANS MS', 10, "bold"))
        l1.grid(row=0, column=0)

        exit_button = Button(self.root, text="Quit", font=("COMIC SANS MS", 10, "bold"))
        exit_button.grid(row=0, column=2)
        exit_button["command"] = lambda: ExitOptions.quit_game(self.root)

    def create_buttons(self):

        buttons = []
        button_count = 0

        for row_ in range(len(self.board_matrix)):
            for col_ in range(len(self.board_matrix)):
                buttons.append(Button(self.root, text="-", height=4, width=8, bg="black", activebackground="white",
                                      fg="white", font="Times 15 bold"))

                buttons[button_count].grid(row=row_ + 2 , column=col_) #account for first two rows
                buttons[button_count]["command"] = lambda \
                        button_count = button_count, row_=row_, col_=col_: \
                    self.change_value(buttons[button_count], row_ , col_ )
                button_count += 1

    def change_value(self, btn, row_ , col_):

        if btn["text"] == "-":
            if self.count % 2 == 0:
                btn["text"] = "X"
                l1 = Label(self.root, text="PLAYER: 2(O)", height=3, font=("COMIC SANS MS", 10, "bold")
                           , bg="white").grid(row=0, column=0)
                self.board_matrix[row_][col_] = "X"
            else:
                btn["text"] = "O"
                l1 = Label(self.root, text="PLAYER: 1(X)", height=3, font=("COMIC SANS MS", 10, "bold"),
                           bg="white").grid(row=0, column=0)
                self.board_matrix[row_][col_] = "O"
            self.count += 1
            print(self.board_matrix)
            Winner.check_for_winner(self.count, btn, self.board_matrix, self.root)
        else:
            messagebox.showerror("Error", "This field is already occupied")

    def __getitem__(self, item):
        return self.board_matrix[item]





        




