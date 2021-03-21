#solution1
def main():
    n = eval(input("how many numbers are there?"))
    #assign fist valve to varibale max
    max = eval(input("Enter a number >> "))

    for i in range(n-1):
        x = eval(input("Enter a number >> "))
        if  x > max:
            max =x
        print("The largest value is, max")

main()