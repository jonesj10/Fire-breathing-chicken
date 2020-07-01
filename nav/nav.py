from random import *
import time
import numpy as np
import matplotlib as mpl

grid = []
#Create a 10x10 grid
for row in range(10):
    grid.append([])
    for col in range(10):
        grid[row].append("0")
        
gridshow = []        
for rowshow in range(10):
    gridshow.append([])
    for colshow in range(10):
        gridshow[rowshow].append("?")

# makes trees
for trees in range(25):
    c_x = randint(0, len(grid)-1)
    c_y = randint(0, len(grid[0])-1)
    while c_x == 7 and c_y == 0:
           c_x = randint(0, len(grid)-1)
           c_y = randint(0, len(grid[0])-1)
    else:
        grid[c_x][c_y] = "T"
    grid[9][9] = "0"
    grid[0][0] = "R"
    gridshow[0][0] = "R"


for row in grid:
    print(" ".join(str(row)))


#locations
i = 0
j = 0
#past locations
i0 = 0
j0 = 0
lstmv = 0


while grid[9][9]!="R":
    #mv shows if the bot moved this cycle mv is usen instead of elif to prevent out-of-bounds errors
    mv = 0
    if(j!=9):
        if(grid[i][j+1] == "0"):
            j0 = j
            j= j+1
            grid[i][j0] = "B"
            gridshow[i][j0] = "B"
            lstmv = "+j"
            mv=1

    if(i!=9):
        if(grid[i+1][j] == "0" and mv==0):
            i0 = i
            i = i+1
            grid[i0][j] = "B"
            gridshow[i0][j] = "B"
            lstmv = "+i"
            mv=1

# change route after backtracking
    if(i != 9 and j != 9 and mv == 0 and i != 0 and j != 0):
        if ((grid[i+1][j]=="T" or grid[i+1][j]=="B") and (grid[i][j+1]=="T" or grid[i][j+1]=="B") and grid[i][j-1]=="0"):

            j0 = j
            j= j-1
            grid[i][j0] = "B"
            gridshow[i][j0] = "B"
            lstmv = "-j"
            mv=1

        if ((grid[i+1][j]=="T" or grid[i+1][j]=="B") and (grid[i][j+1]=="T" or grid[i][j+1]=="B") and grid[i-1][j]=="0" and mv == 0):

            i0 = i
            i = i-1
            grid[i0][j] = "B"
            gridshow[i0][j] = "B"
            lstmv = "-i"
            mv=1
    if(i == 9 and j != 9 and mv == 0 and i != 0 and j != 0):
        if((grid[i][j+1] == "T" or grid[i][j+1] == "B") and (grid[i][j-1] == "T" or grid[i][j-1] == "B") and grid[i-1][j] == "0"):
            i0 = i
            i = i-1
            grid[i0][j] = "B"
            gridshow[i0][j] = "B"
            lstmv = "-i"
            mv=1




#backtracking code
    if(i!=9 and j!=9 and mv == 0):
        if(grid[i+1][j]=="T" and grid[i][j+1]=="T" and mv == 0):
            if (lstmv == "+i"):
                i0 = i
                i = i-1
                grid[i0][j] = "B"
                gridshow[i0][j] = "B"
            if (lstmv =="+j"):
                j0 = j
                j = j-1
                grid[i][j0] = "B"
                gridshow[i][j0] = "B"

    if(i==9 and j!= 9 and mv == 0):
        if (lstmv == "+i"):
            i0 = i
            i = i-1
            grid[i0][j] = "B"
            gridshow[i0][j] = "B"
        if (lstmv =="+j"):
            j0 = j
            j = j-1
            grid[i][j0] = "B"
            gridshow[i][j0] = "B"

    if(i!=9 and j == 9 and mv==0):
        if (lstmv == "+i"):
            i0 = i 
            i = i-1 
            grid[i0][j] = "B"
            gridshow[i0][j] = "B"

        elif (lstmv =="+j"):
            j0 = j 
            j = j-1 
            grid[i][j0] = "B"
            gridshow[i][j0] = "B"
        


#data from surroundings
    if(i == 0 and j == 0):
        gridshow[i+1][j] = grid[i+1][j]
        gridshow[i+1][j+1] = grid[i+1][j+1]
        gridshow[i][j+1] = grid[i][j+1]
    elif(i == 9 and j == 9):
        print("\nDone\n")
    elif(i == 0 and j != 9):
        gridshow[i+1][j] = grid[i+1][j]
        gridshow[i+1][j+1] = grid[i+1][j+1]
        gridshow[i][j+1] = grid[i][j+1]
        gridshow[i+1][j-1] = grid[i+1][j-1]
        gridshow[i][j-1] = grid[i][j-1]
    elif(i != 9 and j == 0):
        gridshow[i+1][j] = grid[i+1][j]
        gridshow[i+1][j+1] = grid[i+1][j+1]
        gridshow[i][j+1] = grid[i][j+1]
        gridshow[i-1][j+1] = grid[i-1][j+1]
        gridshow[i-1][j] = grid[i-1][j]
    elif(i == 0 and j == 9):
        gridshow[i+1][j] = grid[i+1][j]
        gridshow[i+1][j-1] = grid[i+1][j-1]
        gridshow[i][j-1] = grid[i][j-1]
    elif(i == 9 and j == 0):
        gridshow[i-1][j] = grid[i-1][j]
        gridshow[i-1][j+1] = grid[i-1][j+1]
        gridshow[i][j+1] = grid[i][j+1]
    elif(i == 9):
        gridshow[i-1][j] = grid[i-1][j]
        gridshow[i-1][j+1] = grid[i-1][j+1]
        gridshow[i][j+1] = grid[i][j+1]
        gridshow[i][j-1] = grid[i][j-1]
        gridshow[i-1][j-1] = grid[i-1][j-1]
    elif(j == 9):
        gridshow[i+1][j] = grid[i+1][j]
        gridshow[i+1][j-1] = grid[i+1][j-1]
        gridshow[i][j-1] = grid[i][j-1] 
        gridshow[i-1][j-1] = grid[i-1][j-1]
        gridshow[i-1][j] = grid[i-1][j]
    else:
        gridshow[i+1][j] = grid[i+1][j]
        gridshow[i+1][j+1] = grid[i+1][j+1]
        gridshow[i][j+1] = grid[i][j+1]
        gridshow[i-1][j+1] = grid[i-1][j+1]
        gridshow[i-1][j] = grid[i-1][j]
        gridshow[i-1][j-1] = grid[i-1][j-1]
        gridshow[i][j-1] = grid[i][j-1]
        gridshow[i+1][j-1] = grid[i+1][j-1]





    grid[i][j] = "R"
    gridshow[i][j] = "R"



    print("\n------------------------------------------------------------------------------------\n")
    print("i = "+str(i)+" j = "+str(j))
    print("\n------------------------------------------------------------------------------------\n")
    for rowshow in gridshow:
        print(" ".join(str(rowshow)))
    time.sleep(.500)



print("\n------------------------------------------------------------------------------------\n")
print("DONE")
print("\n------------------------------------------------------------------------------------\n")


for row in grid:
    print(" ".join(str(row)))

