import random

def main():

    level = get_level()
    count = 0

    for i in range(10):
        result = task(generate_integer(level), generate_integer(level))
        if result:
            count += 1
        elif not result:
            continue

    print("Score:", count)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
        return number
    elif level == 2:
        number = random.randint(10, 99)
        return number
    elif level == 3:
        number = random.randint(100, 999)#
        return number
    else:
        raise ValueError

def task(x, y):
    for _ in range(3):
        try:
            ans = int(input(f"{x} + {y} = "))
            if ans != x+y:
                print("EEE")
                pass
            if ans == x+y:
                return True
        except ValueError:
            print("EEE")
            pass
    print(x+y)
    return False


if __name__ == "__main__":
    main()
