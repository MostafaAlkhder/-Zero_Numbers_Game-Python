import copy


class State:
    def __init__(self, Orginal_Matrix, Parent=None):
        self.rows = len(Orginal_Matrix)
        self.columns = len(Orginal_Matrix[0])
        self.matrix = copy.deepcopy(Orginal_Matrix)
        self.parent = Parent

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
        # return False

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


class UniformState(State):
    def __init__(self, Orginal_Matrix, Parent=None, g=0):
        self.rows = len(Orginal_Matrix)
        self.columns = len(Orginal_Matrix[0])
        self.matrix = copy.deepcopy(Orginal_Matrix)
        self.parent = Parent
        self.g = g

    def __lt__(self, other):
        return other.g < self.g


class HillClimpingState(State):
    def __init__(self, Orginal_Matrix, Parent=None):
        self.rows = len(Orginal_Matrix)
        self.columns = len(Orginal_Matrix[0])
        self.matrix = copy.deepcopy(Orginal_Matrix)
        self.parent = Parent
        self.h = self.Update_h()

    def __lt__(self, other):
        return self.h < other.h

    def Update_h(self):
        h = 0
        same_cells = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != -1:
                    h += 1
                    if ((self.Cheak_possibility_to_move(i, j, "i") and self.matrix[i-1][j] == self.matrix[i][j]) or (self.Cheak_possibility_to_move(i, j, "k") and self.matrix[i+1][j] == self.matrix[i][j]) or (self.Cheak_possibility_to_move(i, j, "l") and self.matrix[i][j+1] == self.matrix[i][j]) or (self.Cheak_possibility_to_move(i, j, "j") and self.matrix[i][j-1] == self.matrix[i][j])):
                        h -= 1
                        same_cells += 1

        h -= same_cells / 2
        if (h >= 0):
            h -= 1
        return h


class AStarState(State):
    def __init__(self, Orginal_Matrix, Parent=None, g=0):
        self.rows = len(Orginal_Matrix)
        self.columns = len(Orginal_Matrix[0])
        self.matrix = copy.deepcopy(Orginal_Matrix)
        self.parent = Parent
        self.g = g
        self.h = self.Update_h()

    def __lt__(self, other):
        return other.h + other.g < self.h + self.g

    def Update_h(self):
        h = 0
        same_cells = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.matrix[i][j] != -1:
                    h += 1
                    if ((self.Cheak_possibility_to_move(i, j, "i") and self.matrix[i-1][j] == self.matrix[i][j]) or (self.Cheak_possibility_to_move(i, j, "k") and self.matrix[i+1][j] == self.matrix[i][j]) or (self.Cheak_possibility_to_move(i, j, "l") and self.matrix[i][j+1] == self.matrix[i][j]) or (self.Cheak_possibility_to_move(i, j, "j") and self.matrix[i][j-1] == self.matrix[i][j])):
                        h -= 1
                        same_cells += 1

        h -= same_cells / 2
        return h
