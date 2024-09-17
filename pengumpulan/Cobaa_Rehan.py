# AHMAD RIKHAN ARBAI
# 230411100192
# Taufik Ikrom Jamil 
# 230411100179
# agatha yasmin rahman
# 230411100156
# n=int(input("masukan angka : "))


# # soal nomer 1
# # Menggunakan dua perulangan bersarang
# for i in range(n):  # Perulangan baris
#     for j in range(1, n+1):  # Perulangan kolom
#         print(j, end=' ')
#     print()  # Pindah ke baris berikutnya setelah selesai mencetak satu baris

# print()


# # soal nomer 2
# # Melakukan perulangan untuk menghasilkan pola
# for i in range(n):
#     for j in range(n, 0, -1):
#         # Mencetak angka dari n hingga 1 pada setiap baris
#         print(j, end=' ')
#     # Pindah ke baris berikutnya setelah mencetak satu baris lengkap
#     print()


# print()

# # soal nomer 3
# # Loop untuk menghasilkan pola bintang
# for i in range(1, n+1):  # Mulai dari baris pertama hingga baris ke-n
#     # Dalam setiap baris, cetak '*' sebanyak i kali, diikuti dengan spasi
#     # Jumlah spasi di setiap baris adalah (n - i)
#     # Akhirnya, cetak newline untuk pindah ke baris berikutnya
#     print("* " * i)

# print()

# # soal nomer 4
# # Loop untuk menghasilkan pola
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# print()

# # soal nomer 5
# # Melakukan perulangan untuk setiap baris
# for i in range(1, n + 1):
#     # Melakukan perulangan untuk setiap angka dalam baris saat ini
#     for j in range(i, 0, -1):
#         # Mencetak angka dengan spasi setelahnya
#         print(j, end=' ')
#     # Pindah ke baris berikutnya
#     print()

















n=int(input("masukkan angka :"))

for i in range(n):
    for j in range(1, n-i+1):
        print("*", end='')
    print()























