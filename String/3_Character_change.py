def change(inp_string):
    emp_string=""
    first_var=inp_string.split()[0][0]
    emp_string+=first_var
    for i in range(1,len(inp_string)):
        if inp_string[i]==first_var:
            emp_string+="$"
        else:
            emp_string+=inp_string[i]
    return emp_string

def main():
    try:
        inp_string=input("Enter a string to replace the another occuerence of the first character : ")
        output=change(inp_string)
        print(output)
    except Exception as e:
        print(e)
    

if __name__=="__main__":
    main()