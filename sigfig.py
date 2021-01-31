class Number:
    def __init__(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def is_decimal(self):
        if isinstance(self.get_val(), float):
            return True
        else:
            return False


x = Number(20.0)

print(x.is_decimal())

