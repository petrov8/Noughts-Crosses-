
from dataclasses import dataclass

from tkinter import Tk, Label, Button
from project.check_if_winner import WinnerCheck
from project.exit_options import ExitOptions


@dataclass
class Winner:

    def __init__(self):
        pass

    @staticmethod
    def display_winner(winner, root):
        if winner != "It's a tie!":
            winner = "Player X" if winner == "X" else "Player O"
        winner_window = Tk()
        winner_window.title("Winner Window")
        winner_window.configure(bg="Black")
        l1 = Label(winner_window, text=f"The winner is:\n{winner}", font=('COMIC SANS MS', 15), bg='Black', fg="White")
        l1.pack()
        l2 = Label(winner_window, text="", font=('COMIC SANS MS', 15, 'bold'), bg='Black', fg="White")
        l2.pack()

        b_proceed = \
            Button(winner_window, text="OK", font=("COMIC SANS MS", 10, "bold"))
        b_proceed.pack()
        ExitOptions.kill_winner_window(b_proceed, winner_window)
        ExitOptions.kill_game(root)

    @staticmethod
    def kill_game(root, winner_window):
        root.destroy()
        winner_window.destroy()

    @staticmethod
    def check_for_winner(count, btn, board, root):
        if count == 9:
            Winner.display_winner("it's a tie!", root)
        if WinnerCheck.check_rows(board, btn["text"]) or \
                WinnerCheck.check_columns(board, btn["text"]) or \
                WinnerCheck.check_diagonals(board, btn["text"]):
            Winner.display_winner(btn["text"], root)




