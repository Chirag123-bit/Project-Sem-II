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
