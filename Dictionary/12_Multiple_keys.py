def check_key(dictionary,inp_key):
    for key in dictionary.keys():
        if inp_key==key:
            return True
    else:
        return False

def main():
    try:
        inp_dict={1:10,2:20,3:30,4:40,5:50,6:60,7:70}
        print(f"input dictionary is {inp_dict} ")
        inp_key=int(input("Enter a key to be checked : "))
        if check_key(inp_dict,inp_key):
            print("Key is present in the dictionary ")
        else:
            print("Key is not present in the dictionary : ")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()

