import time
import sys
def main():
    print("Fahrenheit or Celsius (F/C)?")
    tempScale = input("> ")
    if checkTempScale(tempScale) == 'invalid':
        invalid = "Invalid input\n"
        for letter in invalid:
            sys.stdout.write(letter)
            time.sleep(0.1)
        scaleMsg = "Defaulting to Fahrenheit scale..."
        for letter in scaleMsg:
            sys.stdout.write(letter)
            time.sleep(0.1)
        tempScale = 'F'

    print("What is the temperature?")
    degree = int(input("> "))

    if tempScale == 'F':
        temp = convertToCelsius(degree)
        print("{} deg {} is {} deg C".format(degree, tempScale, temp))

    if tempScale == 'C':
        temp = convertToFahrenheit(degree)
        print("{} deg {} is {} deg F".format(degree, tempScale, temp))

    return 0


def convertToFahrenheit(celsius):
    return celsius * (9/5) + 32


def convertToCelsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)


def checkTempScale(scale):
    scale = scale.upper()
    if scale == 'F':
        return 'F'
    if scale == 'C':
        return 'C'
    else:
        return 'invalid'


if __name__ == "__main__":
    main()