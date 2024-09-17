from datetime import datetime

menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Sate Ayam": 20000,
    "Bakso": 13000,
    "Es Teh": 5000
}

riwayat_pembelian = []

def tampilkan_menu():
    print("\nSelamat datang di Restoran Sederhana")
    print("1. Beli Makanan")
    print("2. Tampilkan Riwayat Pembelian")
    print("3. Update Pembelian")
    print("4. Hapus Pembelian")
    print("5. Metode Pembayaran")
    print("6. Tampilkan Menu Makanan")
    print("7. Cari Riwayat Pembelian")
    print("8. Tampilkan Statistik")
    print("9. Keluar")

def tampilkan_menu_makanan():
    print("\nMenu Makanan:")
    for i, (makanan, harga) in enumerate(menu_makanan.items(), start=1):
        print(f"{i}. {makanan} - Rp {harga}")

def beli_makanan():
    tampilkan_menu_makanan()
    pilihan = int(input("Silakan pilih makanan: "))

    if 1 <= pilihan <= len(menu_makanan):
        jenis_makanan = list(menu_makanan.keys())[pilihan - 1]
        jumlah = int(input(f"Berapa porsi {jenis_makanan} yang ingin Anda pesan: "))

        total_harga = jumlah * menu_makanan[jenis_makanan]
        tanggal_pembelian = input("Masukkan tanggal pembelian (YYYY-MM-DD): ")

        pembelian_data = {
            "Makanan": jenis_makanan,
            "Jumlah": jumlah,
            "Total Harga": total_harga,
            "Tanggal": tanggal_pembelian,
            "Status Pembayaran": None
        }

        riwayat_pembelian.append(pembelian_data)
        print(f"Terima kasih telah memesan {jumlah} porsi {jenis_makanan} seharga Rp {total_harga} pada tanggal {tanggal_pembelian}.")
    else:
        print("Pilihan tidak valid, silakan pilih makanan yang tersedia.")

def tampilkan_riwayat_pembelian():
    print("\nRiwayat Pembelian:")
    for pembelian in riwayat_pembelian:
        status_pembayaran = pembelian.get("Status Pembayaran")
        tanda_pembayaran = "Sudah Dibayar" if status_pembayaran == "Sudah Dibayar" else "Belum Dibayar"
        print(f"Makanan: {pembelian['Makanan']}, Jumlah: {pembelian['Jumlah']} porsi, Total Harga: Rp {pembelian['Total Harga']} - {tanda_pembayaran}")

def update_pembelian():
    tampilkan_riwayat_pembelian()
    if riwayat_pembelian:
        index = int(input("Pilih indeks pembelian yang ingin diupdate (Mulai dari 0): "))
        if 0 <= index < len(riwayat_pembelian):
            if riwayat_pembelian[index].get("Status Pembayaran") is None:
                makanan = riwayat_pembelian[index]["Makanan"]
                jumlah_baru = int(input(f"Masukkan jumlah porsi baru untuk {makanan}: "))
                total_harga_baru = jumlah_baru * menu_makanan[makanan]
                riwayat_pembelian[index]["Jumlah"] = jumlah_baru
                riwayat_pembelian[index]["Total Harga"] = total_harga_baru
                print(f"Pembelian berhasil diupdate.")
            else:
                print("Pembelian sudah dibayar, tidak bisa diupdate.")
        else:
            print("Indeks tidak cocok.")
    else:
        print("Belum ada riwayat pembelian.")

def hapus_pembelian():
    tampilkan_riwayat_pembelian()
    if riwayat_pembelian:
        index = int(input("Pilih indeks pembelian yang ingin dihapus (Mulai dari 0): "))
        if 0 <= index < len(riwayat_pembelian):
            if riwayat_pembelian[index].get("Status Pembayaran") is None:
                del riwayat_pembelian[index]
                print("Pembelian berhasil dihapus.")
            else:
                print("Pembelian sudah dibayar, tidak bisa dihapus.")
        else:
            print("Indeks tidak cocok.")
    else:
        print("Belum ada riwayat pembelian.")

