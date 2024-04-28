from ZeroNumbers import ZeroNumbers
from GetInput import GetInput

userInput = GetInput()
userInput.GetFromUser()
game = ZeroNumbers(userInput.matrix)
direction = "q"
while (direction != "z"):
    game.Print_matrix()
    print("Choose A Cell To Move: ")
    row_to_move = int(input()) - 1
    column_to_move = int(input()) - 1
    direction = input("What Is Your Direction: ")
    if not game.Cheak_possibility_to_move(row_to_move, column_to_move, direction):
        print("You Can't Move Your Cell .. Please Try Again")
        continue
    else:
        game.Move(row_to_move, column_to_move, direction)
    if game.Cheak_is_win_game() == True:
        game.Print_matrix()
        print("#" * 25)
        print("You Won This Game")
        print("#" * 25)
        direction = "z"
    if game.Cheak_is_lose_state() == True:
        game.Print_matrix()
        print("#" * 25)
        print("You Lost This Game")
        print("#" * 25)
        direction = "z"
