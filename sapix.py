import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

import random

def answer():
    try:
        new_name = random.choice(st.session_state["name"])
    except Exception as e:
        new_name = str(e)
    finally:
        st.session_state["new_name"] = new_name

if not any(st.session_state):
    st.session_state["name"] = ""
    st.session_state["new_name"] = False
   
name = st.sidebar.text_input("合格したい？なら、ここに名前を書きな。",
    key="name", on_change=answer)

new_name = st.session_state["new_name"]



text = st.sidebar.text_input('nｓame''の目標校は？')

condition = st.sidebar.slider('{name}の直近の偏差値は？', 0, 50, 100)


img = Image.open('jyuken_top.jpg')
st.image(img, caption='jyuken_top', use_column_width=True)

text_column, right_column = st.columns(2)

if new_name:
    st.write(f"### フン。{name}というのかい。贅沢な名だねぇ。")
    st.write(f"今日からお前の名前は{new_name}だ。")
    st.write(f"いいかい、{new_name}だよ。")
    st.write(f"### わかったら現実を見るんだ、{new_name}!!")

    img = Image.open('yubaba.jpg')
    st.image(img, caption='画像はスタジオジブリの場面写真の無償提供からお借りしています', use_column_width=True)


st.write("---")

'{new_name}の目標校：', text
'{new_name}の偏差値：', condition

st.title('SAPIX実績')

df_2020 = pd.read_csv('sapixdata_2020.csv',encoding = 'shift_jis')
df_2019 = pd.read_csv('sapixdata_2019.csv')

df_2020['年度']=2020
df_2019['年度']=2019

df_concat = pd.concat([df_2019,df_2020])

df_concat = pd.DataFrame(df_concat)

st.write(df_concat)
st.dataframe(df_concat,width=500,height=100)


if st.button('運試し、押してみる？'):
    img = Image.open('waraukadoniha.jpg')
    st.write('Good Luck!')
    st.image(img, caption='笑う門には福来る', use_column_width=True)

st.write("<div style='text-align: right;'>制作・著作　爆速班</div>",
         unsafe_allow_html=True) 