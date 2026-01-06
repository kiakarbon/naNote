import streamlit as st
import sqlite3
from datetime import datetime

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Notes App",
    layout="centered"
)

# =========================
# DATABASE
# =========================
conn = sqlite3.connect("notes.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT
)
""")
conn.commit()

# =========================
# FUNGSI DATABASE
# =========================
def add_note(title, content):
    c.execute(
        "INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)",
        (title, content, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()

def get_notes():
    c.execute("SELECT * FROM notes ORDER BY id DESC")
    return c.fetchall()

def delete_note(note_id):
    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()

# =========================
# UI APLIKASI
# =========================
st.title("📒 Aplikasi Catatan")

with st.form("note_form"):
    title = st.text_input("Judul Catatan")
    content = st.text_area("Isi Catatan", height=2000)
    submitted = st.form_submit_button("Simpan Catatan")

    if submitted:
        if title and content:
            add_note(title, content)
            st.success("Catatan berhasil disimpan.")
        else:
            st.error("Judul dan isi tidak boleh kosong.")

st.divider()
st.subheader("Daftar Catatan")

notes = get_notes()

if notes:
    for note in notes:
        note_id, title, content, created_at = note

        with st.expander(f"{title}  |  {created_at}"):
            st.write(content)
            if st.button("Hapus", key=f"delete_{note_id}"):
                delete_note(note_id)
                st.warning("Catatan dihapus. Refresh halaman.")
else:
    st.info("Belum ada catatan.")
