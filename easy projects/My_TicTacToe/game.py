player_1 = "Daria"
player_2 = "Tommaso"

class Player:
    
    def __init__(self, letter):
        self.letter = letter

class Human_player(Player):
    
    def __init__(self, name, letter):
        super().__init__(letter)
        self.name = name
        
    def get_move(self, game):
        while True:    
            self.move = input("Imput a move (0-8): ")
            try:
                self.move = int(self.move)
            except ValueError :
                print("Invalid character. Try again: ")
                continue
            # bisogna gestire l'errore
            if self.move in game.available_moves:
                game.available_moves.remove(self.move)
                return self.move
            else:
                print("Invalid move. Try again: ")

class Computer_player(Player):
    
    def __init__(self, letter):
        super().__init__(letter)
        self.name = "Computer"
        self.enemy_letter = "X" if self.letter == "O" else "O"
        
    def get_move(self, game):
        board = [game.board[i].copy() for i in range(3)]
        self.move, result = self.min_max(board, game.available_moves.copy(), self.letter, self.enemy_letter)
        game.available_moves.remove(self.move)
        return self.move

    @classmethod
    def min_max(cls, board, available, letter, enemy_letter):

        def update(board, move, letter):
            row = move // 3 
            column = move % 3 
            board[row][column] = letter
            return board

        if Game.player_won(letter, board):
            return (None, 1*(len(available) + 1))
        elif Game.player_won(enemy_letter, board):
            return (None, -1*(len(available) + 1))
        elif not available:
            return (None, 0)

        results = []
        for move in available:
            n_board = update([board[i].copy() for i in range(3)], move, letter)
            n_available = available.copy()
            n_available.remove(move)
            results.append((move, (cls.min_max(n_board, n_available, enemy_letter, letter))[1]))

        move, result = min(results, key=lambda x: x[1])
        result = result * -1

        return move, result

class Game:
    def __init__(self, p1, p2):
        
        self.p1 = p1
        self.p2 = p2
        self.players = [p1, p2]
        
        self.board = [[" "]*3, [" "]*3, [" "]*3]
        self.available_moves = [i for i in range(9)]
        
        self.not_a_winner = True
        self.winner = None
        
    def print_board(self):
        for row in self.board:
            print("| " + " | ".join(row) + " |")
            
    @staticmethod
    def print_number_board():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
        
    @staticmethod
    def player_won(letter, board):
        result = False

        # checking rows
        for row in board:
            if row.count(letter) == 3:
                result = True

        # checking columns
        for column in range(3):
            col_letters = []
            for row in board: 
                col_letters.append(row[column])
            if col_letters.count(letter) == 3:
                result = True

        # checking diagonals
        i = 0
        diag_letters = []
        for row in board: 
            diag_letters.append(row[i])
            i += 1
        if diag_letters.count(letter) == 3:
            result = True

        i = -1
        diag_letters = []
        for row in board: 
            diag_letters.append(row[i])
            i -= 1
        if diag_letters.count(letter) == 3:
            result = True

        return result

    def not_winner(self):
        
        if self.player_won(self.player_on_turn.letter, self.board):
            self.winner = self.player_on_turn
            self.not_a_winner = False

        return self.not_a_winner

    def update_board(self):
        row = self.move // 3 
        column = self.move % 3 
        self.board[row][column] = self.player_on_turn.letter

    def play(self):
        
        self.print_number_board()
        print("\nWelcome to Tic Tac Toe, use your numpad to play.")

        self.player_on_turn = self.p2
        while self.not_winner() and self.available_moves:
            self.player_on_turn = self.p1 if self.player_on_turn == self.p2 else self.p2
            print(f"\nIt's {self.player_on_turn.name}'s turn")
            self.move = self.player_on_turn.get_move(self)
            self.update_board()
            self.print_board()
        if self.not_winner():
            print("Well done to both players, It's a tie!")
        else:
            print(f"Well done {self.player_on_turn.name}, you won!")

Io = Human_player(player_1, "X")
Cecio = Human_player(player_2, "O")
Computer = Computer_player("O")

Tic_Tac_Toe = Game(Io, Computer)
Tic_Tac_Toe.play()

# ctrl + alt + c