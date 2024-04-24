import numpy as np

def remove_index(lst,indices):
    lst=np.array(lst)
    lst=np.delete(lst,indices)
    return lst

def main():
    try:
        lst=input("Enter the elements to be added in the list seperated by ',' : ")
        lst=list(map(int,lst.split(',')))
        indices=input("Enter the indices to be removed from the list seperated by ',' : ")
        indices=list(map(int,indices.split(',')))
        print(remove_index(lst,indices))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
