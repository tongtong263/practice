#solution1
def main():
    n = eval(input("how many numbers are there?"))
    #assign fist valve to varibale max
    max = eval(input("Enter a number >> "))

    for i in range(n-1):
        x = eval(input("Enter a number >> "))
        if  x > max:
            max =x
        print("The largest value is", max)

main()

'''
#solution2 (shortest one)
def main():
    x1,x2,x3=eval(input("Please enter three values: "))
    print("the largest value is: ", max(x1,x2,x3))
main()
'''