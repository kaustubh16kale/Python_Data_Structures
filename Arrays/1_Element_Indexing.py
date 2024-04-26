import numpy as np

def indexing(inp_array,index):
    return inp_array[index]

def add_elements():
    inp=int(input("Enter the numbers of element to be added in the array : "))
    temp_array=np.array([0 for _ in range(inp)])
    for i in range(inp):
        temp_array[i]=int(input("Enter the element to be added in the array : "))
    return temp_array

def main():
    try:
        inp_array=add_elements()
        index=int(input("Enter the index to access the element : "))
        print(indexing(inp_array,index))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()

         