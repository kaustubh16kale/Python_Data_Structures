def count(inp_string):
    new_dict={}
    for item in inp_string:
        if item in new_dict:
            new_dict[item]+=1
        else:
            new_dict[item]=1
    return new_dict

def main():
    try :
        inp_string=input("Enter a string : ")
        print(count(inp_string))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
    

    