import random
import time


def main():
    print("How many dice to roll?")
    numofdice = int(input("> "))
    while True:
        for i in range(numofdice):
            roll = rolldie()
            print("Roll {}: {}".format(i, roll))
        again = input("Roll again (y/n)?: ")
        if again == 'y' or again == 'Y' or again == 'yes' or again == 'Yes':
            continue
        elif again == 'n' or again == 'N' or again == 'no' or again == 'No':
            break
        else:
            print("Unknown command. Exiting program...")
            time.sleep(1)
            break
    print("Thanks for rolling!")
    time.sleep(1)
    print("Goodbye!")
    return 0


def rolldie():
    roll = random.randint(1, 6)
    return roll


if __name__ == "__main__":
    main()