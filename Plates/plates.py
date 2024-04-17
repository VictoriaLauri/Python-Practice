def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isdigit() or s[1].isdigit():
        return False

    if not s.isalnum():
        return False

    i = 0
    while i < len(s):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            elif not s[i:].isdigit():
                return False
            else:
                return True
        i += 1

    return True

main()
