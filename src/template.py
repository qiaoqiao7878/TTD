class Template:
    @classmethod
    def replace(cls, my_input: str, dictionary):
        index = my_input.find("$")
        if index == -1 or index == len(my_input):
            return my_input

        if my_input[index + 1] == "{":
            close_curly_braces_index = my_input[index:].find("}") + index
            word = my_input[index + 2 : close_curly_braces_index]
            if word in dictionary:
                output = (
                    my_input[:index]
                    + dictionary[word]
                    + Template.replace(
                        my_input[close_curly_braces_index + 1 :], dictionary
                    )
                )
                return output
            else:
                return my_input
        else:
            return my_input[: index + 1] + Template.replace(
                my_input[index + 1 :], dictionary
            )
