# Tugas 1 II4031 2024: Aplikasi Ragam *Cipher* Klasik 🔥🌾

Aplikasi implementasi beberapa *cipher* klasik dengan Web GUI.

#### Daftar cipher yang diimplementasikan
- *Vigenere cipher*
- *Extended vigenere cipher*
- *Playfair cipher*
- *Product cipher*: Kombinasi vigenere *cipher• dan *cipher* transposisi berbasis kolom
- *Affine cipher*
- *Autokey vigenere cipher*

#### Spesifikasi lainnya
- Program dapat menerima pesan berupa berkas sembarang (teks maupun biner) atau pesan yang diketikkan dari papan-ketik
- Program dapat mengenkripsi plainteks. Pada seluruh *cipher* selain *extended vigenere cipher*, program hanya mengenkripsi karakter alfabet saja. Angka, spasi, dan tanda baca lainnya diabaikan dan dibuang saat cipherteks ditampilkan atau disimpan
- Program dapat mendekripsi cipherteks menjadi plainteks semula
- Untuk pesan teks dari papan-ketik, program dapat menampilkan plainteks dan cipherteks di
layar. Cipherteks sebaiknya ditampilkan dalam kode Base64
- Program dapat menyimpan cipherteks ke dalam file
- Kunci dimasukkan oleh pengguna. Panjang kunci bebas
- Untuk enkripsi plainteks sembarang file (khusus untuk *extended vigenere cipher* saja), setiap file diperlakukan sebagai file of bytes. Program membaca setiap byte di dalam file (termasuk byte-byte header file) dan mengenkripsinya. Hanya saja file yang sudah terenkripsi tidak bisa dibuka oleh program aplikasinya karena header file ikut terenkripsi. Namun dengan mendekripsinya kembali maka file tersebut dapat dibuka oleh aplikasinya

## Langkah instalasi
- Pasang Python versi 3.10 ke atas
- Pasang modul `Flask` menggunakan perintah `pip install flask`
- Unduh atau lakukan kloning pada repo ini
- Buka folder repo ini dan jalankan perintah berikut:
```bash
python3 app.py
```

## Langkah penggunaan program
- Buka `http://127.0.0.1:5000` di peramban web
- Pilih *cipher* yang hendak digunakan
- Ketikkan teks atau unggah berkas yang hendak dienkripsi atau didekripsi
- Masukkan kunci *cipher* yang sesuai
- Tekan tombol untuk mengenkripsi/dekripsi teks/berkas
- Hasil enkripsi/dekripsi akan ditampilkan pada layar dan dapat disalin atau diunduh

## Anggota kelompok
- Aufar Ramadhan 18221163
- Naura Valda Prameswari 18221173
