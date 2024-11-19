# Program untuk menambahkan data ke dalam list dan menghitung nilai akhir

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa:")
    
    # Input nama mahasiswa
    nama = input("Nama: ")
    
    # Input nilai tugas, UTS, dan UAS
    try:
        nilai_tugas = float(input("Nilai Tugas (0-100): "))
        nilai_uts = float(input("Nilai UTS (0-100): "))
        nilai_uas = float(input("Nilai UAS (0-100): "))
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        continue

    # Validasi input nilai (0-100)
    if not (0 <= nilai_tugas <= 100 and 0 <= nilai_uts <= 100 and 0 <= nilai_uas <= 100):
        print("Nilai harus berada dalam rentang 0-100. Silakan coba lagi.")
        continue

    # Hitung nilai akhir
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)

    # Tambahkan data mahasiswa ke dalam list
    data_mahasiswa.append({
        "nama": nama,
        "nilai_tugas": nilai_tugas,
        "nilai_uts": nilai_uts,
        "nilai_uas": nilai_uas,
        "nilai_akhir": nilai_akhir
    })

    # Tanyakan apakah ingin menambahkan data lagi
    lanjut = input("Apakah ingin menambahkan data lagi? (y/t): ").lower()
    if lanjut == 't':
        break

# Tampilkan daftar data mahasiswa
print("\nDaftar Data Mahasiswa:")
print("=" * 50)
print(f"{'No.':<4} {'Nama':<15} {'Tugas':<7} {'UTS':<7} {'UAS':<7} {'Akhir':<7}")
print("=" * 50)

for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"{i:<4} {mahasiswa['nama']:<15} {mahasiswa['nilai_tugas']:<7.2f} "
          f"{mahasiswa['nilai_uts']:<7.2f} {mahasiswa['nilai_uas']:<7.2f} {mahasiswa['nilai_akhir']:<7.2f}")

print("=" * 50)
