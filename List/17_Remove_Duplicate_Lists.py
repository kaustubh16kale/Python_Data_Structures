def check(lst):
    new_list=[]
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

def main():
    try:
        # lst=input("Enter the words to be added to list seperated by ',' : ")
        # lst=list(lst.split(','))
        print("sample_input is: ",[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])
        print(check([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()