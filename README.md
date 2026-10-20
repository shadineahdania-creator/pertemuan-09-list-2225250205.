# Pertemuan 09 – List dan Pengolahan Data Numerik

**Nama:** Shadine Ahdania Sofyan
**NIM:** 2225250205 
**Kelas:** 3B

## Tujuan
Mengolah kumpulan data numerik menggunakan list Python, menghitung rata-rata, menentukan nilai minimum dan maksimum, serta menghitung jumlah mahasiswa yang lulus.

## Struktur Program
1. `latihan/` berisi file latihan untuk memahami penggunaan list, indeks, dan pengolahan data numerik.
2. `praktik/analisis_nilai_mahasiswa.py` berisi program untuk menghitung rata-rata nilai, menentukan nilai minimum dan maksimum, serta menghitung jumlah nilai yang lulus.

## Cara Menjalankan
Jalankan perintah berikut melalui terminal dari folder utama proyek:

```bash
python3 praktik/analisis_nilai_mahasiswa.py
```

## Test Case

| Data | Yang diperiksa | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|---|
| `[60, 70, 80]` | Rata-rata | 70.00 | 70.00 | Lulus |
| `[60, 70, 80]` | Minimum/maksimum | 60 / 80 | 60 / 80 | Lulus |
| `[60, 70, 80]` | Jumlah lulus | 3 | 3 | Lulus |
| `[59, 60, 61]` | Batas kelulusan 60 | 2 lulus | 2 lulus | Lulus |
| `[]` | List kosong pada fungsi rata-rata | Tidak error | Mengembalikan `None` | Lulus |

## Refleksi
Saya memahami bahwa indeks list Python dimulai dari 0 dan list dapat digunakan untuk menyimpan serta mengolah banyak nilai. Saya juga memahami cara menggunakan perulangan dan fungsi untuk menghitung rata-rata dan jumlah nilai yang lulus.

Kesalahan yang berhasil diperbaiki adalah pembagian dengan nol ketika list kosong. Saya mengatasinya dengan memeriksa apakah list kosong sebelum menghitung rata-rata.