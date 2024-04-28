from GetInput import GetInput
from State import State
from NextStates import NextStates

Input = GetInput()
Input.GetFromFile("4")
state = State(Input.matrix)

state.Print_matrix()

next_state = NextStates(state)
next_state.getPossibleNextStates()
next_state.printStatesInList()
