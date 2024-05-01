class ZeroNumbers:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __str__(self):
        return f'Matrix:\n {self.matrix}'

    def Print_matrix(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] == -1:
                    print("**", end=" ")
                elif self.matrix[i][j] < 10:
                    print(f'0{self.matrix[i][j]}', end=" ")
                else:
                    print(f'{self.matrix[i][j]}', end=" ")
            print()
        return False

    def Cheak_possibility_to_move(self, i1, j1, direction):
        i2 = i1
        j2 = j1
        if direction == "l":
            j2 = j1 + 1
        elif direction == "j":
            j2 = j1 - 1
        elif direction == "k":
            i2 = i1 + 1
        elif direction == "i":
            i2 = i1 - 1
        else:
            return False
        if i1 < 0 or i1 >= self.rows or i2 < 0 or i2 >= self.rows or j1 < 0 or j1 >= self.columns or j2 < 0 or j2 >= self.columns:
            return False
        if self.matrix[i1][j1] == -1 or self.matrix[i2][j2] == -1:
            return False
        return True

    def Move(self, i, j, direction):
        if direction == "l":
            if self.matrix[i][j+1] == self.matrix[i][j]:
                self.matrix[i][j+1] = -1
            else:
                self.matrix[i][j+1] = self.matrix[i][j] + self.matrix[i][j+1]

        if direction == "j":
            if self.matrix[i][j-1] == self.matrix[i][j]:
                self.matrix[i][j-1] = -1
            else:
                self.matrix[i][j-1] = self.matrix[i][j] + self.matrix[i][j-1]

        if direction == "k":
            if self.matrix[i+1][j] == self.matrix[i][j]:
                self.matrix[i+1][j] = -1
            else:
                self.matrix[i+1][j] = self.matrix[i][j] + self.matrix[i+1][j]

        if direction == "i":
            if self.matrix[i-1][j] == self.matrix[i][j]:
                self.matrix[i-1][j] = -1
            else:
                self.matrix[i-1][j] = self.matrix[i][j] + self.matrix[i-1][j]

        self.matrix[i][j] = -1

    def Cheak_is_win_game(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != -1:
                    return False
        return True

    def Cheak_is_lose_state(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != -1:
                    if (not self.Cheak_possibility_to_move(i, j, "l") and not self.Cheak_possibility_to_move(i, j, "i") and not self.Cheak_possibility_to_move(i, j, "j") and not self.Cheak_possibility_to_move(i, j, "k")):
                        return True
        return False

    def Cheak_is_final_state(self):
        if (self.Cheak_is_win_game() or self.Cheak_is_lose_state()):
            return True
        return False

    # def Start_game(self):
    #     direction = "q"
    #     while (direction != "z"):
    #         self.Print_matrix()
    #         print("Choose A Cell To Move: ")
    #         row_to_move = int(input()) - 1
    #         column_to_move = int(input()) - 1
    #         direction = input("What Is Your Direction: ")
    #         if not self.Cheak_possibility_to_move(row_to_move, column_to_move, direction):
    #             print("You Can't Move Your Cell .. Please Try Again")
    #             continue
    #         else:
    #             self.Move(row_to_move, column_to_move, direction)
    #         if self.Cheak_is_win_game() == True:
    #             self.Print_matrix()
    #             print("#" * 25)
    #             print("You Won This Game")
    #             print("#" * 25)
    #             direction = "z"
    #         if self.Cheak_is_lose_state() == True:
    #             self.Print_matrix()
    #             print("#" * 25)
    #             print("You Lost This Game")
    #             print("#" * 25)
    #             direction = "z"


# # For input From File
# fileMatrix = []
# with open("level3.txt") as textFile:
#     for line in textFile:
#         ele = [item.strip() for item in line.split(',')]
#         fileMatrix.append(ele)

# # Convert to matrix of numbers
# matrix = []
# for i in range(len(fileMatrix)):		 # A for loop for row entries
#     a = []
#     for j in range(len(fileMatrix[0])):	 # A for loop for column entries
#         a.append(int(fileMatrix[i][j]))
#     matrix.append(a)


# # Playing The Game ..
# my_game = ZeroNumbers(matrix)
# my_game.Start_game()
