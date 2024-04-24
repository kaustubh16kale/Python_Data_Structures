def check(lst1,lst2):
    if len(lst1)!=len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1==lst2:
            return True
        else:
            lst2.append(lst2[0])
            lst2.pop(0)
    return False

def main():
    try:
        lst1=input("Enter the elements of list 1 seperated by ',' : ")
        lst1=list(map(int,lst1.split(',')))
        lst2=input("Enter the elements of list 1 seperated by ',' : ")
        lst2=list(map(int,lst2.split(',')))
        if check(lst1,lst2):
            print("Both the list are circularly identical")
        else:
            print("Both the list are not circularly idenctical")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
        
            


