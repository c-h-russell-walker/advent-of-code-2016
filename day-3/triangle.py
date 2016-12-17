
class Triangle():
    """ Class and solution assumes sides as floats """

    def __init__(self, sides, *args, **kwargs):
        self.a = float(sides[0])
        self.b = float(sides[1])
        self.c = float(sides[2])

    def pos_sides(self):
        pos = [
            self.a > 0,
            self.b > 0,
            self.c > 0
        ]
        return all(pos)

    def valid_sides(self):
        if not self.pos_sides():
            return False
        valid = [
            self.a + self.b > self.c,
            self.b + self.c > self.a,
            self.c + self.a > self.b,
        ]
        return all(valid)