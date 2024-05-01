from LinkedList import LinkedList
from ZeroNumbers import ZeroNumbers
# from NextStates import NextStates
from GetInput import GetInput
from State import State
from State import HillClimpingState
from State import AStarState
from State import UniformState


class NextStates:
    def __init__(self, state):
        self.state = state
        self.matrix = state.matrix
        self.game = ZeroNumbers(self.matrix)
        self.list = LinkedList()
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

    def getPossibleNextStates(self):
        parent = self.state
        for i in range(self.rows):
            for j in range(self.columns):
                if (self.state.Cheak_possibility_to_move(i, j, "i")):
                    upState = State(self.matrix, parent)
                    upState.Move(i, j, "i")
                    self.list.add_node(upState)
                if (self.state.Cheak_possibility_to_move(i, j, "k")):
                    downState = State(self.matrix, parent)
                    downState.Move(i, j, "k")
                    self.list.add_node(downState)
                if (self.state.Cheak_possibility_to_move(i, j, "l")):
                    rightState = State(self.matrix, parent)
                    rightState.Move(i, j, "l")
                    self.list.add_node(rightState)
                if (self.state.Cheak_possibility_to_move(i, j, "j")):
                    leftState = State(self.matrix, parent)
                    leftState.Move(i, j, "j")
                    self.list.add_node(leftState)

        return self.list

    def printStatesInList(self):
        n = 1
        for l in self.list:
            print(f'-------------{n}-------------')
            n += 1
            for i in range(self.rows):
                for j in range(self.columns):
                    if l.value.matrix[i][j] == -1:
                        print("**", end=" ")
                    elif l.value.matrix[i][j] < 10:
                        print(f'0{l.value.matrix[i][j]}', end=" ")
                    else:
                        print(f'{l.value.matrix[i][j]}', end=" ")
                print()


class UniformCostNextStates(NextStates):
    def getPossibleNextStates(self):
        parent = self.state
        for i in range(self.rows):
            for j in range(self.columns):
                if (self.state.Cheak_possibility_to_move(i, j, "i")):
                    upState = UniformState(self.matrix, parent,
                                           self.state.g + self.matrix[i-1][j])
                    upState.Move(i, j, "i")
                    if not upState.Cheak_is_lose_state():
                        self.list.add_node(upState)
                if (self.state.Cheak_possibility_to_move(i, j, "k")):
                    downState = UniformState(self.matrix, parent,
                                             self.state.g + self.matrix[i+1][j])
                    downState.Move(i, j, "k")
                    if not downState.Cheak_is_lose_state():
                        self.list.add_node(downState)
                if (self.state.Cheak_possibility_to_move(i, j, "l")):
                    rightState = UniformState(self.matrix, parent,
                                              self.state.g + self.matrix[i][j+1])
                    rightState.Move(i, j, "l")
                    if not rightState.Cheak_is_lose_state():
                        self.list.add_node(rightState)
                if (self.state.Cheak_possibility_to_move(i, j, "j")):
                    leftState = UniformState(self.matrix, parent,
                                             self.state.g + self.matrix[i][j-1])
                    leftState.Move(i, j, "j")
                    if not leftState.Cheak_is_lose_state():
                        self.list.add_node(leftState)

        return self.list


class HillClimpingNextStates(NextStates):
    def getPossibleNextStates(self):
        parent = self.state
        for i in range(self.rows):
            for j in range(self.columns):
                if (self.state.Cheak_possibility_to_move(i, j, "i")):
                    upState = HillClimpingState(self.matrix, parent)
                    upState.Move(i, j, "i")
                    if not upState.Cheak_is_lose_state():
                        self.list.add_node(upState)
                if (self.state.Cheak_possibility_to_move(i, j, "k")):
                    downState = HillClimpingState(self.matrix, parent)
                    downState.Move(i, j, "k")
                    if not downState.Cheak_is_lose_state():
                        self.list.add_node(downState)
                if (self.state.Cheak_possibility_to_move(i, j, "l")):
                    rightState = HillClimpingState(self.matrix, parent)
                    rightState.Move(i, j, "l")
                    if not rightState.Cheak_is_lose_state():
                        self.list.add_node(rightState)
                if (self.state.Cheak_possibility_to_move(i, j, "j")):
                    leftState = HillClimpingState(self.matrix, parent)
                    leftState.Move(i, j, "j")
                    if not leftState.Cheak_is_lose_state():
                        self.list.add_node(leftState)

        return self.list


class AStarNextStates(NextStates):
    def getPossibleNextStates(self):
        parent = self.state
        for i in range(self.rows):
            for j in range(self.columns):
                if (self.state.Cheak_possibility_to_move(i, j, "i")):
                    upState = AStarState(self.matrix, parent,
                                         self.state.g + self.matrix[i-1][j])
                    upState.Move(i, j, "i")
                    if not upState.Cheak_is_lose_state():
                        self.list.add_node(upState)
                if (self.state.Cheak_possibility_to_move(i, j, "k")):
                    downState = AStarState(self.matrix, parent,
                                           self.state.g + self.matrix[i+1][j])
                    downState.Move(i, j, "k")
                    if not downState.Cheak_is_lose_state():
                        self.list.add_node(downState)
                if (self.state.Cheak_possibility_to_move(i, j, "l")):
                    rightState = AStarState(self.matrix, parent,
                                            self.state.g + self.matrix[i][j+1])
                    rightState.Move(i, j, "l")
                    if not rightState.Cheak_is_lose_state():
                        self.list.add_node(rightState)
                if (self.state.Cheak_possibility_to_move(i, j, "j")):
                    leftState = AStarState(self.matrix, parent,
                                           self.state.g + self.matrix[i][j-1])
                    leftState.Move(i, j, "j")
                    if not leftState.Cheak_is_lose_state():
                        self.list.add_node(leftState)

        return self.list
