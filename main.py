from luhnAlgorithm import checksum

def main():
    ccNumber = input('Please enter your credit card number: ')
    if checksum(ccNumber) == True:
        print('This card is valid.')
    else:
        print('This card is not valid.')
    return None

if __name__ == "__main__":
    main()

