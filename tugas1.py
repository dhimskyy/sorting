#bubble sort program
def bubble_sort(array):
    for i in range (len(array)):
        for j in range (len(array)-1):
            if array [j + 1] > array [j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array

#titik uji
array = [3.8, 2.4, 4.4, 5.9, 1.1]
print("Nilai :", array)
sorted_array = bubble_sort(array)

print("Nilai terbesar ke terkecil :")
for name in sorted_array:
    print(name)