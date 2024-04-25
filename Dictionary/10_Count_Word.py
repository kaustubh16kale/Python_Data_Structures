def count(inp_list,word):
    count=0
    for dictionary in inp_list:
        if dictionary[word]==True:
            count+=1
    return count

def main():
    try :
        Sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
                        False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
        print(count(Sample_data,"success"))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()