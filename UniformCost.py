from LinkedList import LinkedList
from NextStates import NextStates
from NextStates import UniformCostNextStates

from NextStates import HillClimpingNextStates
from queue import PriorityQueue
# from State import HillClimpingState
# from State import AStarState
# from State import UniformState
# from GetInput import GetInput
# from State import State
# from State import HillClimpingState
# from State import AStarState
# from State import UniformState
# from Path import Path
# from DFS import DFS
# from BFS import BFS
# from HillClimping import HillClimping
# from AStar import AStar


class UniformCost:
    def __init__(self, state):
        self.nextStates = NextStates(state)
        self.queue = PriorityQueue()
        self.visited = []
        self.state = state
        self.counter = 0
    # def Is_Visited(self, matrix):
    #     if self.visited.head == self.visited.tail == None:
    #         return False
    #     equal = True
    #     for v in self.visited:
    #         equal = True
    #         for i in matrix:
    #             for j in v.value:
    #                 if i != j:
    #                     equal = False
    #                     break
    #         if equal:
    #             return equal
    #     return equal

    # def Is_Visited(self, matrix):
    #     if self.visited.head == self.visited.tail:
    #         return False
    #     equal = True
    #     for v in self.visited:
    #         equal = True
    #         for i in range(len(v.value)):
    #             for j in range(len(v.value[0])):
    #                 if matrix[i][j] != v.value[i][j]:
    #                     equal = False
    #                     break
    #         if not equal:
    #             break
    #         if equal:
    #             return equal

    #     return equal

    def Is_Visited(self, matrix):
        if matrix in self.visited:
            return True
        return False

    def Search(self):
        self.counter = 0
        self.queue.put((7, self.state))
        current_State = self.state
        while (not self.queue.empty()):
            current_State = self.queue.get()[1]
            if current_State.Cheak_is_win_game():
                self.counter = len(self.visited)
                return current_State
            elif current_State.Cheak_is_lose_state():
                # self.queue.get()
                continue
            else:
                self.visited.append(current_State.matrix)
                next_state_list = UniformCostNextStates(
                    current_State).getPossibleNextStates()
                for l in next_state_list:
                    # if not self.Is_Visited(l.value.matrix):
                    if not l.value.matrix in self.visited:
                        self.queue.put((1, l.value))


# To Get The Input
# Input = GetInput()
# Input.GetFromFile("1")
# matrix = Input.matrix
# state = State(matrix)

# # Print The Main State
# print(" -- This Is Main Game -- ")
# print()
# state.Print_matrix()
# print()


# # UniformCost
# uniformState = UniformState(matrix)
# uniformCost = UniformCost(uniformState)
# print("-"*40)
# final_state = uniformCost.Search()
# print("-"*40)
# print("----------- The Algorithem UniformCost -----------")
# print("-"*40)
# # path = Path(final_state)
# # # pathCounter = path.Print_Path()
# # # print(f"UniformCost Takes {pathCounter} Moves To Solve This Game")
# # print(f"UniformCost Takes {path.GetCounter()} Moves To Solve This Game")
# print(f"UniformCost Needs {uniformCost.counter} Nodes To Solve This Game")

# print()
