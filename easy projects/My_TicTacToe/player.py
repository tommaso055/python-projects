class Player:
    
    def __init__(self, letter):
        self.letter = letter
        

class Human_player(Player):
    
    def __init__(self, letter):
        super().__init__(game, letter)
        
    def get_move(self, moves):
        while True:    
            move = int(input("Imput a move (1-9): "))
            # bisogna gestire l'errore
            if move in moves:
                moves.remove(move)
                return move
            else:
                print("Invalid move. Try again: ")
        
        

class Computer_player(Player):
    
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        pass
        
        