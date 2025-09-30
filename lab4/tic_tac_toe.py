from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self,name,sympol):
        self.name = name
        self.sympol = sympol
    @abstractmethod
    def make_move(self,board):
        pass


class HumanPlayer(Player):
    def __init__(self,name,sympol):
        super().__init__(name,sympol)
    
    def make_move(self,board):
        r,c = map(str,input("Enter The Col And The Row Seperated By Space : ").split())
        return [r,c]
        

class ComputerPlayer(Player):
    def __init__(self,name,sympol):
        super().__init__(name,sympol)

    def make_move(self,board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    return [str(i+1), str(j+1)]


class Board:
    def __init__(self):
        self.grid = [[-1 for _ in range(3)] for _ in range(3)]
   
    def display(self):
        for row in self.grid:
            row_display = []
            for cell in row:
                if cell == -1:
                    row_display.append(" ")
                else:
                    row_display.append(str(cell))
            
            print(" | ".join(row_display))
            print("-" * 9)

    def update(self, position, sympol):
        r, c = position
        if not r.isdigit() or not c.isdigit():
            print("Please Enter A Valid Positions")
            return 1
        r = int(r)
        c = int(c)

        if r < 1 or r > 3 or c < 1 or c > 3 :
            print("Please Enter A Valid Positions")
            return 1
        
        r -=1
        c -=1
        
        if self.grid[r][c] == -1:
            self.grid[r][c] = sympol
            self.display()
            return 0
        else:
            print("Cell already taken! Try again.")
            return 1
        


    def check_winner(self):
        x_win = 0
        o_win = 0
        for i in range(len(self.grid)):
            if self.grid[i].count("X") == 3:
                x_win = 1
                break
            if self.grid[i].count("O") == 3:
                o_win = 1
                break
        
        for i in range(len(self.grid[0])):
            if self.grid[0][i] == self.grid[1][i] and self.grid[1][i] == self.grid[2][i]:
                x_win = 1 if self.grid[0][i] == "X" else x_win
                o_win = 1 if self.grid[0][i] == "O" else o_win
                break
        

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != -1:
            x_win = 1 if self.grid[0][0] == "X" else x_win
            o_win = 1 if self.grid[0][0] == "O" else o_win

        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != -1:            
            x_win = 1 if self.grid[0][2] == "X" else x_win
            o_win = 1 if self.grid[0][2] == "O" else o_win

        if x_win == 1:
            print("X Win The Game !!!!!!")
            return 1
        elif o_win == 1:
            print("O Win The Game !!!!!!")
            return 1
        return 0

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == -1:
                    return 0
        print("It's Draw !!!!!!!!")
        return 1




class Game:
    def __init__(self,players,board):
        self.players = players
        self.current_turn = 0
        self.board = board
    
    def play(self):
        while True:
            while True:
                position = self.players[self.current_turn].make_move(self.board.grid)
                notValid = self.board.update(position,self.players[self.current_turn].sympol)
                if notValid == 0:
                    break

                
            case = self.board.check_winner()
            if case:
                break

            case += self.board.is_full()
            if case:
                break
            self.switch_turns()
        

        

    def switch_turns(self):
        self.current_turn ^= 1


def main():
    
    user_input = int(input("1- Play With Friend\n2- Play With Computer\n Your Choice : "))
    
    Pname = input("Please Enter The First Player Name : ")
    player1 = HumanPlayer(Pname,"X")
    
    if user_input == 1:
        Pname = input("Please Enter The Second Player Name : ")
        player2 = HumanPlayer(Pname,"O")

    elif user_input == 2:
        player2 = ComputerPlayer("Computer","O")

    else :
        print("Wrong Choice")
    
    NewBoard = Board()

    NewGame = Game([player1,player2],NewBoard)
    NewGame.play()



if __name__ == "__main__":
    main()