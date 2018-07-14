# Validates the data type of the passed value to be integer.
def isInt(param):
    try:
        param = int(param)
        return True
    except TypeError:
        return False


# Validates an integer to be in a range (optional).
def validateInt(param, min_limit=0, max_limit=100):
    if isInt(param):
        if min_limit <= param <= max_limit:
            return True
        else:
            return False
    else:
        return False


# Grabs the 0-based index position of the element to be found in the array.
# More likely based on linear search.
def getIndexOfElement(element, *array):
    if element not in array:
        raise ReferenceError("Element your looking for is not in the array.")
    else:
        for i in range(len(array)):
            if array[i] == element:
                return i


# Parses an array into a string, explicitly removing the unwanted characters.
def array_to_string(array):
    return str(array).replace("[", "").replace("]", "")


class Menu:
    """
    This menu is constructed to provide a flexible textual menu for the developer. Although this may not have
    pagination functionality, it's purpose is to make typical menus more sustainable and consistent.

    :argument menu_width: When forming an menu object, it is mandatory that you pass the menu-width argument.
                         It states how wide your menu will be. But this argument will not affect the flexibility of the menu,
                         unless the value passed is a negative or 0 integer.
    """

    def __init__(self, menu_width):
        self.menu_width = menu_width
        self.data = []
        self.wall_char = "|"

    # Sets the title of the menu.
    def setTitle(self, title):
        self.data.append(("title", title))

    # Adds an item to the data set.
    def addItem(self, option, option_no=None):
        if option_no is not None:
            self.data.append((option_no, option))
        else:
            self.data.append((len(self.data), option))

    # Deletes an option.
    def deleteItem(self, option):
        for (i, key, item) in enumerate(self.data):
            if key == option:
                self.data.pop(i)
                return True
        return False

    # Prints out the menu with the values that are obtained with the setter methods.
    def print_menu(self):
        def line(chr):
            print('{0} {1} {0}'.format(self.wall_char, chr * self.menu_width))

        line('¯')
        line(' ')

        for (key, item) in self.data:
            item = '({}) {}'.format(key, item)
            chunks = len(item)
            chunk_size = int(chunks / (chunks / self.menu_width))
            lines = [item[idx:idx + chunk_size] for idx in range(0, chunks, chunk_size)]

            print("\n".join(
                ['{0} {1:{2}s} {0}'.format(self.wall_char, line.replace("(title)", ""), self.menu_width) for line in
                 lines]))

            if key == "title":
                line(' ')
                line('-')
            line(' ')
        line('_')

    # Gets the option from the user after printing the menu. It may need to be looped to get the acceptable option.
    @property
    def getOption(self):
        self.print_menu()
        answer = input()
        options = [str(option).replace("title", "") for (option, content) in enumerate(self.data)]
        if answer in options:
            for option in options:
                if answer == option:
                    return option
        else:  # We basically loop the function logically until we get an acceptable option.
            return self.getOption
