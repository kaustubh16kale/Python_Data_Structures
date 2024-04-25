def generate(inp_num):
    temp_dict={}
    for i in range(1,inp_num+1):
        temp_dict[i]=i*i
    return temp_dict

def main():
    try :
        inp_num=int(input("Enter a number to generate the dictionary upto : "))
        print(generate(inp_num))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()