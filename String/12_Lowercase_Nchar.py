def lower(input_string,num_char):
    if num_char>len(input_string):
        raise ValueError("Enter valid numbers of char : ")
    else:
        return input_string[:num_char].lower()+input_string[num_char:]

def main():
    try:
        input_string=input("Enter the string : ")
        num_char=int(input("Enter the nums to be capitalize : "))
        print(lower(input_string,num_char))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()