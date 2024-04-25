def iterate(dictionary):
    for i,j in dictionary.items():
        print(f"The value for key {i} is {j} ")

def add_key_value(count):
    temp_dict={}
    for i in range(1,count+1):
        value=input(f"Enter the value for key {i} : ")
        temp_dict[i]=value
    return temp_dict

def main():
    try:
        count=int(input("Enter the number of keys to be added in dictionary : "))
        new_dict=add_key_value(count)
        iterate(new_dict)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
