#交互式循环代码
'''
def main():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = eval(input("enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more number (yes or no)? ")
    print("\nThe avalue of the numebr is", sum/count)

main()
'''
#哨兵循环，设置一个value来结束循环
def main():
    sum = 0.0
    count = 0
    x = eval(input("Enter a number (negative to quit) >> "))
    while x >= 0:
        sum = sum + x
        count = count + 1
        x = eval(input("Enter a number (negative to quit) >> "))
    print("\nThe avalue of the numebr is", sum / count)
main()



#文件循环代码for
def main():
    fileName = input("what file are the numbers in? ")
    infile = open(fileName, 'r')
    sum = 0
    count = 0
    for line in infile:
        sum = sum + eval(line)
        count = count + 1
    print("\nThe average of the number is", sum /count)
main()


#文件循环代码while
def main():
    fileName = input("what file are the numbers in? ")
    infile = open(fileName, 'r')
    sum = 0
    count = 0
    line = infile.readline()
    while line != "":
        sum = sum + eval(line)
        count = count + 1
    print("\nThe average of the number is", sum /count)
main()

#