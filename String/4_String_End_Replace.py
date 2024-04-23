def string_change(inp_string):
    output=""
    if len(inp_string)<3:
        return inp_string
    elif inp_string[-3:]=="ing":
        return inp_string[:len(inp_string)]+"ly"
    else:
        output+=inp_string
        output+="ing"
        return output

def main():
    try:
        inp_string=input("Enter a string : ")
        output_string=string_change(inp_string)
        print(output_string)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
