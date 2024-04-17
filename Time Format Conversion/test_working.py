from working import convert
import pytest


def main():
    test_format()
    test_hrs()
    test_mins()
    test_convert()

def test_format():
    with pytest.raises(ValueError):
        convert("10 AM - 10 PM")

def test_hrs():
    with pytest.raises(ValueError):
        convert("13:00 AM to 17:00 PM")

def test_mins():
    with pytest.raises(ValueError):
        convert("3:60 AM to 1:65 PM")

def test_convert():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("8:30 PM to 3:00 AM") == "20:30 to 03:00"
    assert convert("12:30 PM to 5 PM") == "12:30 to 17:00"

if __name__ == "__main__":
    main()
