def substring_count(input_string,substring):
    
    if len(substring)>len(input_string):
        raise ValueError("Substring cannot be bigger than string")
    if substring=="" and input_string=="":
        raise ValueError("Substring and string cannot be empty")
    
    count=0
    emp_string=""
    for i in range(len(input_string)):
        for j in range(i,len(input_string)):
            emp_string+=input_string[j]
            if emp_string==substring:
                count+=1
        emp_string=""
    return count

def main():
    try:
        input_string=input("Enter the string : ")
        substring=input("Enter the substring to be count : ")
        print(substring_count(input_string,substring))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()