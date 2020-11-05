number_list = [k for k in range(101) if k != 0]


def main():
    fizz = input("What should be the divider number for 'Fizz'?\n=> ")
    buzz = input("What should be the divider number for 'Buzz'?\n=> ")

    if fizz.isdigit() and buzz.isdigit():
        fizz, buzz = int(fizz), int(buzz)
        for i in range(len(number_list)):
            if number_list[i] % fizz == 0 and number_list[i] % buzz == 0:
                number_list[i] = "FizzBuzz"
            elif number_list[i] % fizz == 0:
                number_list[i] = "Fizz"
            elif number_list[i] % buzz == 0:
                number_list[i] = "Buzz"
        print(number_list)
    else:
        print("You need to use integer numbers!")


if __name__ == "__main__":
    main()