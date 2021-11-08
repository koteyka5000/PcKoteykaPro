def selectionSort(w):
    for i in range(len(w)):
        e = w[i:]
        min_e = min(e)
        ind = w.index(min_e)
        w[i], w[ind] = w[ind], w[i]
    return w


a = selectionSort([9, 2, 6, 4, 7, 8, 0])
print(a)
