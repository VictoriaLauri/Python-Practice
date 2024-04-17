import sys
from datetime import date
from operator import sub
import inflect
p = inflect.engine()

def main ():

    user_input = input("Date of Birth: ")
    birthday = get_birthday(user_input)
    today = date.today()
    result = sub(today, birthday).days * 1440

    words = p.number_to_words(result, andword="").capitalize()
    print(f"{words} minutes")

def get_birthday(s):
    try:
        birthday = date.fromisoformat(s)
        return birthday
    except ValueError:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()
