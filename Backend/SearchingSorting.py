class sorting:
    def insertion_sort(self, lista, index):
        for i in range(1, len(lista)):  # For Traversing through list
            save = lista[i]  # Copying a element to a variable
            j = i  # For getting element smaller than our current index
            while j > 0 and lista[j - 1][index] > save[index]:  # For comparing values
                lista[j] = lista[j - 1]  # Changing variable03 value if element is small
                j -= 1
            lista[j] = save  # Swapping values
        return lista  # return sorted list


class searching:
    def binary_search(self, list, index, item):
        sorted_list = sorting.insertion_sort(list, index)
        min = 0
        max = len(sorted_list) - 1
        while min <= max:
            mid = (min + max) // 2
            if sorted_list[mid][index] == item:
                return sorted_list[mid]
            elif list[mid][index] > item:
                max = mid - 1
            else:
                min = mid + 1
        return
