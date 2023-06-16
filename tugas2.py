def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
            array[min_index], array[i] = array[i], array[min_index]
    return array

array = ['SpongeBob', 'Patrick', 'Plankton', 'Sandy', 'Squidward', 'Garry', 'Mr.Crab']
sorted_array = selection_sort(array)

print("Nama sesuai abjad (A-Z): ")
for name in sorted_array:
    print(name)