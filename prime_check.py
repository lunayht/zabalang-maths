import sys


def is_prime(n: int, i: int) -> bool:
    if n == 0 or n == 1:
        return False

    if n == i:
        return True

    if n % i == 0:
        return False

    i += 1

    return is_prime(n, i)


if __name__ == "__main__":
    sys.setrecursionlimit(9000)

    number = input("Number: ")
    result = is_prime(int(number), 2)
    if result:
        print(f"{number} is prime!")
    else:
        print(f"{number} is not a prime :(")
