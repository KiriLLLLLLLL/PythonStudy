__author__ = 'Ермаченков Кирилл'


class BaseFigure:

    def __init__(self, name, nc):
        self.name = name
        self.nc = nc



    def get_sides_length(self):
        self.sides_length = []
        self.nc.append(self.nc[0])
        for _ in range(len(self.nc)-1):
            p1 = self.nc[_]
            p2 = self.nc[_ + 1]
            self.sides_length.append(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)**0.5)
        return self.sides_length

    def get_perimeter(self):
        self.perimeter = sum(self.sides_length)
        return self.perimeter

    def get_square(self):
        self.sq = []
        self.nc.append(self.nc[0])
        for _ in range(len(self.nc)-1):
            p1 = self.nc[_]
            p2 = self.nc[_ + 1]
            self.sq.append(p1[0] * p2[1] - p2[0] * p1[1])
        self.square = 0.5 * abs(sum(self.sq))
        return self.square


class Triangle(BaseFigure):

    def __init__(self, name, nc):
        BaseFigure.__init__(self, name, nc)


    def get_height(self):
        self.tr_heights = []
        for _ in range(len(self.sides_length)):
            self.tr_heights.append(2 * self.square / self.sides_length[_])
        return self.tr_heights


class Trapeze(BaseFigure):
    def __init__(self, name, nc):
        BaseFigure.__init__(self, name, nc)

    def trapeze_eq_sides_check(self):
        if self.sides_length[0] == self.sides_length[2] or self.sides_length[1] == self.sides_length[3]:
            eq_sides = "Да"
        else:
            eq_sides = 'Нет'
        return eq_sides
    
        



    
