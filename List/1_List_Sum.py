def list_sum(lst):
    elements_sum=0
    for element in lst:
        elements_sum+=element
    return elements_sum

def main():
    try:
        lst=input("Enter the elements to be added into the list seperated by ',' : ")
        lst=list(map(int,lst.split(",")))
        print(list_sum(lst))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()

