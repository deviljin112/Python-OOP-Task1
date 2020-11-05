class FizzBuzz:
    def __init__(self, div_1, div_2):
        self.numbers = [k for k in range(101) if k != 0]
        self.fizz = div_1
        self.buzz = div_2

    def check_numbers(self):
        for i in range(len(self.numbers)):
            if self.numbers[i] % self.fizz and self.numbers[i] % self.buzz:
                self.numbers[i] = "FizzBuzz"
            elif self.numbers[i] % self.fizz:
                self.numbers[i] = "Fizz"
            elif self.numbers[i] % self.buzz:
                self.numbers[i] = "Buzz"

        return " ".join(str(x) for x in self.numbers)

    def __str__(self):
        return " ".join(str(x) for x in self.numbers)


def main():
    fizz = input("What should be the divider number for 'Fizz'?\n=> ")
    buzz = input("What should be the divider number for 'Buzz'?\n=> ")

    if fizz.isdigit() and buzz.isdigit():
        fizz, buzz = int(fizz), int(buzz)
        game = FizzBuzz(fizz, buzz)

        # print(game)
        print(game.check_numbers())
    else:
        print("You need to use integer numbers!")


if __name__ == "__main__":
    main()
