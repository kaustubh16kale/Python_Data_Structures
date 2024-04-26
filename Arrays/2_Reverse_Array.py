import array as arr

def reverse_array(inp_array):
    for i in range(len(inp_array)-1,-1,-1):
        print(inp_array[i],end=" ")

def main():
    try :
        inp_array=arr.array('i',[1,2,3,4,5,6,7,8,9])
        reverse_array(inp_array)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()