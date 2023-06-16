def td(db):
    jb = int(input("Masukkan total buku: "))
    for i in range(jb):
        jubu = input(f"Masukkan judul buku ke-{i + 1}: ")
        db.append(jubu)
    print("Data buku berhasil ditambahkan.")
    
#variabel array
db = []
td(db)

#insertion sort ascending program
def isascending(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

#insertion sort descending program
def isdescending(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

#print menu
while True:
    print("<=====Ururtkan=====>")
    print("1. Insertion Ascending")
    print("2. Insertion Descending")
    pilihan = int(input("Pilih: "))

#if statement pilihan
    if pilihan == 1:
        ub = isascending(db)
        print("Sorting buku secara ascending: ")
        for i, buku in enumerate(ub):
            print(f"Indeks buku ke-{i}: {buku}")
        break
    elif pilihan == 2:
        ub = isdescending(db)
        print("Sorting buku secara descending: ")
        for i, buku in enumerate(ub):
            print(f"Indeks buku ke-{i}: {buku}")
        break
    else:
        print("Input tidak valid!, Silahkan coba lagi.")
        
        