import array as arr

def count(inp_array,inp_element):
    count=0
    inp_array=arr.array('i',inp_array)
    for element in inp_array:
        if element==inp_element:
            count+=1
    return count

def main():
    try :
        inp_list=input("Enter the values to be added in the array seperated by ',' : ")
        inp_list=map(int,inp_list.split(','))
        inp_element=int(input(("Enter the value to be count in the array : ")))
        print(count(inp_list,inp_element))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()