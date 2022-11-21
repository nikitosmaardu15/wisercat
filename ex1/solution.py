"""WiserCat."""


def reversed_array_into_the_text_file(filename: str):
    """Read file contents into string."""
    mylist = []  # create list
    with open(filename, 'r', encoding='utf-8') as file:  # reading the file
        for line in file:
            if len(line) > 2:
                divide = line[1:-1].split(",")  # divide by a comma
                for elements in divide:
                    integer = int(elements)
                    mylist.append(integer)  # add to the list
            else:
                print("Empty!!!")
    print(mylist)
    if len(mylist) > 0:
        print(mylist[::-1])  # reverse list
        with open(filename, 'w', encoding='utf-8') as file:
            for reversed_elements in str(mylist[::-1]):
                file.write(reversed_elements)


if __name__ == '__main__':
    print(reversed_array_into_the_text_file("file.txt"))
