class SameNameClass:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def action(self):
        return f"Class 2 action with values {self.value1} and {self.value2}"

    @classmethod
    def print_class_info(cls):
        print("This is the second class with the same name")

    @staticmethod
    def utility_method(val1, val2):
        return val1 + val2
