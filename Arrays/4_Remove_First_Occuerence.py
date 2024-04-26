import array as arr

def remove_first_occuerence(inp_array,element):
    inp_array=arr.array('i',inp_array)
    inp_array.remove(element)
    return inp_array

def main():
        try:
            inp_list=input("Enter the values to be added in the array seperated by ',' : ")
            inp_list=map(int,inp_list.split(','))
            inp_element=int(input(("Enter the value to be removed from the array : ")))
            print(remove_first_occuerence(inp_list,inp_element))
        except Exception as e:
             print(e)


if __name__=="__main__":
     main()
    
