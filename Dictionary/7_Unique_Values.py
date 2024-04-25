def unique_values(dictionary):
    set_values=set(dictionary.values())
    return set_values

def main():
    try:
        dictionary={1:10,2:10,3:30,4:40,5:100}
        print(unique_values(dictionary))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
