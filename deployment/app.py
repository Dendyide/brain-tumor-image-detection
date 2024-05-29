import streamlit as st
import eda
import prediction as prediction

page = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'Prediction'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()