def intersection(set1,set2):
    return set1.intersection(set2)

def main():
    try:
        set1=input("Enter the values to be added in set1: ")
        set2=input("Enter the values to be added in set2: ")
        set1=set(set1.split(','))
        set2=set(set2.split(','))
        print(intersection(set1,set2))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()