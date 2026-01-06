import streamlit as st

st.title("_naNote_ is :blue[cool] :sunglasses:")
st.header("Catatan Praktik dan Kalkulasi Hasil PSA")


#Information tentang apk
expander = st.expander("🐡Apa itu naNote?")
expander.write('''
    naNote merupakan aplikasi berbasis web yang dirancang oleh mahasiswa/i Politeknik AKA Bogor
    untuk membantu praktikkan mengkalkulasi
    hasil data PSA yang di dapat.
''')
expander.image("https://www.microtrac.com/images/5545e7b51b645ef7b0b93088a878cd6c/1200x/max/alpha/pic-wave-ii.jpg")
expander.write('''
    dan juga membantu praktikkan mencatat data - data saat praktik berlangsung!
''')
expander.image("https://stuyspec-media.s3.us-east-2.amazonaws.com/rewrite_media/81ebc150-d809-11ed-952b-f5fad1466d2c.jpg")

#option
if st.button("Catatan", width="stretch", type="primary"):
    st.switch_page("pages/catatan_1.py", query_params={"page": "catatan"})
if st.button("Kalkulasi", width="stretch", type="primary"):
    st.switch_page("pages/kalkulasi_2.py", query_params={"page": "kalkulasi"})
