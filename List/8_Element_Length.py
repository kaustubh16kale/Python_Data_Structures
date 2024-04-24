def element_length(lst,length):
    new_lst=[]
    for element in lst:
        if len(element)>length:
            new_lst.append(element)
    return new_lst

def main():
    try:
        lst=input("Enter the elements to be added in the list seperated by ',' : ")
        lst=list(map(str,lst.split(',')))
        length=input("Enter the length of the words to be filtered : ")
        length=int(length)
        print(element_length(lst,length))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()

