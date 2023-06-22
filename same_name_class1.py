class SameNameClass:
    def __init__(self, value):
        self.value = value

    def action(self):
        return f"Class 1 action with value {self.value}"

    @classmethod
    def print_class_info(cls):
        print("This is the first class with the same name")

    @staticmethod
    def utility_method(val):
        return val * 2
