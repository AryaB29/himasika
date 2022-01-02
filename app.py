import streamlit as st 
import pandas as pd
import numpy as np
import plotly as plot
import plotly.express as px
import time

st.title("LPJ Himasika ITS Kabinet Parayuga")
st.header("Selamat Datang Di LPJ Himasika ITS")
st.write("Silahkan Pilih Menu Yang Anda Inginkan Pada Sidebar Disamping")
input = st.sidebar.selectbox(
    'Silahkan Pilih Menu Yang Ingin Anda Pilih',
    ('Hasil Survey','LPJ Departemen')
)
st.write('Menu Yang Anda Pilih :', input)
if input == 'Hasil Survey':
    with st.spinner('Silahkan Tunggu Sistem Sedang Memproses'):
        time.sleep(5)
    from apps import hasil_survey
if input == 'LPJ Departemen':
    with st.spinner('Silahkan Tunggu Sistem Sedang Memproses'):
        time.sleep(5)
    from apps import lpj_departemen
