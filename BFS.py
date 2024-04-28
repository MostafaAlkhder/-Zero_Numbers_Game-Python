from GetInput import GetInput
from LinkedList import LinkedList
from NextStates import NextStates
from queue import Queue
from State import State
from Path import Path
import numpy as np


class BFS:
    def __init__(self, state):
        self.nextStates = NextStates(state)
        self.queue = Queue()
        self.visited = LinkedList()
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

    def Is_Visited(self, matrix):
        if self.visited.head == self.visited.tail:
            return False
        equal = True
        for v in self.visited:
            equal = True
            for i in range(len(v.value)):
                for j in range(len(v.value[0])):
                    if matrix[i][j] != v.value[i][j]:
                        equal = False
                        break
            if not equal:
                break
            if equal:
                return equal

        return equal

    def Search(self):
        self.queue.put(self.state)
        self.counter = 0
        while (not self.queue.empty()):
            current_State = self.queue.get()
            if current_State.Cheak_is_win_game():
                self.counter = self.visited.__len__()
                return current_State
            elif current_State.Cheak_is_lose_state():
                # self.queue.get()
                continue
            else:
                self.visited.add_node(current_State.matrix)
                next_state_list = NextStates(
                    current_State).getPossibleNextStates()
                for l in next_state_list:
                    if not self.Is_Visited(l.value.matrix):
                        self.queue.put(l.value)
