from random import *
import time
import numpy as np


def gridmake(size, trees):
    grid = []
#Create a 10x10 grid
    for row in range(size):
        grid.append([])
        for col in range(size):
            grid[row].append("0")
        

# makes trees
    for trees in range(25):
        c_x = randint(0, len(grid)-1 )
        c_y = randint(0, len(grid) -1 )
        grid[c_x][c_y] = "T"
        grid[size -1][size-1] = "0"
        grid[0][0] = "R"



    return grid

def movement(desti, destj, grid, gridshow):

    f = open("location.txt", "w")
    
#locations
    i = 0
    j = 0
#past locations
    i0 = 0
    j0 = 0
    lstmv = 0
    lim = len(grid)-1


    print("\n "+ str(lim) + "\n ")

    for row in grid:
        print(" ".join(str(row)))
        f.write(" ".join(str(row)) + "<br/>")


    while grid[9][9]!="R":
    #mv shows if the bot moved this cycle mv is usen instead of elif to prevent out-of-bounds errors
        mv = 0
        if(j!= lim):
            if(grid[i][j+1] == "0"):
                j0 = j
                j= j+1
                grid[i][j0] = "B"
                gridshow[i][j0] = "B"
                lstmv = "+j"
                mv=1

        if(i!=lim):
            if(grid[i+1][j] == "0" and mv==0):
                i0 = i
                i = i+1
                grid[i0][j] = "B"
                gridshow[i0][j] = "B"
                lstmv = "+i"
                mv=1
        if(j == lim and mv == 0):
            if(grid[i+1][j] == "T" or grid[i+1][j] == "B" and grid[i-1][j] == "0" or grid[i-1][j] == "B"):
                j0 = j
                j = j-1
                grid[i][j0] = "B"
                gridshow[i][j0] = "B"
                lstmv = "-j"
                mv=1



        if(i == lim and mv == 0):
            if(grid[i][j+1] == "0" or grid[i][j+1] == "B" and grid[i][j-1] == "0"):
                i0 = i
                i = i-1
                grid[i0][j] = "B"
                gridshow[i0][j] = "B"
                lstmv = "-i"
                mv=1


# change route after backtracking
        if(i != lim and j != lim and mv == 0 and i != 0 and j != 0):
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
        if(i == lim and j != lim and mv == 0 and i != 0 and j != 0):
            if((grid[i][j+1] == "T" or grid[i][j+1] == "B") and (grid[i][j-1] == "T" or grid[i][j-1] == "B") and grid[i-1][j] == "0"):
                i0 = i
                i = i-1
                grid[i0][j] = "B"
                gridshow[i0][j] = "B"
                lstmv = "-i"
                mv=1




#backtracking code
        if(i!=lim and j!=lim and mv == 0):
            if(grid[i+1][j]=="T" and grid[i][j+1]=="T" and mv == 0):
                if (lstmv == "+i"):
                    i0 = i
                    i = i-1
                    grid[i0][j] = "B"
                    gridshow[i0][j] = "B"
                    mv = 1
                if (lstmv =="+j"):
                    j0 = j
                    j = j-1
                    grid[i][j0] = "B"
                    gridshow[i][j0] = "B"
                    mv = 1

        if(i==lim and j!= lim and mv == 0):
            if (lstmv == "+i"):
                i0 = i
                i = i-1
                grid[i0][j] = "B"
                gridshow[i0][j] = "B"
                mv = 1
            if (lstmv =="+j" and j != 0):
                j0 = j
                j = j-1
                grid[i][j0] = "B"
                gridshow[i][j0] = "B"
                mv =1

        if(i!=lim and j == lim and mv==0):
            if (lstmv == "+i" and i != 0):
                i0 = i 
                i = i-1 
                grid[i0][j] = "B"
                gridshow[i0][j] = "B"
                mv =1

            elif (lstmv =="+j"):
                j0 = j 
                j = j-1 
                grid[i][j0] = "B"
                gridshow[i][j0] = "B"
                mv=1
        


#data from surroundings
        if(i == 0 and j == 0):
            gridshow[i+1][j] = grid[i+1][j]
            gridshow[i+1][j+1] = grid[i+1][j+1]
            gridshow[i][j+1] = grid[i][j+1]
        elif(i == lim and j == lim):
            print("\nDone\n")
        elif(i == 0 and j != lim):
            gridshow[i+1][j] = grid[i+1][j]
            gridshow[i+1][j+1] = grid[i+1][j+1]
            gridshow[i][j+1] = grid[i][j+1]
            gridshow[i+1][j-1] = grid[i+1][j-1]
            gridshow[i][j-1] = grid[i][j-1]
        elif(i != lim and j == 0):
            gridshow[i+1][j] = grid[i+1][j]
            gridshow[i+1][j+1] = grid[i+1][j+1]
            gridshow[i][j+1] = grid[i][j+1]
            gridshow[i-1][j+1] = grid[i-1][j+1]
            gridshow[i-1][j] = grid[i-1][j]
        elif(i == 0 and j == lim):
            gridshow[i+1][j] = grid[i+1][j]
            gridshow[i+1][j-1] = grid[i+1][j-1]
            gridshow[i][j-1] = grid[i][j-1]
        elif(i == lim and j == 0):
            gridshow[i-1][j] = grid[i-1][j]
            gridshow[i-1][j+1] = grid[i-1][j+1]
            gridshow[i][j+1] = grid[i][j+1]
        elif(i == lim):
            gridshow[i-1][j] = grid[i-1][j]
            gridshow[i-1][j+1] = grid[i-1][j+1]
            gridshow[i][j+1] = grid[i][j+1]
            gridshow[i][j-1] = grid[i][j-1]
            gridshow[i-1][j-1] = grid[i-1][j-1]
        elif(j == lim):
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
            f.write(" ".join(str(rowshow)) + "<br/>")

        f.write("<br/>------------------------------------------------------------------------------------------------<br/>")


    print("\n------------------------------------------------------------------------------------\n")
    print("DONE")
    print("\n------------------------------------------------------------------------------------\n")


    for row in grid:
        print(" ".join(str(row)))
    return gridshow


gridshow = []
for rowshow in range(10):
    gridshow.append([])
    for colshow in range(10):
        gridshow[rowshow].append("?")

gridshow[0][0] = "R"


grid = gridmake(10,3)
movement(9,9, grid, gridshow)
