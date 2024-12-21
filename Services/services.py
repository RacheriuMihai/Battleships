from colorama import Fore, Style

from Domain.destroyer import *
from Domain.cruiser import *
from Domain.submarine import *
from Domain.battleship import *
from Domain.carrier import *
import random
class Services:

    """
    -- Creates a 12 X 12 board, the first and last rows are letters assigned to the collumns and the first and last
    -- colluns are numbers assigned to each row
    """
    @staticmethod
    def create_board():
        board = []
        board.append([" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", " "])
        row = 1
        while row <= 10:
            board.append([str(row), " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", str(row)])
            row += 1
        board.append([" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", " "])
        return board

    """
    -- Places a 2 space ship at hte given coordinates on a given board
    """
    def place_destroyer(self, bow, direction, board):
        x, y = self.cordtoxy(bow)
        cords = [x, y]
        dir = self.direction_to_int(direction)
        print(x, y)
        self.check_destroyer(bow, direction, board)
        destroyer = Destroyer(cords[0], cords[1], dir)
        body = destroyer.get_body()
        print(body)
        for i in range(0, len(body)):
            board[body[i][0]][body[i][1]] = "D"
        return board, destroyer.get_body()

    """
    -- Places a 3 space ship at hte given coordinates on a given board
    """
    def place_cruiser(self, bow, direction, board):
        x, y = self.cordtoxy(bow)
        cords = [x, y]
        dir = self.direction_to_int(direction)
        print(x, y)
        self.check_cruiser_or_submarine(bow, direction, board)
        cruiser = Cruiser(cords[0], cords[1], dir)
        body = cruiser.get_body()
        print(body)
        for i in range(0, len(body)):
            board[body[i][0]][body[i][1]] = "C"
        return board, cruiser.get_body()

    """
    -- Places a 3 space ship at hte given coordinates on a given board
    """
    def place_submarine(self, bow, direction, board):
        x, y = self.cordtoxy(bow)
        cords = [x, y]
        dir = self.direction_to_int(direction)
        print(x, y)
        self.check_cruiser_or_submarine(bow, direction, board)
        submarine = Submarine(cords[0], cords[1], dir)
        body = submarine.get_body()
        print(body)
        for i in range(0, len(body)):
            board[body[i][0]][body[i][1]] = "S"
        return board, submarine.get_body()

    """
    -- Places a 4 space ship at hte given coordinates on a given board
    """
    def place_battleship(self, bow, direction, board):
        x, y = self.cordtoxy(bow)
        cords = [x, y]
        dir = self.direction_to_int(direction)
        print(x, y)
        self.check_battleship(bow, direction, board)
        battleship = Battleship(cords[0], cords[1], dir)
        body = battleship.get_body()
        print(body)
        for i in range(0, len(body)):
            board[body[i][0]][body[i][1]] = "B"
        return board, battleship.get_body()

    """
    -- Places a 5 space ship at hte given coordinates on a given board
    """
    def place_carrier(self, bow, direction, board):
        x, y = self.cordtoxy(bow)
        cords = [x, y]
        dir = self.direction_to_int(direction)
        print(x, y)
        self.check_carrier(bow, direction, board)
        carrier = Carrier(cords[0], cords[1], dir)
        body = carrier.get_body()
        print(body)
        for i in range(0, len(body)):
            board[body[i][0]][body[i][1]] = "K"
        return board, carrier.get_body()

    """
    -- Checks if all the coordinates that belong to the destoryer's body are valid
    """
    def check_destroyer(self, bow, direction, board):
        x, y = self.cordtoxy(bow)
        cords = [x, y]
        dir = self.direction_to_int(direction)
        error = ""
        if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
            error += "Invalid bow coordinates\n"
        if dir == 0:
            cords[0] += 1
            if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                error += "Invalid body coordinates"
        if dir == 1:
            cords[1] -= 1
            if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                error += "Invalid body coordinates"
        if dir == 2:
            cords[0] -= 1
            if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                error += "Invalid body coordinates"
        if dir == 3:
            cords[1] += 1
            if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                error += "Invalid body coordinates"
        if len(error) > 0:
            raise ValueError(error)

    """
   -- Checks if all the coordinates that belong to the cruiser's or submarines's body are valid
    """
    def check_cruiser_or_submarine(self, bow, direction, board):
        x, y = self.cordtoxy(bow)
        cords = [x, y]
        dir = self.direction_to_int(direction)
        error = ""
        if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
            error += "Invalid bow coordinates\n"
        check = 2
        if dir == 0:
            while (check > 0):
                cords[0] += 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if dir == 1:
            while (check > 0):
                cords[1] -= 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if dir == 2:
            while (check > 0):
                cords[0] -= 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if dir == 3:
            while (check > 0):
                cords[1] += 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if len(error) > 0:
            raise ValueError(error)

    """
    -- Checks if all the coordinates that belong to the battleships's body are valid
    """
    def check_battleship(self, bow, direction, board):
        x, y = self.cordtoxy(bow)
        cords = [x, y]
        dir = self.direction_to_int(direction)
        error = ""
        if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
            error += "Invalid bow coordinates\n"
        check = 3
        if dir == 0:
            while (check > 0):
                cords[0] += 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if dir == 1:
            while (check > 0):
                cords[1] -= 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if dir == 2:
            while (check > 0):
                cords[0] -= 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if dir == 3:
            while (check > 0):
                cords[1] += 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if len(error) > 0:
            raise ValueError(error)

    """
   -- Checks if all the coordinates that belong to the carrier's body are valid
    """
    def check_carrier(self, bow, direction, board):
        x, y = self.cordtoxy(bow)
        cords = [x, y]
        dir = self.direction_to_int(direction)
        error = ""
        if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
            error += "Invalid bow coordinates\n"
        check = 4
        if dir == 0:
            while (check > 0):
                cords[0] += 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if dir == 1:
            while (check > 0):
                cords[1] -= 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if dir == 2:
            while (check > 0):
                cords[0] -= 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if dir == 3:
            while (check > 0):
                cords[1] += 1
                if cords[0] < 1 or cords[0] > 10 or cords[1] < 1 or cords[1] > 10 or board[cords[0]][cords[1]] != " ":
                    error += "Invalid body coordinates"
                check -= 1
        if len(error) > 0:
            raise ValueError(error)

    """
    -- Converts a givne direction to a number
    """
    @staticmethod
    def direction_to_int(direction):
        error = ""
        if direction != "N" and direction != "E" and direction != "S" and direction != "W":
            error += "Invalid direction. Should be of type ( N / E / S / W )!"
        if len(error) > 0:
            raise ValueError(error)
        if direction == "N":
            return 0
        if direction == "E":
            return 1
        if direction == "S":
            return 2
        if direction == "W":
            return 3

    """
    -- Converts the LetterInt pair to 2 numbers from 1 to 10
    """
    @staticmethod
    def cordtoxy(bow):
        bow = list(bow)
        error = ""
        if len(bow) == 0 or len(bow) == 1:
            error += "Invalid coordinates(Should be of type (LetterInt))"
            raise ValueError(error)
        if len(bow) < 2 or len(bow) > 3:
            error += "Invalid coordinates(Should be of type (LetterInt))"
        if len(bow) == 3 and (bow[1] != "1" or bow[2] != "0"):
            error += "Invalid coordinates(Should be of type (LetterInt))"
        if len(bow) == 3:
            y = ord(bow[0]) - 64
            x = 10
        else:
            y = ord(bow[0]) - 64
            x = int(ord(bow[1]) - 48)
        if y < 1 or x < 1 or y > 10 or x > 10:
            error += "Invalid coordonates!"
        if len(error) > 0:
            raise ValueError(error)
        return x, y

    def cordtoxylist(self, guess):
        x, y = self.cordtoxy(guess)
        return [x, y]

    """
    -- Transforms two numbers to a LetterInt pair
    """
    @staticmethod
    def xytocord(x, y):
        cy = chr(y + 64)
        cx = chr(x + 48)
        res = cy + cx
        return res

    """
    -- Checks if the space guesses by the player belongs to an ai ship
    -- It returns 0 if it is a miss, 1 if it is a hit and 2 if it is a hit and the ship is sunk
    """
    def playerturn(self, guess, fakeboard, cords):
        x, y = self.cordtoxy(guess)
        self.checkhit([x, y], fakeboard)
        trguess = [x, y]
        hit = 0
        mes = ""
        if trguess in cords['d']:
            cords['d'].remove(trguess)
            hit = 1
            if len(cords['d']) == 0:
                hit = 2
                mes += "D"
        elif trguess in cords['c']:
            cords['c'].remove(trguess)
            hit = 1
            if len(cords['c']) == 0:
                hit = 2
                mes += "C"
        elif trguess in cords['s']:
            cords['s'].remove(trguess)
            hit = 1
            if len(cords['s']) == 0:
                hit = 2
                mes += "S"
        elif trguess in cords['b']:
            cords['b'].remove(trguess)
            hit = 1
            if len(cords['b']) == 0:
                hit = 2
                mes += "B"
        elif trguess in cords['ca']:
            cords['ca'].remove(trguess)
            hit = 1
            if len(cords['ca']) == 0:
                hit = 2
                mes += "K"
        if hit == 2:
            fakeboard[x][y] = "X"
            return fakeboard, cords, 2, mes
        elif hit == 1:
            fakeboard[x][y] = "X"
            return fakeboard, cords, 1, mes
        else:
            fakeboard[x][y] = "O"
            return fakeboard, cords, 0, mes

    """
    -- Checks if the space guesses by the ai belongs to a player ship
    -- It returns 0 if it is a miss, 1 if it is a hit and 2 if it is a hit and the ship is sunk
    """
    def aiturn(self, guess, fakeboard, cords, ai_data, orgcords):
        x, y = self.cordtoxy(guess)
        self.checkhit([x, y], fakeboard)
        trguess = [x, y]
        hit = 0
        mes = ""
        if trguess in cords['d']:
            cords['d'].remove(trguess)
            hit = 1
            if len(cords['d']) == 0:
                hit = 2
                self.sunk_ship_remove_logic(ai_data, orgcords['d'])
                mes += "D"
        elif trguess in cords['c']:
            cords['c'].remove(trguess)
            hit = 1
            if len(cords['c']) == 0:
                hit = 2
                self.sunk_ship_remove_logic(ai_data, orgcords['c'])
                mes += "C"
        elif trguess in cords['s']:
            cords['s'].remove(trguess)
            hit = 1
            if len(cords['s']) == 0:
                hit = 2
                self.sunk_ship_remove_logic(ai_data, orgcords['s'])
                mes += "S"
        elif trguess in cords['b']:
            cords['b'].remove(trguess)
            hit = 1
            if len(cords['b']) == 0:
                hit = 2
                self.sunk_ship_remove_logic(ai_data, orgcords['b'])
                mes += "B"
        elif trguess in cords['ca']:
            cords['ca'].remove(trguess)
            hit = 1
            if len(cords['ca']) == 0:
                hit = 2
                self.sunk_ship_remove_logic(ai_data, orgcords['ca'])
                mes += "K"
        if hit == 2:
            fakeboard[x][y] = "X"
            return fakeboard, cords, 2, ai_data, mes
        elif hit == 1:
            fakeboard[x][y] = "X"
            return fakeboard, cords, 1, ai_data, mes
        else:
            fakeboard[x][y] = "O"
            return fakeboard, cords, 0, ai_data, mes

    """
    -- Checks if the space has already been hit
    """
    @staticmethod
    def checkhit(guess, board):
        error = ""
        if board[guess[0]][guess[1]] == "X" or board[guess[0]][guess[1]] == "O" or board[guess[0]][guess[1]] == Fore.LIGHTMAGENTA_EX + 'X' + Style.RESET_ALL:
            error += "Coordinates already hit!"
        if len(error) > 0:
            raise ValueError(error)

    """
    -- The logic behind the ai's guesses:
    -- if the list of hit spaces is empty, it will randomly choose a space, if the space is a hit it will add it to a list
    -- if the list of hit spaces is not empty, it will take the first from the list and the guess in a random dirrection arround it
    -- if a ship is sunk, all its spaces are deleted form the hit list
    """
    def ai_logic(self, ai_data):
        if len(ai_data) == 0:
            guess = self.ai_random()
        else:
            guess, ai_data = self.ai_hunt_ship(ai_data)
        return guess, ai_data

    """
    -- Chooses a random space for the ai
    """
    @staticmethod
    def ai_random():
        x = random.randint(1, 10)
        y = random.randint(1, 10) + 64
        return chr(y) + str(x)

    """
    -- Chooses a space that is in a random direction from hte first space in the hit spaces list
    """
    def ai_hunt_ship(self, ai_data):
        already_found = ai_data[0][0]
        found = self.cordtoxylist(already_found)
        direction = ai_data[0][1][0]
        if direction == 0:
            found[0] -= 1
        elif direction == 1:
            found[1] += 1
        elif direction == 2:
            found[0] += 1
        else:
            found[1] -= 1
        del(ai_data[0][1][0])
        if len(ai_data[0][1]) == 0:
            del ai_data[0]
        return self.xytocord(found[0], found[1]), ai_data

    """
    -- Removes all the spaces from the hit list that belong to a ship that has been sunk
    """
    @staticmethod
    def sunk_ship_remove_logic(ai_data, ship):
        to_remove = []
        for i in range(0, len(ship)):
            for j in range(0, len(ai_data)):
                if ship[i][0] == ai_data[j][0][0] and ship[i][1] == ai_data[j][0][1]:
                    to_remove.append(j)
        for i in range(0, len(to_remove)):
            del ai_data[i]
            for j in range(i+1, len(to_remove)):
                if to_remove[i] < to_remove[j]:
                    to_remove[j] -= 1
        return ai_data

