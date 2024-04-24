import copy

def copy_list(lst):
    return copy.copy(lst)

def main():
    try:
        lst=input("Enter the elements to be added in the list seperated by ',' : ")
        lst=list(map(int,lst.split(',')))
        print(copy_list)
        print("Copy created ")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
