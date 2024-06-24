class TwoDArray:
    def __init__ (self, array: list):
        self.__array = array

    def add(self, *args):
        self.__array.append(list(args))

    def get(self):
        return self.__array

    def sort(self):
        for i in range(len(self.__array)):
            self.__array[i].sort(reverse=True)

    def get_quantity_of_elements(self):
        counter = 0
        for i in range(len(self.__array)):
            counter += len(self.__array[i])
        return (f'{len(self.__array)} - quantity of strings \n'
                f'{counter} - quantity of elements in strings\n'
                f'{counter + len(self.__array)} - total number of elements')

    def set_increase(self, increment):
        for i in range(len(self.__array)):
            for j in range(len(self.__array[i])):
                self.__array[i][j] += increment

    prop = property(get_quantity_of_elements, set_increase)


new_array = TwoDArray([[1, 3, 2], [4, 8, 5]])
new_array.add(1, 7, 2, 9)
print(new_array.get())
new_array.sort()
print(new_array.get())
new_array.prop = 3
print(new_array.prop)
print(new_array.get())