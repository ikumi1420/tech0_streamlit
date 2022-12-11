import streamlit as st
import numpy as np
import pandas as pd

st.title('SAPIX実績')
st.write('Tech0「爆速班」sample')

df_2020 = pd.read_csv('sapixdata_2020.csv',encoding = 'shift_jis')
df_2019 = pd.read_csv('sapixdata_2019.csv')

df_2020['年度']=2020
df_2019['年度']=2019

df_concat = pd.concat([df_2019,df_2020])

df_concat = pd.DataFrame(df_concat)

st.write(df_concat)
st.dataframe(df_concat.style,width=500,height=100)


text = st.text_input('あなたの目標校を教えてください。')

condition = st.slider('あなたの直近の偏差値は？', 0, 50, 100)

text_column, right_column = st.columns(2)

'あなたの目標校：', text
'あなたの偏差値：', condition

