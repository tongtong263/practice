def main():
    #用户输入文件名
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a source file: ").strip()

    #打开文件
    infile = open(f1, "r")
    outfile = open(f2, "w")

    #拷贝数据
    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    print(countLines,"lines and",countChars,"chars copied")

    infile.close()
    outfile.close()

main()