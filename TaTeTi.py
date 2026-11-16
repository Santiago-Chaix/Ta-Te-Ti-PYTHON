import tkinter

def set_tile(row, column):
    global curr_player

    if (game_over):
        return

    if board[row][column]["text"] != "":

        return
    
    board[row][column]["text"] = curr_player

    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO
    
    label["text"] = curr_player+", es tu turno!"

    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" es el ganador!", foreground=color_orange)
            for column in range(3):
                board[row][column].config(foreground=color_orange, background=color_light_gray)
            game_over = True
            return
    
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" es el ganador!", foreground=color_orange)
            for row in range(3):
                board[row][column].config(foreground=color_orange, background=color_light_gray)
            game_over = True
            return
    
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"]+" es el ganador!", foreground=color_orange)
        for i in range(3):
            board[i][i].config(foreground=color_orange, background=color_light_gray)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" es el ganador!", foreground=color_orange)
        board[0][2].config(foreground=color_orange, background=color_light_gray)
        board[1][1].config(foreground=color_orange, background=color_light_gray)
        board[2][0].config(foreground=color_orange, background=color_light_gray)
        game_over = True
        return
    
    if (turns == 9):
        game_over = True
        label.config(text="¡Empate!", foreground=color_orange)


def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=curr_player+", es tu turno", foreground="orange")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_gray)

playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

color_blue = "blue"
color_orange = "orange"
color_gray = "black"
color_light_gray = "black"

turns = 0
game_over = False

window = tkinter.Tk()
window.title("Ta Te Ti")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+", es tu turno", font=("Comic sans", 20), background=color_gray,
                      foreground="orange")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="¡OTRA VEZ!", font=("Consolas", 20), background=color_gray,
                        foreground="orange", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
