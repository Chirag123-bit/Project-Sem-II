class sorting:
    def insertion_sort(self, lista, index):
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
        search_result = []
        for i in list:
            if i[index] == item:
                search_result.append(i)
        return search_result

