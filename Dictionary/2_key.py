def display(dictionary):
    return dictionary

def count(counter):
    dictionary={}
    for i in range(1,counter+1):
        value=input(f"Enter the value for key {i} : ")
        dictionary[i]=value
    return dictionary

def main():
    try:
        counter=int(input("Enter number of Keys to be appended in the dictionary : "))
        dict_values=count(counter)
        print(display(dict_values))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
        
