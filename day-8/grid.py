
class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = [[False for i in range(0, self.height)] for i in range(0, self.width)]

    def __str__(self):
        result = ''

        for y in range(self.height):
            for x in range(self.width):
                if self.rows[x][y]:
                    result += '#'
                else:
                    result += '.'
            result += '\n'

        result += '\n'
        return result

    def count_true(self):
        return sum(x.count(True) for x in self.rows)

    def set_true(self, x, y):
        self.assign(x, y, True)

    def set_false(self, x, y):
        self.assign(x, y, False)

    def assign(self, x, y, state):
        """
        Had modulo operator in place but thought it wasn't needed after all:
        `self.rows[x % self.width][y % self.height] = state`
        """
        self.rows[x][y] = state

    def shift_col(self, x, amt):
        """
        This shifts a column in position x down by the amount supplied
        """
        amount = self.height - amt
        self.rows[x] = self.rows[x][amount:] + self.rows[x][:amount]

    def shift_row(self, y, amt):
        """
        This shifts a row in position y right by the amount supplied
        """
        amount = self.width - amt
        temp_row = [self.rows[idx][y] for idx in range(0, self.width)]
        row = temp_row[amount:] + temp_row[:amount]
        for x, val in enumerate(row):
            self.rows[x][y] = val
