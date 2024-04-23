def reverse(input_string):
    return input_string[::-1]

def main():
    try:
        input_string=input("Enter a string to be reversed : ")
        print(reverse(input_string))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()