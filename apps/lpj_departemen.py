import streamlit as st

link = '[Link LPJ PPT Per Departemen](https://drive.google.com/drive/folders/1yV7lYNl2zCnygAnTdTCPJpdP0QNUT1jS?usp=sharing)'
link2 = '[Link LPJ PDF Per Departemen](https://drive.google.com/drive/folders/1yV6EcjZ0MUfPtfBGwY6lSM4uJHdT0KC_?usp=sharing)'
st.header("Anda Bisa Mengakses Dengan Mengklik Dibawah Ini :")
st.write("PPT :")
st.markdown(link, unsafe_allow_html=True)
st.write("PDF :")
st.markdown(link2, unsafe_allow_html=True)