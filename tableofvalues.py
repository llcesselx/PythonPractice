def main():
    num = int(input("Enter starting value: "))
    _num = num
    maxnum = num*5
    i = 0

    print("A\t\tA+2\t\tA+4\t\tA+6")
    print("------------------------------")
    while i < maxnum:
        # print(i)
        print("{}\t\t{}\t\t{}\t\t{}".format(num, num+2, num+4, num+6))
        i += _num
        num += _num

    return 0


if __name__ == "__main__":
    main()
