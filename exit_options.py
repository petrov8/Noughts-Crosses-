
from tkinter import messagebox


class ExitOptions:

    @staticmethod
    def kill_winner_window(button, winner_window):
        button["command"] = winner_window.destroy

    @staticmethod
    def kill_game(root):
        root.destroy()

    @staticmethod
    def quit_game(root):
        msg = messagebox.askquestion("Confirm", "Do you want to quit?")
        if msg == "yes":
            ExitOptions.kill_game(root)


