from GetInput import GetInput
from LinkedList import LinkedList
from NextStates import NextStates
from Stack import Stack
from State import State
from Path import Path


class DFS:
    def __init__(self, state):
        self.nextStates = NextStates(state)
        self.stack = Stack()
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
        self.stack.push(self.state)
        self.counter = 0
        while (not self.stack.isEmpty()):
            current_State = self.stack.pop()
            if current_State.Cheak_is_win_game():
                self.counter = len(self.visited)
                return current_State
            elif current_State.Cheak_is_lose_state():
                # self.stack.pop()
                continue
            else:
                # self.visited.add(current_State.matrix)
                self.visited.append(current_State.matrix)
                next_state_list = NextStates(
                    current_State).getPossibleNextStates()
                for l in next_state_list:
                    # if not self.Is_Visited(l.value.matrix):
                    if not l.value.matrix in self.visited:
                        self.stack.push(l.value)
