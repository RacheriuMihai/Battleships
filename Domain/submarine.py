class Submarine:
    def __init__(self, x, y, direction):
        self.bow = [x, y]
        self.direction = direction
        self.body = [[x, y]]
        self.generate_body()

    def generate_body(self):
        cords = self.bow
        i = 1
        while i < 3:
            if self.direction == 0:
                cords[0] += 1
                self.body.append([cords[0], cords[1]])
            if self.direction == 1:
                cords[1] -= 1
                self.body.append([cords[0], cords[1]])
            if self.direction == 2:
                cords[0] -= 1
                self.body.append([cords[0], cords[1]])
            if self.direction == 3:
                cords[1] += 1
                self.body.append([cords[0], cords[1]])
            i += 1

    def get_body(self):
        return self.body

    def get_direction(self):
        return self.direction

    def get_bow(self):
        return self.bow
