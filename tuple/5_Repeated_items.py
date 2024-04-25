from collections import Counter

def repeated_items(inp_tuple):
    new_list=[]
    count_items=Counter(inp_tuple)
    print(count_items)
    for key,value in count_items.items():
        if value>1:
            new_list.append(key)
    return new_list
    # return [x for x,count in count_items.items() if count>1]

def main():
    inp_tuple=input("Enter the values to be added in the tuple seperated by ',' : ")
    inp_tuple=inp_tuple.split(',')
    print(repeated_items(inp_tuple))


if __name__=="__main__":
    main()
