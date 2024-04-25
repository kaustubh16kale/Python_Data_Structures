def create_tupple(inp):
    print(type(inp))
    return inp

def main():
    try:
        inp_tuple=input("Enter the values to be added in tuple : ")
        inp_tuple=tuple(inp_tuple.split(','))
        print(create_tupple(inp_tuple))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()