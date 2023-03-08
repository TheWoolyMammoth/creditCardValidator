import pytest

def checksum(cardNumber):

    # split() <- splits up string up by whitespace (or other seperator if specified) "".join() joins an iterable and removes any whitespaces left and replaces with ""
    listDigitsCard = list("".join(cardNumber.split()))
    luhnListDigits = []
    flipper = 0
    listDigitsCard.reverse()
    for digit in listDigitsCard:
        if flipper == 0:
            flipper = 1
            luhnListDigits.append(int(digit))
            continue
        else:
            flipper = 0
            doubled = int(digit) * 2
            if doubled > 9:
                doubled = sumDigits(doubled)
            luhnListDigits.append(doubled)
    if sum(luhnListDigits) % 10 == 0:
        return True
    else:
        return False

def sumDigits(digit):
    stringDigit = list(str(digit))
    return int(stringDigit[0]) + int(stringDigit[1])


def test_sumDigits_0():
    assert sumDigits('10') == 1

def test_sumDigits_1():
    assert sumDigits('54') == 9

def test_sumDigits_2():
    assert sumDigits('35') == 8

def test_checksum_0():
    assert checksum('378282246310005') == True

def test_checksum_1():
    assert checksum('4111111111111119') == False

def test_checksum_2():
    assert checksum('36123409853619') == True