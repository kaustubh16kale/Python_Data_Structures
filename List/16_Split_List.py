def split_list(lst):
    if len(lst)<1:
        raise ValueError("List cannot be empty")
    lst.sort()
    temp_list = []
    new_list = []
    temp_char = lst[0][0]
    for element in lst:
        if element[0] == temp_char:
            temp_list.append(element)
        else:
            new_list.append(temp_list)
            temp_list = [element]  
            temp_char = element[0]  
    new_list.append(temp_list)
    return new_list

def main():
    try:
        lst=input("Enter the words to be added to list seperated by ',' : ")
        lst=list(lst.split(','))
        print(split_list(lst))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
