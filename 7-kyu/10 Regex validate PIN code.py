"""
DESCRIPTION:
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""


def validate_pin(pin: str) -> bool:
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
        return True
    else:
        return False


print(validate_pin("1234"))


def validate_pin2(pin):
    return len(pin) in [4, 6] and pin.isdigit()
