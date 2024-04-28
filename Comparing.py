from GetInput import GetInput
from State import State
from State import HillClimpingState
from State import AStarState
from State import UniformState
from Path import Path
from DFS import DFS
from BFS import BFS
from UniformCost import UniformCost
from HillClimping import HillClimping
from AStar import AStar
# from NewAstar import AStar
# from NewAstar import AStar
from timeit import default_timer as timer


# To Get The Input
Input = GetInput()
Input.GetFromFile("5")
matrix = Input.matrix
state = State(matrix)

# Print The Main State
print(" -- This Is Main Game -- ")
print()
state.Print_matrix()
print()


# DFS
dfs = DFS(state)
start = timer()
final_state = dfs.Search()
end = timer()
print("-"*40)
print("----------- The Algorithem DFS -----------")
print("-"*40)
path = Path(final_state)
pathCounter = path.Print_Path()
print(f"DFS Takes {pathCounter} Depth To Solve This Game")
# print(f"DFS Takes {path.GetCounter()} Moves To Solve This Game")
print(f"DFS Needs {dfs.counter} Nodes To Solve This Game")
print(f"DFS Takes {end - start} Seconds To Solve This Game")

print()

BFS
bfs = BFS(state)
start = timer()
final_state = bfs.Search()
end = timer()
print("-"*40)
print("----------- The Algorithem BFS -----------")
print("-"*40)
path = Path(final_state)
pathCounter = path.Print_Path()
print(f"BFS Takes {pathCounter} Depth To Solve This Game")
# print(f"BFS Takes {path.GetCounter()} Moves To Solve This Game")
print(f"BFS Needs {bfs.counter} Nodes To Solve This Game")
print(f"BFS Takes {end - start} Seconds To Solve This Game")

print()

# UniformCost
uniformState = UniformState(matrix)
uniformCost = UniformCost(uniformState)
start = timer()
final_state = uniformCost.Search()
end = timer()
print("-"*40)
print("----------- The Algorithem UniformCost -----------")
print("-"*40)
path = Path(final_state)
pathCounter = path.Print_Path()
print(f"UniformCost Takes {pathCounter} Depth To Solve This Game")
# print(f"UniformCost Takes {path.GetCounter()} Moves To Solve This Game")
print(f"UniformCost Needs {uniformCost.counter} Nodes To Solve This Game")
print(f"UniformCost Takes {end - start} Seconds To Solve This Game")

print()

# HillClimping
hillClimpingState = HillClimpingState(matrix)
hillClimping = HillClimping(hillClimpingState)
start = timer()
final_state = hillClimping.Search()
end = timer()
print("-"*40)
print("----------- The Algorithem HillClimping -----------")
print("-"*40)
path = Path(final_state)
pathCounter = path.Print_Path()
print(f"HillClimping Takes {end - start} Seconds To Solve This Game")
print(f"HillClimping Takes {pathCounter} Depth To Solve This Game")
# print(f"HillClimping Takes {path.GetCounter()} Moves To Solve This Game")
print(f"HillClimping Needs {hillClimping.counter} Nodes To Solve This Game")

print()

# AStar
aStarState = AStarState(matrix)
aStar = AStar(aStarState)
start = timer()
final_state = aStar.Search()
end = timer()
print("-"*40)
print("----------- The Algorithem AStar -----------")
print("-"*40)
path = Path(final_state)
pathCounter = path.Print_Path()
print(f"AStar Takes {pathCounter} Depth To Solve This Game")
# print(f"AStar Takes {path.GetCounter()} Moves To Solve This Game")
print(f"AStar Needs {aStar.counter} Nodes To Solve This Game")
print(f"AStar Takes {end - start} Seconds To Solve This Game")

print()
