def add_numbers(input: str):
    if input == "":
        return 0
    if input[:2] == "//":
        index = input.find("\n")
        delimiter = input[2:index]
        input = input[index:]
    else:
        delimiter = ","
    input = input.replace("\n", delimiter)

    number_list_str = input.split(delimiter)
    sum_of_numbers = 0
    for number_str in number_list_str:
        if number_str == "":
            continue
        sum_of_numbers += int(number_str)
    return sum_of_numbers
