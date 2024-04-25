def max_min(set1):
    max_element,min_element=max(set1),min(set1)
    return max_element,min_element

def main():
    try: 
        set1=input("Enter the values to be added in set1: ")
        set1=set(set1.split(','))
        max_element,min_element=max_min(set1)
        print(f"Max element in set is {max_element} ,Min element in set is {min_element} ")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()