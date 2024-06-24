class FunctionValue:
    def __init__(self, x_0: float = -30, x_n: float = 50, h_x: float = 0.25):
        self.x_0 = x_0
        self.x_n = x_n
        self.h_x = h_x

    def get_value(self):
        lst = []
        while self.x_0 <= self.x_n:
            if self.x_0 <= -2:
                lst.append([self.x_0, 4])
            elif -2 < self.x_0 < 2:
                lst.append([self.x_0, int(((16 - self.x_0 ** 2) ** 0.5) * 1000) / 1000])

            elif self.x_0 >= 2:
                lst.append([self.x_0, int((1.5 * self.x_0) * 1000) / 1000])
            self.x_0 += self.h_x
        return lst


your_variables = FunctionValue()
print(your_variables.get_value())

