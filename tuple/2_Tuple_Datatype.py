def data_type_tuple(inp_tuple):
    print(type(inp_tuple))
    return inp_tuple

def main():
    try:
        inp_tuple=(input("Enter int values to be added in the tuple seperated by ',' : "))
        inp_tuple=tuple(map(int,inp_tuple.split(',')))
        print(data_type_tuple(inp_tuple))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()