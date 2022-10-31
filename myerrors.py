class MyError(Exception):
    def __init__(self):
        self.txt = 1

if __name__ == "__main__":
    a = input("Input positive integer: ")

    try:
        a = int(a)
        if a < 0:
            raise MyError("You give negative!")
    except ValueError:
        print("Error type of value!")
    except MyError as mr:
        print(mr)
    else:
        print(a)