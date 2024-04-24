def difference_list(lst1,lst2):
    return list(set(lst1)-set(lst2))

def main():
    try:
        lst1=input("Enter the elements to be added in the list seperated by ',' : ")
        lst1=list(map(int,lst1.split(',')))
        lst2=input("Enter the elements to be added in the list seperated by ',' : ")
        lst2=list(map(int,lst2.split(',')))
        print(difference_list(lst1,lst2))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
