class Calculator(object):
    def add(self, x, y):
        number_type = (int, float, complex)

        if isinstance(x, number_type) and isinstance(y, number_type):
            return x+y
        else:
            raise ValueError

