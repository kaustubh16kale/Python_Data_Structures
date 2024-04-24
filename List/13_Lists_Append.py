def merge_list(lst1,lst2):
    return lst1+lst2

def main():
    try:
        lst1=input("Enter a words for list1 seperated by ',' : ")
        lst1=list(lst1.split(','))
        lst2=input("Enter words for list2 seperated by ',' : ")
        lst2=list(lst2.split(','))
        print(merge_list(lst1,lst2))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
