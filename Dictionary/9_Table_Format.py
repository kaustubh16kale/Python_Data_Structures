def check(dictionary):
    print("Keys | Values")
    for i,j in dictionary.items():
        print(f"{i} | {j} ")

def create_dictionary(count):
    new_dict={}
    for i in range(count):
        new_dict[input("Enter the key : ")]=input("Enter the value : ")
    return new_dict

def main():
    try:
        count=int(input("Enter the number of keys to be added : "))
        new_dict=create_dictionary(count)
        check(new_dict)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()

