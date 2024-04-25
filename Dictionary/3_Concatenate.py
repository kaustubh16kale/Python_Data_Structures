def concatenate(dict1,dict2,dict3):
    new_dict={}
    new_dict.update(dict1)
    new_dict.update(dict2)
    new_dict.update(dict3)
    return new_dict

def main():
    try:
        dict1={1:10, 2:20}
        dict2={3:30, 4:40}
        dict3={5:50,6:60}
        print(concatenate(dict1,dict2,dict3))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()

# def concatenate(*dicts):
#     final_dict={}
#     for item in dicts:
#         final_dict.update(item)
#     return final_dict

# def add_key_values(current_dict):
#     temp_dict={}
#     keys=int(input(f"Enter the numbers of key to be added in dictionary {current_dict}: "))
#     for i in range(1,keys+1):
#         value=input(f"Enter the value for key {i} : ")
#         temp_dict[i]=value
#     return temp_dict

# def dict_create(num_dict):
#     temp_dict_create={}
#     for current_dict in range(1,num_dict+1):
#         temp_dict_create.update(add_key_values(current_dict))
#     return temp_dict_create

# def main():
#     try:
#         num_dict=int(input("Enter the numbers of dictionary to be appended : "))
#         concatenate_dict=dict_create(num_dict)
#         print(concatenate_dict)
#     except Exception as e:
#         print(e)


# if __name__=="__main__":
#     main()
