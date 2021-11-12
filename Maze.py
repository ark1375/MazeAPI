## Randomized depth-fist-search
### Itterative implementation
# [external link](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

import random

class Maze():
    
    def __init__(self, width = 500 , height = 500):

        self.width = width
        self.height = height

        self._maze = [ [0b10000]*width ] * height
    



    @staticmethod   
    def createRandomMaze_RDFS(width = 500 , height = 500):
        
        stack = []
        maze = []

        for _ in range(height + 2):
            maze.append([0b00000] * (width + 2))

        maze[0] =  [0b11111] * (width + 2) 
        maze[height + 1] =  [0b11111] * (width + 2) 

        for i in range(height + 1):
            maze[i][0] = 0b11111
            maze[i][width + 1] = 0b11111

        init_x , init_y = random.randrange(1,width) , random.randrange(1,height) ## Choose the initial cell, mark it as visited and push it to the stack

        maze[init_x][init_y] = maze[init_x][init_y] | 0b10000   ## mark as visited
        print(maze[init_x][init_y])

        stack.append((init_x , init_y)) 

        while(stack):   ## While the stack is not empty

            cur_x , cur_y = stack.pop() ## Pop a cell from the stack and make it a current cell
            # print(cur_x , cur_y)
            
            visiting_neighbours = [0,1,2,3]
            random.shuffle(visiting_neighbours)

            for arrow in visiting_neighbours:

                # Check North
                if arrow == 0:
                    check_x , check_y = cur_x , cur_y - 1
                
                # Check East
                elif arrow == 1: 
                    check_x , check_y = cur_x + 1, cur_y

                # Check South
                elif arrow == 2: 
                    check_x , check_y = cur_x, cur_y + 1
                
                # Check West
                else: 
                    check_x , check_y = cur_x - 1, cur_y
                
                if maze[check_x][check_y] & 0b10000 == 0b00000:
                    stack.append( (cur_x,cur_y) )
                    
                    maze[cur_x][cur_y] |= 2**arrow 
                    maze[check_x][check_y] |= 2 ** ( (arrow + 2) % 4)

                    maze[check_x][check_y] |= 0b10000
                    stack.append((check_x , check_y))
                    break

        return maze


maze = Maze.createRandomMaze_RDFS(width=20 , height= 20)
# for m in maze:
#     for i in range(len(m)):
#         m[i] -= 0b10000
#     print(m)


import turtle

screen = turtle.getscreen()

sc_x , sc_y = 400 , 400

screen.setup(500,500, 3000, 400)

screen.bgcolor('black')

turtle = turtle.getturtle()

turtle.pencolor('white')
turtle.speed(10)
turtle.pensize(5)

# cord_x , cord_y = random.randint(1,19) , random.randint(1,19)
cord_x , cord_y = 1 , 1
maze_cop = maze.copy()

stack =[]

stack.append((cord_x,cord_y))

c_r , c_g , c_b = 0 , 0 , 255

while stack:
    # stack.reverse()
    cur_x , cur_y = stack.pop()
    # stack.reverse()
    visiting_neighbours = [0,1,2,3]
    # random.shuffle(visiting_neighbours)
    for arrow in visiting_neighbours:

        # Check North
        if arrow == 0:
            check_x , check_y = cur_x , cur_y - 1
        
        # Check East
        elif arrow == 1: 
            check_x , check_y = cur_x + 1, cur_y

        # Check South
        elif arrow == 2: 
            check_x , check_y = cur_x, cur_y + 1
        
        # Check West
        else: 
            check_x , check_y = cur_x - 1, cur_y
        
        if maze[cur_x][cur_y] & (2**arrow) == (2**arrow):
            
            maze[cur_x][cur_y] &= ~(2**arrow)
            maze[check_x][check_y] &= ~(2 ** ( (arrow + 2) % 4))

            stack.append((check_x , check_y))
            screen.colormode(255)

            turtle.pencolor((c_r , c_g , c_b))
            turtle.pensize(10)
 
            turtle.penup()
            turtle.setx( ((cur_x - 1)*20) - 200 )
            turtle.sety( ((cur_y - 1)*20) - 200 )
            
            
            turtle.pendown()
            turtle.goto((((check_x - 1)*20) - 200 , ((check_y - 1)*20) - 200 ))
            # break

    step = 1
    if c_b == 0 and c_r != 0:
        c_g += step
        c_r -= step
    
    elif c_g == 0 and c_b != 0:
        c_b -= step
        c_r += step  

    elif c_r == 0 and c_g != 0:
        c_g -= step
        c_b += step


    

            







screen.exitonclick()