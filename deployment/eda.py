import streamlit as st
from PIL import Image

def run():
    #membuat judul
    st.title('Brain Tumor Detection')

    #tambahkan gambar
    image = Image.open('image.jpg')
    st.image(image, caption = 'Tumor Detection')

    #menambahkan deskripsi
    st.write('Page ini dibuat oleh Dendy Dwinanda')

    #tambahkan gambar
    image2 = Image.open('Cancer.png')
    st.image(image2, caption = 'Terdeteksi Tumor')
    st.write('Sinar X-Ray yang terpancar akan masuk kedalam tubuh, apabila mengenai logam atau organ tubuh sinar akan terblokir. Sinar yang terblokir tersebut akan menghasilkan warna putih.')

    #tambahkan gambar
    image3 = Image.open('Not_Cancer.png')
    st.image(image3, caption = 'Terdeteksi Normal')
    st.write('Otak, pembuluh darah, tengkorak, dan wajah memiliki ukuran, bentuk dan posisi yang normal.')
    st.write('Tidak ada benda asing yang tumbuh atau menetap.')
    st.write('Tidak terjadi perdarahan.')

if __name__ == '__main__':
    run()