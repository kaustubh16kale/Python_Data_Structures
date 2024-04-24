def remove_duplicate(lst):
    return list(set(lst))

def main():
    try:
        lst=input("Enter the elements to be added in the list seperated by ',' : ")
        lst=list(map(int,lst.split(',')))
        print(remove_duplicate(lst))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()