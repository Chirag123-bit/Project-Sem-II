class sorting:
    def insertion_sort(lista,index):
        for i in range(1, len(lista)):
            save = lista[i]
            j = i
            while j > 0 and lista[j - 1][index] > save[index]:
                lista[j] = lista[j - 1]
                j -= 1
            lista[j] = save
        return lista


class searching:
    def binary_search(self, list,index,item):
        sorted_list = sorting.insertion_sort(list,index)
        print(sorted_list)
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




