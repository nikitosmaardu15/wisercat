"""Solution."""


def reversed_array_into_the_text_file(filename: str):
    """Read file contents into string."""
    mylist = []  # create list
    with open(filename, 'r') as file:  # reading the file
        for line in file:
            for elements in line:
                if elements.isdigit():  # digital check
                    mylist.append(str(elements))  # add to the list
                else:
                    continue
    print(mylist)
    if len(mylist) > 0:
        print(mylist[::-1])  # reverse list
        with open(filename, 'w') as file:
            for reversed_elements in str(mylist[::-1]):
                file.write(reversed_elements)


if __name__ == '__main__':
    print(reversed_array_into_the_text_file("file.txt"))
