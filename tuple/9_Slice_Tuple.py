def slice_tuple(inp_tuple,start,end):
    new_tuple=inp_tuple[start:end]
    return new_tuple

def main():
    try:
        inp_tuple=input("Enter the values to be added inside the tuple seperated by ',' : ")
        inp_tuple=inp_tuple.split(',')
        start=int(input("enter a slicing start index : "))
        end=int(input("Enter a slicing stop index : "))
        print(slice_tuple(inp_tuple,start,end))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()