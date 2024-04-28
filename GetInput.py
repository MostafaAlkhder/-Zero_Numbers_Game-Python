class GetInput:
    def __init__(self):
        self.matrix = []

    def GetFromUser(self):
        # # A basic code for matrix input from user
        rows = int(input("Enter the number of rows:"))
        columns = int(input("Enter the number of columns:"))
        print("Enter Your Game:")

        # # For user input
        for i in range(rows):		 # A for loop for row entries
            a = []
            for j in range(columns):	 # A for loop for column entries
                a.append(int(input()))
            self.matrix.append(a)

    def GetFromFile(self, level):
        # For input From File
        fileMatrix = []
        with open(f"level{level}.txt") as textFile:
            for line in textFile:
                ele = [item.strip() for item in line.split(',')]
                fileMatrix.append(ele)

        # Convert to matrix of numbers
        matrix = []
        for i in range(len(fileMatrix)):		 # A for loop for row entries
            a = []
            # A for loop for column entries
            for j in range(len(fileMatrix[0])):
                a.append(int(fileMatrix[i][j]))
            self.matrix.append(a)
