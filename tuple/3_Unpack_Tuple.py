def unpack_tuple(inp_tuple):
    if len(inp_tuple)>3:
        raise ValueError("Enter only three values in input")
    else:
        a,b,c=inp_tuple
        return a,b,c

def main():
    try:
        inp_tuple=input("Enter three int values seperated by',' : ")
        inp_tuple=inp_tuple.split(',')
        a,b,c=(unpack_tuple(inp_tuple))
        print(f"The values of a : {a},b : {b}, c : {c}")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()