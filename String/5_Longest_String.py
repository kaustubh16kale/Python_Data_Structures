def len_count(inp):
    temp=0
    for word in inp:
        if len(word)>temp:
            temp=len(word)
            longest_word=word
    return longest_word

def list_add(counter):
    count=0
    lst=[]
    while count<counter:
        inp=input("Enter a string to add to list : ")
        lst.append(inp)
        count+=1
    return lst

def main():
    try:
        counter=int(input("Enter the number of words to be entered : "))
        lst=list_add(counter)
        longest_word=len_count(lst)
        print(longest_word)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
