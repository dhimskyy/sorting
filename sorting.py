import timeit

print("Ascending")
print(" ")

#insection sort
# def insertion_sort(array):
#     start = timeit.default_timer()
#     for i in range(1, len(array)):
#         item = array [i]
#         j = i - 1
        
#         while j >= 0 and array[j] > item:
#             array[j + 1] = array[j]
#             j -= 1
        
#         array[j + 1] = item
        
#     stop = timeit.default_timer()
#     print(f"Inserttion sort succcesfull! Elapsed time: + {stop - start}")
#     return array

# list_1 = [2, 4, 6, 12, 26, 46, 22]
# print(f"before: {list_1}")
# insertion_sort(list_1)
# print(f"After: {list_1}")

#bubble sort
# def bubble_sort(array):
#     start = timeit.default_timer()
#     for i in range(len(array)):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
                
#     stop = timeit.default_timer()
#     print(f"Bubble sort succcesfull! Elapsed time: {stop - start}")
#     return array

# list_1 = [2, 4, 6, 12, 26, 46, 22]
# print(f"before: {list_1}")
# bubble_sort(list_1)
# print(f"After: {list_1}")

#selection sorting
# def selection_sort(array):
#     start = timeit.default_timer()
#     for i in range(len(array)):
#         min_index = i
#         for j in range(i+1, len(array)):
#             if array[min_index] < array[j]:
#                 min_index = j
#         array[i], array[min_index] = array[min_index], array[i]
    
#     stop = timeit.default_timer()
#     print(f"Selection sort succcesfull! Elapsed time: {stop - start}")
#     return array

# list_1 = [2, 4, 6, 12, 26, 46, 22]
# print(f"before: {list_1}")
# selection_sort(list_1)
# print(f"After: {list_1}")
