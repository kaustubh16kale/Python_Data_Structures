def sort_asc_dsc(dict):
    asc_dict=sorted(dict.items(),key=lambda x : x[1])
    dsc_dict=sorted(dict.items(),key = lambda x :x[1],reverse=True)
    return asc_dict,dsc_dict

def dict_add(counter):
    dict={}
    for i in range(counter):
        dict[i]=int(input("Enter the value to be added : "))
    return dict

def main():
    try:
        count=int(input(("Enter the numbers of items to be added in the dictionay : ")))
        dict=(dict_add(count))
        asc_dict,dsc_dict=sort_asc_dsc(dict)
        print(f"The ascendong order sorted dictionary is {asc_dict}, Descending order sorted dictionary is {dsc_dict}")
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()

