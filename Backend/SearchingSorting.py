class sorting:
    """This class is responsible for performing searching and sorting operation in our database"""

    def insertion_sort(self, lista, index):
        """This method performs insertion sort in our database
        Here,
        lista = List to be sorted
        index = Index on the basis of which the sorting is to be performed
        If index = 0, sorting will be performed on the basis of First Name
        If index = 1, sorting will be performed on the basis of Last Name"""
        for i in range(1, len(lista)):  # For Traversing through list
            save = lista[i]  # Copying a element to a variable
            j = i  # For getting element smaller than our current index
            while j > 0 and lista[j - 1][index] > save[index]:  # For comparing values
                lista[j] = lista[j - 1]  # Changing variable value if element is small
                j -= 1
            lista[j] = save  # Swapping values
        return lista  # return sorted list


class searching:
    def linear_search(self, list, index, item):
        """This method performs linear search in our database
                Here,
                list = List to be searched from
                index = Index on the basis of which the searching is to be performed
                If index = 0, searching will be performed on the First Name
                If index = 1, searching will be performed on the Last Name
                And,
                Item = Item to search for"""
        search_result = []  # Empty list to store result
        for i in list:  # Looping through list
            if i[index] == item:  # Matching items in our list
                search_result.append(i)  # Adding item to our list above if matched
        return search_result  # Returning list which contains search results
