import keyboard
from copy import deepcopy 
from time import sleep 
from random import randint 

MAP = {
    1 :['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
    2 :['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    3 :['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    4 :['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    5 :['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    6 :['0',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    7 :['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    8 :['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    9 :['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    10:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    11:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    12:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    13:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    14:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    15:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    16:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    17:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    18:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    19:['0',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','0',],
    20:['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',]
}

class direction():

    def __init__(self):
        self.x = 0
        self.y = 0 

class Main():

    def __init__(self):

        self.direction = direction()
        self.direction.y = 1 

        self.MAP = deepcopy(MAP)

        self.foodFlag = True 

        self.SCORE = 0

        self.TAIL = []
        self.SNAKE = []
        self.FOOD = []


        self.gameOver = False 

    def mapControl(self):

        self.FLAG = True 
        
        for ROW in self.MAP:
            for COLUMN in range(len(self.MAP)):

                if self.MAP[ROW][COLUMN] == 'X': # search the snake head because we want the change position
                    
                    self.TAIL.append([COLUMN,ROW]) # follow the trace 

                    self.SNAKE.clear()
                    self.SNAKE.append([COLUMN,ROW])

                    if ROW in [1,20] or COLUMN in [1,19] or self.TAIL.count([COLUMN,ROW])==3: # This are walls if snake going into walls game is done 
                        self.FLAG = False
                        self.gameOver = True 

                    if [COLUMN,ROW]  == self.FOOD:
                        self.foodFlag = True 

                    if self.direction.x != 0 and self.FLAG: # means the snake is going the x direction

                        self.MAP[ROW].pop(COLUMN) # delete the old position head
                        self.MAP[ROW].insert(COLUMN,' ')

                        self.MAP[ROW].pop(COLUMN)  # then make a new position head
                        self.MAP[ROW].insert(COLUMN+self.direction.x,'X') 

                    if self.direction.y != 0 and self.FLAG:

                        self.MAP[ROW].pop(COLUMN) # delete the old position head       
                        self.MAP[ROW].insert(COLUMN,' ') 

                        self.MAP[ROW+self.direction.y].pop(COLUMN)  # then make a new position head
                        self.MAP[ROW+self.direction.y].insert(COLUMN,'X')

                    self.FLAG = False 

    def food_create(self):

        while True:
            
            ROW = randint(2,18) # food y position choose 
            COLUMN = randint(2,18) # food x position choose 
            if self.SNAKE != [COLUMN,ROW] and [COLUMN,ROW] not in self.TAIL:
                self.FOOD=[COLUMN,ROW]
                break

        self.MAP[ROW].pop(COLUMN)
        self.MAP[ROW].insert(COLUMN,'$')

        self.foodFlag=False
        self.SCORE += 1 


    def tailMaker(self):

        while len(self.TAIL) > self.SCORE: 
            self.TAIL.pop(0)

        for POS in self.TAIL: # Make the tail 
            for ROW in self.MAP:
                for COLUMN in range(len(self.MAP[ROW])):
                    
                    if [COLUMN,ROW] == [POS[0],POS[1]] and self.MAP[ROW][COLUMN] != 'X':
                        self.MAP[ROW].pop(COLUMN) 
                        self.MAP[ROW].insert(COLUMN,'O')

        for ROW in self.MAP: # clean the old tail 
            for COLUMN in range(len(self.MAP[ROW])):
                 
                if self.MAP[ROW][COLUMN] == 'O':
                    if [COLUMN,ROW] not in self.TAIL:
                        self.MAP[ROW].pop(COLUMN)
                        self.MAP[ROW].insert(COLUMN,' ')

    def draw(self):

        for ROW in self.MAP:
            column = ""
            for COLUMN in range(len(self.MAP)):

                if ROW in [1,20]:
                    if COLUMN != 19:
                        column += self.MAP[ROW][COLUMN] + "0"
                    else:
                        column += self.MAP[ROW][COLUMN]
                else:
                    column += self.MAP[ROW][COLUMN] + " "

            print(column)

    def input(self):

        if keyboard.is_pressed('w') and self.direction.x != 0:
            self.direction.y = -1
            self.direction.x =  0
        elif keyboard.is_pressed('s') and self.direction.x != 0:
            self.direction.y = 1
            self.direction.x = 0
        elif keyboard.is_pressed('a') and self.direction.y != 0:
            self.direction.x = -1
            self.direction.y =  0
        elif keyboard.is_pressed('d') and self.direction.y != 0:
            self.direction.x = 1
            self.direction.y = 0

    def run(self):

        self.input()
        self.mapControl()
        self.tailMaker()

        if self.foodFlag: # create the food and kill the foodFlag
            self.food_create()

        self.draw()

        if self.gameOver:
            self.SCORE = 0
            self.gameOver = False 
            self.MAP = deepcopy(MAP)
            self.foodFlag = True 

main = Main()

while True:
    sleep(0.125)
    main.run()
