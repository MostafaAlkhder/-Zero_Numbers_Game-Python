from GetInput import GetInput
from LinkedList import LinkedList
from NextStates import NextStates
from Stack import Stack
from State import State


class Path:
    def __init__(self, final_state):
        self.final_state = final_state
        self.path = []
        self.counter = 0

    def Print_Path(self):
        print("The Path Of Solution")
        self.counter = 0
        while (self.final_state != None):
            self.path.append(self.final_state)
            self.final_state = self.final_state.parent

        self.path.reverse()
        for p in self.path:
            self.counter += 1
            print()
            print(f'-------------{self.counter}-------------')
            print()
            p.Print_matrix()
        return self.counter

    def GetCounter(self):
        self.counter = 0
        while (self.final_state != None):
            self.path.append(self.final_state)
            self.final_state = self.final_state.parent
            self.counter += 1
        return self.counter
