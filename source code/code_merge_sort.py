def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Membagi array menjadi dua bagian
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Rekursif untuk bagian kiri
        merge_sort(right_half)  # Rekursif untuk bagian kanan

        i = j = k = 0

        # Menggabungkan dua bagian array yang telah diurutkan
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menambahkan sisa elemen jika ada
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Contoh data kode telepon negara
kode_negara = ["1", "7", "20", "27", "30", "31", "32", "33", "34", "36", "39", "40", "41", "44", "45", "46", "47", "48", "49", "51", "52", "53", "54", "55", "56"]
print("Sebelum sorting:", kode_negara)
merge_sort(kode_negara)
print("Setelah sorting:", kode_negara)