import streamlit as st
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "books.json")

st.set_page_config(page_title="Book Search (Scraped via Scrapy)", layout="wide")
st.title("📚 Book Search (Scraped via Scrapy)")

# Load data
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    st.error(f"Data tidak ditemukan: {DATA_PATH}")
    st.stop()
# Input pencarian
query = st.text_input("Cari...", "")

# Filter data
if query:
    filtered = [item for item in data if query.lower() in item.get("title", "").lower()]
else:
    filtered = data

st.markdown(f"### ✨ Ditemukan {len(filtered)} hasil")

for item in filtered:
    st.markdown(f"[{item.get('title')}]({item.get('link')})")
    st.markdown(f"Price: {item.get('price')} | Rating: {item.get('rating')} | Availability: {item.get('availability')}")
    st.markdown("---")
