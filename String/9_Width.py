import textwrap

def width_adjust(input_string,width=2):
    generate_text=textwrap.fill(input_string,width)
    return generate_text

def main():
    try:
        input_string=input("Enter a string : ")
        print(width_adjust(input_string))
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()
