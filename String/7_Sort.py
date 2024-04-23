def sort(inp_list):
    inp_list.sort()
    return inp_list

def add_list(count):
    lst=[]
    counter=0
    while counter<count:
        inp=input("Enter the Word to be added : ")
        lst.append(inp)
        counter+=1
    return sort(lst)

def main():
    try :
        count=int(input("Enter the number of words to be added in the list: "))
        print(add_list(count))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()

