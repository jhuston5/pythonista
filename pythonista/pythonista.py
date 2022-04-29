import sys

class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


def repeater(value):
    while True:
        yield value




if __name__ == "__main__":
  print(sys.getsizeof(repeater("Yes")))