def check_element(lst1,lst2):
    for i in lst1:
        if i in lst2:
            return True
    else:
        return False
    
def main():
    try:
        lst1=input("Enter the elements to be added in the list seperated by ',' : ")
        lst1=list(lst1.split(','))
        lst2=input("Enter the elements to be added in the list seperated by ',' : ")
        lst2=list(lst2.split(','))
        print(check_element(lst1,lst2))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
