def sort_tupples(lst):
    for i in range(len(lst)):
        for j in range(i,len(lst)-1):
            if lst[j][-1] > lst[j + 1][-1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def main():
    try:
        print(sort_tupples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()