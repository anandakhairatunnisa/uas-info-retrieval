# Book Search App

Nama: [Nama Mahasiswa]
NIM: [NIM Mahasiswa]
Link Streamlit: [Link Streamlit]

## Cara Menjalankan

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan spider (opsional, jika ingin mengupdate data):
   ```bash
   cd scrapy_project
   scrapy crawl books -o ../data/books.json
   ```
3. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run app.py
   ```
