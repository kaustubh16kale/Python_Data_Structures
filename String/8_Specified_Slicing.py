def slicing(input_string,symbol):
    for i in range(1,len(input_string)):
        if symbol in input_string[-i:]:
            return input_string[-i+1:]

def main():
    try:
        symbol=input("Enter the seperator symbol : ")
        input_string=input("Enter the string : ")
        print(slicing(input_string,symbol))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()