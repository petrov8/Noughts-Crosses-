
from dataclasses import dataclass


@dataclass
class WinnerCheck:

    @staticmethod
    def check_rows(matrix, player_sign):

        # check rows
        for row in matrix:
            row_win = True
            for element in row:
                if element != player_sign:
                    row_win = False
                    break
            if row_win:
                return True

    @staticmethod
    def check_columns(matrix, player_sign):
        # check column
        winner = True
        for col in range(len(matrix)):
            col_win = True
            for row in range(len(matrix)):
                if matrix[row][col] != player_sign:
                    col_win = not col_win
                    break
            if col_win:
                return True

    @staticmethod
    def check_diagonals(matrix, player_sign):
        # check diagonals
        left_diagonal = True
        right_diagonal = True

        for idx in range(len(matrix)):
            if matrix[idx][idx] != player_sign:
                left_diagonal = False
            if matrix[idx][len(matrix) - 1 - idx] != player_sign:
                right_diagonal = False

        if left_diagonal or right_diagonal:
            return True
        return False


