def common_element(lst1,lst2):
    for element in lst1:
        if element in lst2:
            print(element,end=" ")

def main():
    try:
        lst1=input("Enter the elements of list 1 seperated by ',' : ")
        lst1=list(map(int,lst1.split(',')))
        lst2=input("Enter the elements of list 1 seperated by ',' : ")
        lst2=list(map(int,lst2.split(',')))
        common_element(lst1,lst2)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()