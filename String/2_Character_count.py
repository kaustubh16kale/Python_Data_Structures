def count(inp_string):
    char_op = {}
    for char in inp_string:
        if char in char_op:
            char_op[char] += 1
        else:
            char_op[char] = 1
    print(char_op)

def main():
    try:
        inp_string=input("Enter a string to be checked : ")
        count(inp_string)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()