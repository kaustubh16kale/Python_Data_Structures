def upper_lower(inp_string):
    upper_case=inp_string.upper()
    lower_case=inp_string.lower()
    return upper_case,lower_case

def main():
    try:
        inp_string=input("Enter a string : ")
        upper,lower=upper_lower(inp_string)
        print(f"The upper case of the entered string is : {upper}")
        print(f"The lower case of the entered string is : {lower}")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
