# DASHBOARD PERBANDINGAN APBD PROVINSI SE-INDONESIA
# Dashboard Perbandingan APBD Provinsi se-Indonesia

Dashboard interaktif berbasis Streamlit untuk memvisualisasikan dan menganalisis data APBD (Anggaran Pendapatan dan Belanja Daerah) dari berbagai provinsi di Indonesia. Dashboard ini memungkinkan pengguna untuk mengunggah data APBD dalam format CSV, memfilter berdasarkan tahun dan provinsi, serta melihat statistik ringkas, grafik batang, dan tabel data secara dinamis.

## Fitur

- Unggah data APBD dalam format CSV.
- Pembersihan dan pra-pemrosesan data otomatis, termasuk perbaikan typo umum dan konversi format angka lokal.
- Filter data berdasarkan tahun dan provinsi melalui kontrol sidebar.
- Menampilkan total pendapatan dan belanja berdasarkan filter yang dipilih.
- Visualisasi perbandingan pendapatan dan belanja per provinsi menggunakan grafik batang.
- Menampilkan tabel data yang sudah difilter secara interaktif.

## Persyaratan Data

File CSV yang diunggah harus mengandung kolom-kolom berikut:

- Provinsi (nama provinsi)
- Tahun (tahun data)
- Bulan (nama bulan dalam bahasa Indonesia)
- Pendapatan (nilai pendapatan, format angka lokal diperbolehkan)
- Belanja (nilai belanja, format angka lokal diperbolehkan)

Catatan: Program juga menangani typo umum pada nama kolom Pendpatan dengan mengubahnya menjadi Pendapatan.

## Cara Penggunaan

1. Jalankan aplikasi Streamlit.
2. Unggah file CSV APBD menggunakan fitur unggah file.
3. Gunakan filter di sidebar untuk memilih tahun dan provinsi yang ingin dianalisis.
4. Lihat statistik ringkas, grafik batang, dan tabel data yang akan diperbarui secara dinamis sesuai pilihan filter.

## Teknologi yang Digunakan

- [Streamlit](https://streamlit.io/) untuk aplikasi web interaktif.
- [Pandas](https://pandas.pydata.org/) untuk manipulasi data.
- [NumPy](https://numpy.org/) untuk operasi numerik.
- [Matplotlib](https://matplotlib.org/) untuk pembuatan grafik batang.

---
Dashboard ini membantu para pemangku kepentingan dan analis untuk dengan mudah membandingkan dan menganalisis data anggaran daerah di berbagai provinsi Indonesia selama beberapa tahun dan bulan.

## Penjelasan Kode Program

Berikut adalah penjelasan langkah demi langkah dari kode program pada file app.py:

1. *Import Library*  
   Mengimpor library yang dibutuhkan:  
   - streamlit untuk membuat aplikasi web interaktif.  
   - pandas untuk manipulasi data.  
   - numpy untuk operasi numerik.  
   - matplotlib.pyplot untuk membuat grafik.

2. *Konfigurasi Halaman*  
   Mengatur layout halaman menjadi lebar (wide) dan memberi judul halaman.

3. *Judul Aplikasi*  
   Menampilkan judul utama dashboard di halaman.

4. *Upload File CSV*  
   Menyediakan widget untuk mengunggah file CSV yang berisi data APBD.

5. *Membaca Data*  
   Jika file diunggah, membaca data CSV ke dalam DataFrame df.

6. *Perbaikan Typo Kolom*  
   Memeriksa dan memperbaiki typo pada nama kolom Pendpatan menjadi Pendapatan.

7. *Validasi Kolom Wajib*  
   Memastikan data memiliki kolom-kolom wajib: Provinsi, Tahun, Bulan, Pendapatan, dan Belanja. Jika tidak, menampilkan pesan error.

8. *Konversi Format Angka*  
   Mengubah format angka lokal (titik sebagai ribuan dan koma sebagai desimal) menjadi tipe data float agar dapat diolah.

9. *Mapping Nama Bulan ke Angka*  
   Mengganti nama bulan dalam bahasa Indonesia menjadi angka 1-12 untuk memudahkan analisis.

10. *Filter Sidebar*  
    Membuat filter di sidebar untuk memilih tahun dan provinsi yang ingin dianalisis.

11. *Filter Data*  
    Memfilter DataFrame berdasarkan pilihan tahun dan provinsi dari sidebar.

12. *Statistik Ringkas*  
    Menampilkan total pendapatan dan belanja berdasarkan data yang sudah difilter.

13. *Grafik Batang*  
    Membuat grafik batang perbandingan total pendapatan dan belanja per provinsi menggunakan Matplotlib.

14. *Tabel Data*  
    Menampilkan tabel data yang sudah difilter secara interaktif.

## Sumber Data

Data APBD yang digunakan dalam dashboard ini dapat diperoleh dari situs resmi Direktorat Jenderal Perimbangan Keuangan Kementerian Keuangan Republik Indonesia:  
[https://djpk.kemenkeu.go.id/portal/data/apbd](https://djpk.kemenkeu.go.id/portal/data/apbd)
