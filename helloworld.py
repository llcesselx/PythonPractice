import time

def main():
    users = []
    yorn = 'y'
    print("Hello...")
    time.sleep(1)
    while yorn == 'y':
        user = getname()
        users.append(user)
        print("Hello, {}, are there more users (y/n)?".format(user))
        yorn = input("> ")
    print("Users:")
    count = 1
    for i in users:
        print("{}. {}".format(count, i))
        count += 1
    return 0

def getname():
    print("What is your name?:")
    name = input("> ")
    return name

if __name__ == "__main__":
    main()