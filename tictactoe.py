import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text=" ", width=10, height=5,
                                   command=lambda row=i, col=j: self.click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.status = tk.Label(master, text="Player X's turn", font=("Arial", 16))
        self.status.grid(row=3, columnspan=3)

    def click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player)
            if self.check_win():
                self.game_over()
            elif self.check_tie():
                self.game_over(tie=True)
            else:
                self.switch_player()

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        self.status.configure(text=f"Player {self.current_player}'s turn")

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def game_over(self, tie=False):
        if tie:
            message = "Tie game!"
        else:
            message = f"Player {self.current_player} wins!"
        messagebox.showinfo("Game Over", message)
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    tic_tac_toe = TicTacToe(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text=" ", width=10, height=5,
                                   command=lambda row=i, col=j: self.click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.status = tk.Label(master, text="Player X's turn", font=("Arial", 16))
        self.status.grid(row=3, columnspan=3)

    def click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player)
            if self.check_win():
                self.game_over()
            elif self.check_tie():
                self.game_over(tie=True)
            else:
                self.switch_player()

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        self.status.configure(text=f"Player {self.current_player}'s turn")

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def game_over(self, tie=False):
        if tie:
            message = "Tie game!"
        else:
            message = f"Player {self.current_player} wins!"
        messagebox.showinfo("Game Over", message)
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    tic_tac_toe = TicTacToe(root)
    root.mainloop()
