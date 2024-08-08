#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
import tkinter as tk
from tkinter import messagebox

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score

def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)

def empty_cells(state):
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells

def valid_move(x, y):
    if [x, y] in empty_cells(board):
        return True
    else:
        return False

def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False

def minimax(state, depth, player, ai_log, gui, current_depth=0):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player

        if gui.show_ai_moves.get() and current_depth < int(gui.visualize_depth_var.get()):
            gui.update_buttons()
            gui.window.update()
            time.sleep(0.5)

        score = minimax(state, depth - 1, -player, ai_log, gui, current_depth + 1)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

        if gui.show_ai_moves.get() and current_depth < int(gui.visualize_depth_var.get()):
            ai_log.append(f'Checking move at ({x}, {y}) with score {score[2]} at depth {current_depth + 1}')
            gui.log_text.insert(tk.END, f'Checking move at ({x}, {y}) with score {score[2]} at depth {current_depth + 1}\n')
            gui.log_text.see(tk.END)

    return best

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.h_choice = ''
        self.c_choice = ''
        self.current_player = HUMAN
        self.ai_log = []
        self.show_ai_moves = tk.BooleanVar()
        self.play_depth_var = tk.StringVar(value="2")
        self.visualize_depth_var = tk.StringVar(value="2")
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        for x in range(3):
            for y in range(3):
                button = tk.Button(self.window, text='', font=('Arial', 40), width=5, height=2,
                                   command=lambda x=x, y=y: self.human_turn(x, y))
                button.grid(row=x, column=y)
                self.buttons[x][y] = button

        self.show_ai_checkbox = tk.Checkbutton(self.window, text="Show AI moves", variable=self.show_ai_moves)
        self.show_ai_checkbox.grid(row=3, column=0, columnspan=3)

        self.play_depth_label = tk.Label(self.window, text="AI Play Depth:")
        self.play_depth_label.grid(row=4, column=0)
        self.play_depth_menu = tk.OptionMenu(self.window, self.play_depth_var, "1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.play_depth_menu.grid(row=4, column=1)

        self.visualize_depth_label = tk.Label(self.window, text="AI Visualize Depth:")
        self.visualize_depth_label.grid(row=4, column=2)
        self.visualize_depth_menu = tk.OptionMenu(self.window, self.visualize_depth_var, "1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.visualize_depth_menu.grid(row=4, column=3)

        self.log_text = tk.Text(self.window, height=10, width=50)
        self.log_text.grid(row=5, column=0, columnspan=4)
        self.choose_side()

    def choose_side(self):
        side = messagebox.askquestion("Choose your side", "Do you want to be X?")
        if side == 'yes':
            self.h_choice = 'X'
            self.c_choice = 'O'
        else:
            self.h_choice = 'O'
            self.c_choice = 'X'

        first = messagebox.askquestion("First move", "Do you want to start first?")
        if first == 'no':
            self.ai_turn()

    def update_buttons(self):
        for x in range(3):
            for y in range(3):
                if board[x][y] == HUMAN:
                    self.buttons[x][y].config(text=self.h_choice, state=tk.DISABLED)
                elif board[x][y] == COMP:
                    self.buttons[x][y].config(text=self.c_choice, state=tk.DISABLED)
                else:
                    self.buttons[x][y].config(text='', state=tk.NORMAL)

    def check_game_over(self):
        if wins(board, HUMAN):
            self.update_buttons()
            messagebox.showinfo("Game Over", "You win!")
            self.window.quit()
        elif wins(board, COMP):
            self.update_buttons()
            messagebox.showinfo("Game Over", "You lose!")
            self.window.quit()
        elif len(empty_cells(board)) == 0:
            self.update_buttons()
            messagebox.showinfo("Game Over", "It's a draw!")
            self.window.quit()

    def ai_turn(self):
        self.log_text.delete('1.0', tk.END)  # Clear previous log
        self.ai_log.clear()
        depth = int(self.play_depth_var.get())  # Get selected play depth
        if depth == 0 or game_over(board):
            return

        if len(empty_cells(board)) == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = minimax(board, depth, COMP, self.ai_log, self)
            x, y = move[0], move[1]

        set_move(x, y, COMP)
        self.update_buttons()
        self.check_game_over()
        self.current_player = HUMAN

    def human_turn(self, x, y):
        if self.current_player == HUMAN and valid_move(x, y):
            set_move(x, y, HUMAN)
            self.update_buttons()
            self.check_game_over()
            self.current_player = COMP
            self.window.after(100, self.ai_turn)

if __name__ == "__main__":
    TicTacToeGUI()
