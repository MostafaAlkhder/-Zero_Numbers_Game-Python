from GetInput import GetInput
from LinkedList import LinkedList
from NextStates import NextStates
from NextStates import AStarNextStates
from queue import Queue
from State import State
from Path import Path
from queue import PriorityQueue
import heapq
from dataclasses import dataclass, field
from typing import Any


class AStar:
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
        self.queue.put((7, self.state))
        self.counter = 0
        while (not self.queue.empty()):
            current_State = self.queue.get()[1]
            if current_State.Cheak_is_win_game():
                self.counter = len(self.visited)
                return current_State
            elif current_State.Cheak_is_lose_state():
                # self.queue.get()
                # self.visited.remove(current_State.matrix)
                continue
            else:
                self.visited.append(current_State.matrix)
                next_state_list = AStarNextStates(
                    current_State).getPossibleNextStates()
                for l in next_state_list:
                    if not self.Is_Visited(l.value.matrix):
                        self.queue.put((1, l.value))
