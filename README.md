# UAS Information Retrieval

## Rancang Bangun Sistem Information Retrieval Berbasis Web Menggunakan Scrapy dan Streamlit untuk Pencarian Data Buku

### Identitas Mahasiswa

- **Nama** : Ananda Khairatunnisa
- **NIM** : 24146038
- **Mata Kuliah** : Information Retrieval (SIF502)
- **Dosen Pengampu** : Teuku Rizky Noviandy, S.Kom., M.Kom.

---

## Deskripsi Proyek

Proyek ini merupakan implementasi sistem **Information Retrieval (Temu Balik Informasi)** berbasis web menggunakan **Scrapy** sebagai web crawler dan **Streamlit** sebagai antarmuka pengguna.

Aplikasi melakukan proses crawling terhadap website **Books to Scrape** untuk mengambil informasi buku, kemudian menyimpannya dalam format JSON. Data tersebut selanjutnya ditampilkan pada aplikasi Streamlit yang menyediakan fitur pencarian berdasarkan judul buku.

---

## Teknologi yang Digunakan

- Python
- Scrapy
- Streamlit
- JSON

---

## Struktur Proyek

```
book_crawler_app/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── books.json
└── scrapy_project/
```

---

## Cara Menjalankan

### Install dependensi

```bash
pip install -r requirements.txt
```

### Jalankan Scrapy

```bash
cd scrapy_project
scrapy crawl books -o ../data/books.json
```

### Jalankan Streamlit

```bash
streamlit run app.py
```

---

## Repository GitHub

https://github.com/anandakhairatunnisa/uas-info-retrieval

---

## Link Aplikasi Streamlit

*(Isi setelah proses deployment berhasil)*

Contoh:

https://uas-info-retrieval.streamlit.app
