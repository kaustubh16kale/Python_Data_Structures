def multiplier_list(lst,multiplier):
    for i in range(len(lst)):
        lst[i]=lst[i]*multiplier
    return lst

def main():
    try:
        lst=input("Enter the elements to be added in the list seperated by ',' : ")
        multiplier=(input("Enter the multiplier : "))
        multiplier=int(multiplier)
        lst=list(map(int,lst.split(',')))
        print(multiplier_list(lst,multiplier))
    except ValueError:
        print("Enter a intiger only for multiplier and list elements")


if __name__=="__main__":
    main()