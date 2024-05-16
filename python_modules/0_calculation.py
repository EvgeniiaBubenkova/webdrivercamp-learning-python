#!/usr/bin/python3
if __name__ == "__main__":

    from calculation import add, sub, mul, div

    a = 4  # use this variable as the first argument
    b = 2  # use this variable as the second argument


    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")

