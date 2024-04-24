def minimum_element(lst):
    minimum_element=lst[0]
    for element in lst:
        if minimum_element>element:
            minimum_element=element
    return minimum_element

def main():
    try:
        lst=input("Enter the elements to be added in the list seperated by ',' : ")
        lst=list(map(int,lst.split(',')))
        print(minimum_element(lst))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
