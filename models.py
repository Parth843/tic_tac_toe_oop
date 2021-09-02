class Board():
    
    def __init__(self):
        self.board = [["."]*3 for x in range(3)]

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def put_x(self, x, y):
        self.board[x][y] = "X"

    def put_o(self, x, y):
        self.board[x][y] = "o"

    def detect_win(self):
        for row in self.board:
            if (row[0] == row[1] == row[2] == "X") or (row[0] == row[1] == row[2] == "o"):
                return True

        for i in range(3):
            if (self.board[0][i] == self.board[1][i] == self.board[2][i] == "X") or (self.board[0][i] == self.board[1][i] == self.board[2][i] == "o"):
                return True

        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == "X") or (self.board[0][0] == self.board[1][1] == self.board[2][2] == "o"):
            return True

        if (self.board[0][2] == self.board[1][1] == self.board[2][0] == "X") or (self.board[0][2] == self.board[1][1] == self.board[2][0] == "o"):
            return True

        return False
        
            

class Player():
    
    def __init__(self, name):
        self.name = name

    def get_input(self):
        inp = input("Enter row and col: ")
        x, y = [int(i) for i in inp.split()]
        return (x, y)

class Game():
    
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.board = Board()
        self.current_turn = None

    def player1_turn(self):
        self.current_turn = self.player1
        print(f"{self.player1.name}'s turn.")
        x, y = self.player1.get_input()
        self.board.put_x(x, y)

    def player2_turn(self):
        self.current_turn = self.player2
        print(f"{self.player2.name}'s turn.")
        x, y = self.player2.get_input()
        self.board.put_o(x, y)

    def check_winner(self):
        if self.board.detect_win():
            print(f"{self.current_turn.name} wins !")
            return True
        return False

    def play_game(self):
        while True:
            self.board.print_board()
            self.player1_turn()
            self.board.print_board()
            
            if self.check_winner():
                break
    
            self.player2_turn()
            if self.check_winner():
                break