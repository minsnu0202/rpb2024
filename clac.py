def main():
    print("Let's implement division. Type two numbers for x and y")

    x = int(input("x > "))
    y = int(input("y > "))
    if y!=0 :
        print("%d / %d = %0.3f" % (x, y, divide(x, y)))
    else : print("Error: cannot divide by zero.")


def add(a, b):
    return a + b


# TODO: divide() 함수 정의
def divide(x,y):
    return x/y        

if __name__ == "__main__":
    main()
