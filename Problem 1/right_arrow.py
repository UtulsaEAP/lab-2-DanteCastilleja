def right_arrow():
    print("base_char = ")
    base_char = input()
    print("head_char = ")
    head_char = input()

    row1 = base_char * 6 + head_char
    row2 = base_char * 6 + head_char * 2
    row3 = base_char * 6 + head_char * 3
    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()