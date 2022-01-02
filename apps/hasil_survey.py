import pandas as pd
import numpy as np
import plotly as plot
import streamlit as st
import plotly.express as px

data = pd.read_csv(r'apps\Survey Kepuasan Himasika ITS.csv')
data_bersih = data.drop(columns=['S.NO','Submitted Time','17. Apa sih feedback mu terhadap Himasika, dan apa yang dapat dikembangkan dari Himasika Untuk Kedepannya'])
a = data_bersih['1. Angkatan (Silahkan isi dengan tahun angkatan, contoh : 2018'].value_counts().index
b = data_bersih['1. Angkatan (Silahkan isi dengan tahun angkatan, contoh : 2018'].value_counts().values
fig = px.pie(data_bersih,names=a,values=b)
c = data_bersih['2. Jenis Kelamin'].value_counts().index
d = data_bersih['2. Jenis Kelamin'].value_counts().values
fig2 = px.pie(data_bersih,names=c,values=d)
e = data_bersih['3. Keaktifan Himpunan Di Sosial Media'].value_counts().index
f = data_bersih['3. Keaktifan Himpunan Di Sosial Media'].value_counts().values
fig3 = px.pie(data_bersih,names=e,values=f)
g = data_bersih['4. Pelayanan Himpunan Pada Bidang Keprofesian'].value_counts().index
h = data_bersih['4. Pelayanan Himpunan Pada Bidang Keprofesian'].value_counts().values
fig4 = px.pie(data_bersih,names=g,values=h)
i = data_bersih['5. Pelayanan Himpunan Pada Bidang Minat Bakat'].value_counts().index
j = data_bersih['5. Pelayanan Himpunan Pada Bidang Minat Bakat'].value_counts().values
fig5 = px.pie(data_bersih,names=i,values=j)
k = data_bersih['6. Pelayanan Himpunan Pada 4 Bidang Manajerial'].value_counts().index
l = data_bersih['6. Pelayanan Himpunan Pada 4 Bidang Manajerial'].value_counts().values
fig6 = px.pie(data_bersih,names=k,values=l)
m = data_bersih['7. Pelayanan Himpunan Pada 4 Bidang Kewirausahaan'].value_counts().index
n = data_bersih['7. Pelayanan Himpunan Pada 4 Bidang Kewirausahaan'].value_counts().values
fig7 = px.pie(data_bersih,names=m,values=n)
o = data_bersih['8. Respons Himpunan Terhadap Aspirasi Anggota'].value_counts().index
p = data_bersih['8. Respons Himpunan Terhadap Aspirasi Anggota'].value_counts().values
fig8 = px.pie(data_bersih,names=o,values=p)
q = data_bersih['9. Pelayanan himpunan pada bidang Keilmiahan'].value_counts().index
r = data_bersih['9. Pelayanan himpunan pada bidang Keilmiahan'].value_counts().values
fig9 = px.pie(data_bersih,names=q,values=r)
s = data_bersih[ '10. Pelayanan himpunan pada bidang Kesejahteraan Mahasiswa'].value_counts().index
t = data_bersih[ '10. Pelayanan himpunan pada bidang Kesejahteraan Mahasiswa'].value_counts().values
fig10 = px.pie(data_bersih,names=s,values=t)
u = data_bersih['11. Pelayanan himpunan pada bidang Sosial Masyarakat'].value_counts().index
v = data_bersih['11. Pelayanan himpunan pada bidang Sosial Masyarakat'].value_counts().values
fig11 = px.pie(data_bersih,names=u,values=v)
w = data_bersih[ '12. Pelayanan himpunan pada bidang Pengembangan Sumber Daya Mahasiswa'].value_counts().index
x = data_bersih[ '12. Pelayanan himpunan pada bidang Pengembangan Sumber Daya Mahasiswa'].value_counts().values
fig12 = px.pie(data_bersih,names=w,values=x)
y = data_bersih['13. Pelayanan himpunan pada bidang Internal Anggota'].value_counts().index
z = data_bersih['13. Pelayanan himpunan pada bidang Internal Anggota'].value_counts().values
fig13 = px.pie(data_bersih,names=y,values=z)
aa = data_bersih['14. Pelayanan himpunan pada bidang Eksternalisasi'].value_counts().index
ab = data_bersih['14. Pelayanan himpunan pada bidang Eksternalisasi'].value_counts().values
fig14 = px.pie(data_bersih,names=aa,values=ab)
ac = data_bersih['15. Pelayanan himpunan pada bidang Internasionalisasi'].value_counts().index
ad = data_bersih['15. Pelayanan himpunan pada bidang Internasionalisasi'].value_counts().values
fig15 = px.pie(data_bersih,names=ac,values=ad)
ae = data_bersih['16. Kepuasan Terhadap Keseluruhan Pelayanan Himpunan'].value_counts().index
af = data_bersih['16. Kepuasan Terhadap Keseluruhan Pelayanan Himpunan'].value_counts().values
fig16 = px.pie(data_bersih,names=ae,values=af)

st.write('1. Angkatan')
st.write(fig)
st.write('2. Jenis Kelamin')
st.write(fig2)
st.write('3. Keaktifan Himpunan Di Sosial Media')
st.write(fig3)
st.write('4. Pelayanan Himpunan Pada Bidang Keprofesian')
st.write(fig4)
st.write('5. Pelayanan Himpunan Pada Bidang Minat Bakat')
st.write(fig5)
st.write('6. Pelayanan Himpunan Pada 4 Bidang Manajerial')
st.write(fig6)
st.write('7. Pelayanan Himpunan Pada 4 Bidang Kewirausahaan')
st.write(fig7)
st.write('8. Respons Himpunan Terhadap Aspirasi Anggota')
st.write(fig8)
st.write('9. Pelayanan himpunan pada bidang Keilmiahan')
st.write(fig9)
st.write('10. Pelayanan himpunan pada bidang Kesejahteraan Mahasiswa')
st.write(fig10)
st.write('11. Pelayanan himpunan pada bidang Sosial Masyarakat')
st.write(fig11)
st.write('12. Pelayanan himpunan pada bidang Pengembangan Sumber Daya Mahasiswa')
st.write(fig12)
st.write('13. Pelayanan himpunan pada bidang Internal Anggota')
st.write(fig13)
st.write('14. Pelayanan himpunan pada bidang Eksternalisasi')
st.write(fig14)
st.write('15. Pelayanan himpunan pada bidang Internasionalisasi')
st.write(fig15)
st.write('16. Kepuasan Terhadap Keseluruhan Pelayanan Himpunan')
st.write(fig16)



