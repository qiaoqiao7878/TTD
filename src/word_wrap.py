import math


class Wrapper:
    def __init__(self) -> None:
        pass

    def wrap(self, string: str, n_col: int):
        if len(string) <= n_col:
            return string
        if n_col <= 0:
            raise ValueError

        last_space_index = string[:n_col].rfind(" ")
        if last_space_index != -1:
            return (
                string[:last_space_index]
                + "\n"
                + self.wrap(string[last_space_index:].strip(), n_col)
            )
        else:
            return string[:n_col] + "\n" + self.wrap((string[n_col:]).strip(), n_col)
