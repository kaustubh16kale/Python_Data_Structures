def count_elements(lst):
    count=0
    for element in lst:
        if len(element)>=2:
            if element[0]==element[-1]:
                count+=1
    return count

def main():
    try:
        lst=input("Enter the elements to be added in the list seperated by ',' : ")
        lst=list(map(str,lst.split(',')))
        print(count_elements(lst))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()