def bayar():
    tampilkan_riwayat_pembelian()

    if riwayat_pembelian:
        unpaid_transactions = [pembelian for pembelian in riwayat_pembelian if pembelian.get("Status Pembayaran") is None]

        if unpaid_transactions:
            print("Anda akan membayar untuk semua pembelian di atas.")
            print("\nMetode Pembayaran:")
            print("1. Tunai")
            print("2. Kartu Debit")

            metode_pembayaran = int(input("Silakan pilih metode pembayaran (1 atau 2): "))

            if metode_pembayaran == 1:
                total_harga_semua = sum(pembelian["Total Harga"] for pembelian in unpaid_transactions)
                print(f"\nPembayaran tunai sebesar Rp {total_harga_semua} diterima. Terima kasih!")

                for pembelian in unpaid_transactions:
                    pembelian["Status Pembayaran"] = "Sudah Dibayar"
                    pembelian["Metode Pembayaran"] = "Tunai"

            elif metode_pembayaran == 2:
                total_harga_semua = sum(pembelian["Total Harga"] for pembelian in unpaid_transactions)
                print(f"\nPembayaran dengan Kartu Debit sebesar Rp {total_harga_semua} diterima. Terima kasih!")

                for pembelian in unpaid_transactions:
                    pembelian["Status Pembayaran"] = "Sudah Dibayar"
                    pembelian["Metode Pembayaran"] = "Kartu Debit"

            else:
                print("Pilihan metode pembayaran tidak valid.")
        else:
            print("Semua pembelian sudah dibayar.")
    else:
        print("Belum ada riwayat pembelian.")

def cari_riwayat_pembelian():
    tanggal = input("Masukkan tanggal pembelian (YYYY-MM-DD): ")
    hasil_pencarian = [pembelian for pembelian in riwayat_pembelian if pembelian.get("Tanggal") == tanggal]

    if hasil_pencarian:
        print(f"\nRiwayat Pembelian pada tanggal {tanggal}:")
        for pembelian in hasil_pencarian:
            print(f"Makanan: {pembelian['Makanan']}, Jumlah: {pembelian['Jumlah']} porsi, Total Harga: Rp {pembelian['Total Harga']}")
    else:
        print(f"Tidak ditemukan pembelian pada tanggal {tanggal}.")

def tampilkan_statistik():
    paid_purchases = [pembelian for pembelian in riwayat_pembelian if pembelian.get("Status Pembayaran") == "Sudah Dibayar"]

    if paid_purchases:
        total_pendapatan = sum(pembelian["Total Harga"] for pembelian in paid_purchases)
        total_transaksi = len(paid_purchases)
        rata_rata_transaksi = total_pendapatan / total_transaksi

        print(f"\nStatistik Pembelian (Sudah Dibayar):")
        print(f"Total Transaksi: {total_transaksi}")
        print(f"Total Pendapatan: Rp {total_pendapatan}")
        print(f"Rata-rata Transaksi: Rp {rata_rata_transaksi}")
    else:
        print("Belum ada pembelian yang dibayar.")

while True:
    tampilkan_menu()
    pilihan_menu = int(input("Silakan pilih menu: "))

    if pilihan_menu == 1:
        beli_makanan()
    elif pilihan_menu == 2:
        tampilkan_riwayat_pembelian()
    elif pilihan_menu == 3:
        update_pembelian()
    elif pilihan_menu == 4:
        hapus_pembelian()
    elif pilihan_menu == 5:
        bayar()
    elif pilihan_menu == 6:
        tampilkan_menu_makanan()
    elif pilihan_menu == 7:
        cari_riwayat_pembelian()
    elif pilihan_menu == 8:
        tampilkan_statistik()
    elif pilihan_menu == 9:
        print("Terima kasih telah menggunakan layanan kami.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
