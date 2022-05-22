# Imports to be used:
import random
from guizero import App, Box, Combo, PushButton, Text


# Functions area:
def clear_board():
    """This function creates a new board when called."""
    new_board = [[None,None,None],
                 [None,None,None],
                 [None,None,None]]
    for x_axis in range(3):
        for y_axis in range(3):
            button = PushButton(
                board, text = "", grid=[x_axis,y_axis], width = 3, command=choose_square, args=[x_axis,y_axis]
            )
            button.text_size = "24"
            button.text_color = "red"
            button.text = "-"
            new_board[x_axis][y_axis] = button
    return new_board

def games_to_play_selected():
    """This function will show the board, message, buttons and score boxes once the maximum score has been chosen from the combobox."""
    board.visible = True
    message.visible = True
    buttons_box.visible = True
    score_box.visible = True

def choose_square(x_axis,y_axis):
    """This function will perform actions on a selected square (button) when a player selects one."""    
    board_squares[x_axis][y_axis].text = turn
    board_squares[x_axis][y_axis].text_color = "red"
    while games_to_play_menu.enabled == True:
        games_to_play_menu.enabled = False
    board_squares[x_axis][y_axis].disable()
    toggle_player()
    check_win()

def toggle_player():
    """This function cycles through the two players so once one has a turn, the other player goes next."""
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X" 
    message.value = "It is your turn, " + turn

def check_win():
    """This function will check the current state of the game and determine is a round has been won or drawn. It will also check if there is an overall winner 
    by checking the players scores to see if it matches the score to get to and if matched, declare that player the winner"""
    global x_score
    global o_score
    #global display_x_score
    winner = None
    
    # check vertical lines for a winner:
    if (board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text) and board_squares[0][2].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (board_squares[1][0].text == board_squares[1][1].text == board_squares[1][2].text) and board_squares[1][2].text in ["X", "O"]:
        winner = board_squares[1][0]
    elif (board_squares[2][0].text == board_squares[2][1].text == board_squares[2][2].text) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[2][0]
    # check horizontal lines for a winner:
    elif (board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text) and board_squares[2][0].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text) and board_squares[2][1].text in ["X", "O"]:
        winner = board_squares[0][1]
    elif (board_squares[0][2].text == board_squares[1][2].text == board_squares[2][2].text) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][2]
    # check diagonal lines for a winner:
    elif (board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif (board_squares[0][2].text == board_squares[1][1].text == board_squares[2][0].text) and board_squares[2][0].text in ["X", "O"]:
        winner = board_squares[0][2]   
    
    # Check for a winner of either the round or the game:
    if winner is not None:
        message.value = winner.text + " wins!"
        reset_button.enabled = True
        if message.value == "X wins!":
            x_score += 1
            display_x_score.value = "X: " + str(x_score)
            board.enabled = False
            if x_score == int(games_to_play_menu.value):
                message.value = "X is the champ!"
                message.text_color = "#42f54b"
                reset_button.enabled = False
        elif message.value == "O wins!":
            o_score += 1
            display_o_score.value = "O: " + str(o_score)
            board.enabled = False
            if o_score == int(games_to_play_menu.value):
                message.value = "O is the champ!"
                message.text_color = "#00d9ff"
                reset_button.enabled = False
    elif moves_taken() == 9:
        message.value = "It's a draw!"
        reset_button.enabled = True

def moves_taken():
    """This function tracks the number of moves taken. It is mainly used to check for a drawn game."""
    moves = 0
    for row in board_squares:
        for col in row:
            if col.text == "X" or col.text == "O":
                moves = moves + 1
    return moves

def reset_game():
    """This function resets the board for a new round."""
    message.value = "It is your turn, " + turn
    reset_button.enabled = False
    global board_squares
    board.enabled = True
    board_squares = clear_board()

def start_over_again():
    """This function is used to restart the entire game. It clears the scores, resets the board, hides the board, message, buttons and score boxes.
    It also re-enables the combobox to allow the players to select a score to reach."""
    global board_squares
    global x_score
    global o_score
    x_score = 0
    display_x_score.value = "O: " + str(x_score)
    o_score = 0
    display_o_score.value = "O: " + str(o_score)
    board.enabled = True
    board_squares = clear_board()
    message.value = "It is your turn, " + turn
    message.text_color = "white"
    games_to_play_menu.enabled = True
    board.visible = False
    message.visible = False
    buttons_box.visible = False
    score_box.visible = False

def starting_turn():
    """This function will generate a random (0 or 1) number and return either an X or a O"""
    turn_id = random.randint(0,1)
    if turn_id == 0:
        return "X"
    else:
        return "O"


# --- Variables area --- #

turn = starting_turn()
x_score = 0
o_score = 0


# --- Application and GUI area --- #

# --- This section is the initial window settings for the application:
app = App("Tic-Tac-Toe", width = 350, height = 450)
app.tk.resizable(False,False)
app.text_color = "white"
app.bg = "black"
app.text_size = 24

# --- This section is used to display the title of the game in the main window:
title = Text(app, text = "Let's Play ... Tic-Tac-Toe", width = "fill", height = "1")

# --- This section is used to display the score to reach to be deemed the winner:
games_to_play_box = Box(app, layout = "grid")
games_to_play_box.text_color = "white"
games_to_play_box.text_size = 20
games_to_play_text_before_choice = Text(games_to_play_box, text = "First Player To:", grid = [0,0], height= "2")
games_to_play_menu = Combo(games_to_play_box, options = [2,3,4,5], grid = [1,0], selected = "None", command = games_to_play_selected)
games_to_play_text_after_choice = Text(games_to_play_box, text = "Wins!", grid = [2,0])


# --- This section is used to contain the nine buttons the players can choose for their moves:
board = Box(app, layout="grid")
board_squares = clear_board()


# --- This section will display a message with either the players turn or a winner / drawn game:
message = Text(app, width = "350", height = "2", text=f"It is your turn, {turn}")


# --- This section will be used to display two buttons. One to play another game and the second button to start over and reset everything:
buttons_box = Box(app, layout = "grid")
buttons_box.text_size = 20
buttons_box.text_color = "black"
reset_button = PushButton(buttons_box, command = reset_game, text = "Play Again", enabled = False, grid = [0,0])
reset_button.text_color = "red"
start_over = PushButton(buttons_box, command = start_over_again, text = "Start Over", enabled = True, grid = [1,0])


# --- This section is used to display the players scores:
score_box = Box(app, width = "350", align = "bottom", layout = "grid")
display_x_score = Text(score_box, text="X: " + str(x_score), align = "left", grid = [0,0])
display_x_score.text_color = "#42f54b"
score_message = Text(score_box, text = "Scores", grid = [1,0], width = 13)
display_o_score = Text(score_box, text="O: " + str(o_score), align = "right", grid=[2,0])
display_o_score.text_color = "#00d9ff"

# --- This section is used to hide the board, message, buttons and score boxes until a selection is made from the games_to_play_menu combobox:
board.visible = False
message.visible = False
buttons_box.visible = False
score_box.visible = False


# --- This will start the application:
app.display()