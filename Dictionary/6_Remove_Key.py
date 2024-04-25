def remove_key(dictionary,inp_key):
    del dictionary[inp_key]
    return dictionary

def main():
    try:
        dictionary={1:10,2:20,3:30,4:40,5:50}
        print(dictionary)
        inp_key=int(input("Enter the key to remove : "))
        print(remove_key(dictionary,inp_key))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()

