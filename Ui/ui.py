import copy
import random
from colorama import Style, Fore
from Services.services import Services


class UI:
    def __init__(self, services: Services):
        self.services = services
        self.player_board = []
        self.ai_board = []
        self.pdestroyer = self.pcruiser = self.psubmarine = self.pbattleship = self.pcarrier = []
        self.adestroyer = self.acruiser = self.asubmarine = self.abattleship = self.acarrier = []
        self.pcords = {}
        self.acords = {}
        self.ai_fake_board = self.services.create_board()
        self.ai_data = []
        self.orgpcords = {}
        self.orgacords = {}

    """
    - Creates the player and ai boards
    """
    def create_board(self):
        # Creates two empty boards
        self.player_board = self.services.create_board()
        self.ai_board = self.services.create_board()

        # Player places the ships now
        # Places a 2 space ship (Destroyer), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                bow = str(input("Choose the coordinates of the bow of the destroyer(LetterNumber) : "))
                direction = str(input("Choose the direction that the ship is facing(N/E/S/W) : "))
                self.player_board, self.pdestroyer = self.services.place_destroyer(bow, direction, self.player_board)
                ok = 1
            except ValueError as ve:
                print(ve)
        self.show_board(self.player_board, self.ai_fake_board, "")

        # Places a 3 space ship (Cruiser), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                bow = str(input("Choose the coordinates of the bow of the cruiser(LetterNumber) : "))
                direction = str(input("Choose the direction that the ship is facing(N/E/S/W) : "))
                self.player_board, self.pcruiser = self.services.place_cruiser(bow, direction, self.player_board)
                ok = 1
            except ValueError as ve:
                print(ve)
        self.show_board(self.player_board, self.ai_fake_board, "")

        # Places a 3 space ship (Submarine), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                bow = str(input("Choose the coordinates of the bow of the submarine(LetterNumber) : "))
                direction = str(input("Choose the direction that the ship is facing(N/E/S/W) : "))
                self.player_board, self.psubmarine = self.services.place_submarine(bow, direction, self.player_board)
                ok = 1
            except ValueError as ve:
                print(ve)
        self.show_board(self.player_board, self.ai_fake_board, "")

        # Places a 4 space ship (Battleship), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                bow = str(input("Choose the coordinates of the bow of the battleship(LetterNumber) : "))
                direction = str(input("Choose the direction that the ship is facing(N/E/S/W) : "))
                self.player_board, self.pbattleship = self.services.place_battleship(bow, direction, self.player_board)
                ok = 1
            except ValueError as ve:
                print(ve)
        self.show_board(self.player_board, self.ai_fake_board, "")

        # Places a 5 space ship (Carrier), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                bow = str(input("Choose the coordinates of the bow of the carrier(LetterNumber) : "))
                direction = str(input("Choose the direction that the ship is facing(N/E/S/W) : "))
                self.player_board, self.pcarrier = self.services.place_carrier(bow, direction, self.player_board)
                ok = 1
            except ValueError as ve:
                print(ve)

        # Ai places the ships now
        print("Ai placing now\n")

        # Places a 5 space ship (Carrier), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                x = random.randint(1, 10)
                y = random.randint(1, 10) + 64
                direction = self.randomdirection()
                self.ai_board, self.acarrier = self.services.place_carrier(chr(y) + str(x), direction, self.ai_board)
                ok = 1
            except ValueError as ve:
                print(ve)

        # Places a 4 space ship (Battleship), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                x = random.randint(1, 10)
                y = random.randint(1, 10) + 64
                direction = self.randomdirection()
                self.ai_board, self.abattleship = self.services.place_battleship(chr(y) + str(x), direction, self.ai_board)
                ok = 1
            except ValueError as ve:
                print(ve)

        # Places a 3 space ship (Submarine), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                x = random.randint(1, 10)
                y = random.randint(1, 10) + 64
                direction = self.randomdirection()
                self.ai_board, self.asubmarine = self.services.place_submarine(chr(y) + str(x), direction, self.ai_board)
                ok = 1
            except ValueError as ve:
                print(ve)

        # Places a 3 space ship (Cruiser), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                x = random.randint(1, 10)
                y = random.randint(1, 10) + 64
                direction = self.randomdirection()
                self.ai_board, self.acruiser = self.services.place_cruiser(chr(y) + str(x), direction, self.ai_board)
                ok = 1
            except ValueError as ve:
                print(ve)

        # Places a 2 space ship (Destroyer), if the coordinates don't exist or are already filled it prints an error
        ok = 0
        while ok < 1:
            try:
                x = random.randint(1, 10)
                y = random.randint(1, 10) + 64
                direction = self.randomdirection()
                self.ai_board, self.adestroyer = self.services.place_destroyer(chr(y) + str(x), direction, self.ai_board)
                ok = 1
            except ValueError as ve:
                print(ve)
        self.pcords.update({'d': self.pdestroyer, 'c': self.pcruiser, 's': self.psubmarine, 'b': self.pbattleship, 'ca': self.pcarrier})
        self.acords.update({'d': self.adestroyer, 'c': self.acruiser, 's': self.asubmarine, 'b': self.abattleship, 'ca': self.acarrier})
        self.orgpcords.update({'d': copy.deepcopy(self.pdestroyer), 'c': copy.deepcopy(self.pcruiser), 's': copy.deepcopy(self.psubmarine), 'b': copy.deepcopy(self.pbattleship), 'ca': copy.deepcopy(self.pcarrier)})
        self.orgacords.update({'d': copy.deepcopy(self.adestroyer), 'c': copy.deepcopy(self.acruiser), 's': copy.deepcopy(self.asubmarine), 'b': copy.deepcopy(self.abattleship), 'ca': copy.deepcopy(self.acarrier)})
        self.show_board(self.player_board, self.ai_fake_board, "")


    """
    -- Gives a random direction
    -- Output: N / E / S / W
    """
    @staticmethod
    def randomdirection():
        dir = random.randint(0, 3)
        if dir == 0:
            direction = "N"
        elif dir == 1:
            direction = "E"
        elif dir == 2:
            direction = "S"
        elif dir == 3:
            direction = "W"
        return direction

    """
    -- Prints out both the player board and the fake_ai_board (the one the player should see, not hte one containing hte ships)
    """
    def show_board(self, board1, board2, message):
        if message == "":
            textspace = "                                "
        else:
            textspace = message
        row2 = "---+ - + - + - + - + - + - + - + - + - + - +---"
        space = "                                "
        space1 = "                               "
        space2 = "                             "
        row = " "
        for j in range(0, 11):
            row += board1[0][j] + " |"
            row += board1[0][11]
        row += " " + space + " "
        for j in range(0, 11):
            row += board2[0][j] + " | "
        row += board2[0][11]
        print(row)
        print(row2, space2, row2)
        row = " "
        for i in range(1, 5):
            row = " "
            for j in range(0, 11):
                row += self.color_text(board1[i][j]) + " | "
            row += board1[i][11]
            row += space + " "
            for j in range(0, 11):
                row += self.color_text(board2[i][j]) + " | "
            row += board2[i][11]
            print(row)
            print(row2, space2, row2)
        row = " "
        for j in range(0, 11):
            row += self.color_text(board1[5][j]) + " | "
        row += board1[5][11]
        row += textspace + " "
        for j in range(0, 11):
            row += self.color_text(board2[5][j]) + " | "
        row += board2[5][11]
        print(row)
        print(row2, space2, row2)
        for i in range(6, 10):
            row = " "
            for j in range(0, 11):
                row += self.color_text(board1[i][j]) + " | "
            row += board1[i][11]
            row += space + " "
            for j in range(0, 11):
                row += self.color_text(board2[i][j]) + " | "
            row += board2[i][11]
            print(row)
            print(row2, space2, row2)
        row = ""
        for j in range(0, 11):
            row += self.color_text(board1[10][j]) + " | "
        row += board1[10][11]
        row += space1
        for j in range(0, 11):
            row += self.color_text(board2[10][j]) + " | "
        row += board2[10][11]
        print(row)
        print(row2, space2, row2)
        row = " "
        for j in range(0, 11):
            row += board1[11][j] + " | "
        row += board1[11][11]
        row += space + " "
        for j in range(0, 11):
            row += board2[11][j] + " | "
        row += board2[11][11]
        print(row)
        print(row2, space2, row2)
        print("\n\n")

    """
    -- Colors the spaces that have been hit
    """
    @staticmethod
    def color_text(text):
        # Friendly not hit space
        if text == 'B' or text == 'C' or text == 'D' or text == 'K' or text == 'S':
            return Fore.GREEN + text + Style.RESET_ALL
        # Hit space
        elif text == 'X':
            return Fore.RED + text + Style.RESET_ALL
        # Missed space
        elif text == 'O':
            return Fore.LIGHTBLUE_EX + text + Style.RESET_ALL
        return text

    def getbody(self):
        print(self.pdestroyer)
        print(self.pcruiser)
        print(self.psubmarine)
        print(self.pbattleship)
        print(self.pcarrier)
        print(self.adestroyer)
        print(self.acruiser)
        print(self.asubmarine)
        print(self.abattleship)
        print(self.acarrier)
        print(self.pcords)
        print(self.acords)

    """
    -- Starts the actual game
    """
    def play(self):

        # Randomly chooses who starts the game
        turn = random.randint(1, 2)
        if turn == 1:
            self.print_space()
            print("You go first")
            self.print_space()
        else:
            self.print_space()
            print("Ai goes first")
            self.print_space()

        # Main game loop
        while self.get_length(self.pcords) > 0 and self.get_length(self.acords) > 0:
            if turn == 1:
                self.playerturn()
                print("\n")
                input("Press enter for ai turn\n\n")
                print("\n")
                turn = 2
            else:
                self.aiturn()
                turn = 1
        self.gameend()

    """
    -- The player's turn to choose a space to hit
    """
    def playerturn(self):
        ok = 0
        while ok == 0 and self.get_length(self.acords) != 0:
            try:
                guess = str(input("Choose the coordinates where you want to hit (LetterNumber) : "))
                self.ai_fake_board, self.acords, hit, sunk = self.services.playerturn(guess, self.ai_fake_board, self.acords)
                if hit == 2:
                    message = "            Ship sunk           "
                    self.change_board_sunk_player(sunk)
                    self.show_board(self.player_board, self.ai_fake_board, message)
                elif hit == 1:
                    message = "            Ship hit            "
                    self.show_board(self.player_board, self.ai_fake_board, message)
                else:
                    ok = 1
                    message = "           You missed           "
                    self.show_board(self.player_board, self.ai_fake_board, message)
            except ValueError as ve:
                print(ve)

    """
    -- If a certain ship is sunk, its spaces from red to purple for the player
    """
    def change_board_sunk_player(self, sunk):
        if sunk == "D":
            for i in range(0, len(self.orgacords['d'])):
                self.ai_fake_board[self.orgacords['d'][i][0]][self.orgacords['d'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL
        if sunk == "C":
            for i in range(0, len(self.orgacords['c'])):
                self.ai_fake_board[self.orgacords['c'][i][0]][self.orgacords['c'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL
        if sunk == "S":
            for i in range(0, len(self.orgacords['s'])):
                self.ai_fake_board[self.orgacords['s'][i][0]][self.orgacords['s'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL
        if sunk == "B":
            for i in range(0, len(self.orgacords['b'])):
                self.ai_fake_board[self.orgacords['b'][i][0]][self.orgacords['b'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL
        if sunk == "K":
            for i in range(0, len(self.orgacords['ca'])):
                self.ai_fake_board[self.orgacords['ca'][i][0]][self.orgacords['ca'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL

    """
        -- If a certain ship is sunk, its spaces from red to purple for the player
    """
    def change_board_sunk_ai(self, sunk):
        if sunk == "D":
            for i in range(0, len(self.orgpcords['d'])):
                self.player_board[self.orgpcords['d'][i][0]][self.orgpcords['d'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL
        if sunk == "C":
            for i in range(0, len(self.orgpcords['c'])):
                self.player_board[self.orgpcords['c'][i][0]][self.orgpcords['c'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL
        if sunk == "S":
            for i in range(0, len(self.orgpcords['s'])):
                self.player_board[self.orgpcords['s'][i][0]][self.orgpcords['s'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL
        if sunk == "B":
            for i in range(0, len(self.orgpcords['b'])):
                self.player_board[self.orgpcords['b'][i][0]][self.orgpcords['b'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL
        if sunk == "K":
            for i in range(0, len(self.orgpcords['ca'])):
                self.player_board[self.orgpcords['ca'][i][0]][self.orgpcords['ca'][i][1]] = Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL

    """
    -- The ai's turn
    """
    def aiturn(self):
        ok = 0
        while ok == 0 and self.get_length(self.acords) != 0:
            try:
                guess, self.ai_data = self.services.ai_logic(self.ai_data)
                self.player_board, self.pcords, hit, self.ai_data, sunk = self.services.aiturn(guess, self.player_board, self.pcords, self.ai_data, self.orgpcords)
                if hit == 2:
                    message = "            Ship sunk           "
                    self.change_board_sunk_ai(sunk)
                    self.show_board(self.player_board, self.ai_fake_board, message)
                elif hit == 1:
                    message = "            Ship hit            "
                    self.show_board(self.player_board, self.ai_fake_board, message)
                    direct = [0, 1, 2, 3]
                    self.ai_data.append([guess, random.sample(direct, len(direct))])
                else:
                    ok = 1
                    print("Ai guessed: " + guess)
                    message = "            Ai missed           "
                    self.show_board(self.player_board, self.ai_fake_board, message)
            except ValueError as ve:
                print(ve)

    """
    -- Prints out who wins
    """
    def gameend(self):
        if self.get_length(self.pcords) == 0:
            message = "            You lost            "
            self.show_board(self.player_board, self.ai_fake_board, message)
        else:
            message = "            You won             "
            self.show_board(self.player_board, self.ai_fake_board, message)

    @staticmethod
    def print_space():
        print("\n\n\n\n\n\n\n\n")
