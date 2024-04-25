def count(dictionary):
    count=0
    for i,j in dictionary.items():
        if type(j)==list:
            count+=1
    return count

def main():
    try:
        inp_dict={1:[1,2,3],2:5,3:[2,4]}
        print("inp_dictionary is ",inp_dict)
        print(count(inp_dict))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
