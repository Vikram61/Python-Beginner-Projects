import math
import random


class Minesweeper:

    def __init__(self,dim_size=5,num_bombs=5):

        self.dim_size=dim_size
        self.num_bombs=num_bombs

        self.board=self.make_new_board()
        self.assign_values_to_board()
        self.dug=set()  #keep the track of dug locations
    
    def make_new_board(self):
        board=[[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted=0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0,self.dim_size**2-1)
            row= loc//self.dim_size
            col=loc%self.dim_size

            if board[row][col]=='*':
                continue

            board[row][col]='*'
            bombs_planted+=1
        return board
    
    def assign_values_to_board(self):

        for r in range(self.dim_size):

            for c in range(self.dim_size):

                if self.board[r][c]=='*':
                    continue

                self.board[r][c]=self.get_num_neigh_bombs(r,c)
    
    def get_num_neigh_bombs(self,row,col): #to get the neighbouring bombs in the adjacent max of 8 cells of any given cell

        num_bombs=0

        for r in range(max(0,row-1),min(self.dim_size,row+2)):
            for c in range(max(0,col-1),min(self.dim_size,col+2)):

                if r==row and c==col:
                    continue
                if self.board[r][c]=='*':
                    num_bombs+=1
        return num_bombs
    
    def dig(self,row,col):

        if (row,col) in self.dug:
            return True
        
        self.dug.add((row,col))

        if self.board[row][col]=='*':
            return False
        elif self.board[row][col]>0:
            return True
        
        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if (r,c) not in self.dug:
                    self.dig(r,c)
        return True
    def __str__(self):
        visible_board = [[str(self.board[r][c]) if (r, c) in self.dug else ' '
                          for c in range(self.dim_size)] for r in range(self.dim_size)]

        string_rep = ''
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        indices = [str(i) for i in range(self.dim_size)]
        header = '   ' + '  '.join([f"{i:>{widths[idx]}}" for idx, i in enumerate(indices)]) + '\n'
        string_rep += header

        for i, row in enumerate(visible_board):
            row_str = f"{i} |" + ' |'.join([f"{col:>{widths[idx]}}" for idx, col in enumerate(row)]) + ' |\n'
            string_rep += row_str

        return string_rep

def play(dim_size=5,num_bombs=5):

    game=Minesweeper(dim_size,num_bombs)
    safe=True

    while len(game.dug) < game.dim_size**2-num_bombs:

        print(game)

        try:
            row,col=map(int,input("Which cell do you want to dig ? (row col) : ").split())

            if row <0 or row >=dim_size or col<0 or col>=dim_size:
                raise ValueError
        except ValueError:
            print("Invalid input Please enter again !!")
            continue

        safe=game.dig(row,col)
        if not safe:
            break

    if  safe:
        print("Congratulations ! You Won the game")
    else:
        print('Game Over you stepped on a mine !!')
        game.dug = {(r,c) for r in range(dim_size) for c in range(dim_size)}
        print(game)


#rDriver Code
if __name__=="__main__":
    play()


        
