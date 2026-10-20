def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    return [x for x in data if x >= batas]

nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Gunakan fungsi dan tampilkan ringkasan
print("=== Ringkasan Data ===")
print(f"Rata-rata: {rata_rata(nilai):.2f}")
print(f"Jumlah lulus: {len(nilai_lulus(nilai))}")

# Test Case Wajib
print("\n=== Test Case Wajib ===")
print(f"[60, 70, 80] Rata-rata: {rata_rata([60, 70, 80]):.2f}")
print(f"[60, 70, 80] Minimum / maksimum: {min([60, 70, 80])} / {max([60, 70, 80])}")
print(f"[60, 70, 80] Jumlah lulus: {len(nilai_lulus([60, 70, 80]))}")
print(f"[59, 60, 61] Batas kelulusan: {len(nilai_lulus([59, 60, 61]))} lulus")
print(f"[] Penanganan list kosong: {rata_rata([])} (Tidak error)")