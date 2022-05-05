# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Game:
    values = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    running = True
    first_player_name = "First Player"
    second_player_name = "Second Player"
    first_player_symbol = "O"
    second_player_symbol = "X"

    def __init__(self):
        self.configure()

    def configure(self):
        print("1.Default Game")
        print("2.Enter player names and symbol")
        val = int(input("Enter your choice : "))
        if val == 2:
            self.first_player_name = input("Enter First player name    : ")
            self.second_player_name = input("Enter Second player name   : ")
            self.first_player_symbol = input("Enter First player symbol  : ")
            self.second_player_symbol = input("Enter Second player symbol : ")

    def start(self):
        self.display()
        while self.running:
            self.take_input(self.first_player_name)
            if self.display():
                break
            self.take_input(self.second_player_name)
            self.display()

    def display(self):
        # os.system("cls")
        print(f'{self.values[0][0]}|{self.values[0][1]}|{self.values[0][2]}')
        print(f'{self.values[1][0]}|{self.values[1][1]}|{self.values[1][2]}')
        print(f'{self.values[2][0]}|{self.values[2][1]}|{self.values[2][2]}')
        if self.check_victory(self.first_player_symbol) or self.check_victory(self.second_player_symbol):
            return True

    def take_input(self, player_name):
        val = int(input(f"{player_name}'s turn : "))
        row = int((val - 1) / 3)
        col = (val - 1) % 3
        if player_name == self.first_player_name:
            self.values[row][col] = self.first_player_symbol
        else:
            self.values[row][col] = self.second_player_symbol

    def print_victory(self, symbol):
        if symbol == self.first_player_symbol:
            print(f"{self.first_player_name} wins")
        else:
            print(f"{self.second_player_name} wins")

    def check_victory(self, symbol):
        for i in range(3):
            if self.values[i][0] == symbol and self.values[i][1] == symbol and self.values[i][2] == symbol:
                self.print_victory(symbol)
                self.running = False
                return True
            if self.values[0][i] == symbol and self.values[1][i] == symbol and self.values[2][i] == symbol:
                self.print_victory(symbol)
                self.running = False
                return True

        if self.values[0][0] == symbol and self.values[1][1] == symbol and self.values[2][2] == symbol:
            self.print_victory(symbol)
            return True
        if self.values[0][2] == symbol and self.values[1][1] == symbol and self.values[2][0] == symbol:
            self.print_victory(symbol)
            return True


if __name__ == '__main__':
    game = Game()
    game.start()
