import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import psycopg2
import streamlit.components.v1 as components


#PostgreSQLデータベースへの接続
conn = psycopg2.connect(
    database = 'アンケートアプリ',
    user = 'shunsuke',
    password = 'Is1484317',
    host = 'localhost',
    port = '5432'
)

#テーブルを作成（初回のみ）
# cursor = conn.cursor()
# cursor.execute('''
#         CREATE TABLE IF NOT EXISTS ramen_survey(
#               id SERIAL PRIMARY KEY,
#                age INT,
#                sex INT,
#                point INT,
#                depth VARCHAR(255),
#                thickness VARCHAR(255),
#                improvement VARCHAR(255),
#                good VARCHAR(255),
#                hope VARCHAR(255)
#         )
#  ''')
# conn.commit()



#アンケート質問
st.title("ラーメンアンケート")
st.write('2025年のオープンを目指して、ラーメンを作っています。\n 食べていただいた方からのご意見を大切にし、お客様と作るラーメン屋にしたいと考えています。\nアンケートのご協力をお願いしたします。')

#ユーザーからの入力を受け取る
age = st.number_input('①年齢を入力してください。', min_value=0, max_value=120, step=1, value=20)
st.write("&nbsp;")  # スペースを挿入
sex = st.selectbox('②性別を選択してください。', [' ','男性','女性','その他'])

point = st.slider('③ラーメンに点数をつけてください',0,100,50,1)

depth = st.selectbox('④味の濃さはいかがでしょうか。', [' ','ちょうどいい','濃い方がよかった','薄い方がよかった','その他'])
thickness = st.selectbox('⑤麺の太さはいかがでしょうか。',['','ちょうどいい','細い方がよかった','太い方がよかった','その他'])
st.write("&nbsp;")  # スペースを挿入

improvement = st.text_input('⑥改善点があればお書きください。')
st.write("&nbsp;")  # スペースを挿入
good = st.text_input('⑦よかったところがあればお書きください。')
hope = st.text_input('⑧今後のラーメンの種類やトッピングで希望があればお書きください。')

# # 4つの写真を表示するコンテナ
# photos_container = st.empty()

# # 4つの写真を表示するためのHTMLとCSS
# photos_html = """
#     <div style="display: flex; justify-content: space-between;">
#         <img src="/Users/shunsuke/Desktop/峰吉ラーメンアンケートアプリ/①.jpg" style="width: 200px; height: 200px;">
#         <img src="/Users/shunsuke/Desktop/峰吉ラーメンアンケートアプリ/②.jpg" style="width: 200px; height: 200px;">
#     </div>
#     """

# # HTMLコンポーネントを使用して写真を表示
# photos_container.components.v1.html(photos_html, height=250)

st.write("&nbsp;")  # スペースを挿入
st.write('趣味で、お弁当を作っています。らーめん出店など情報はしばらく、このアカウントで発信していきたいと考えています。よければ、フォローをお願いします。')

st.write("https://www.instagram.com/kinniku_bento/") 
st.write("&nbsp;")  # スペースを挿入
st.write("アンケートのご協力ありがとうございました！") 

#データベースにデータを蓄積
if st.button('回答を送信'):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ramen_survey(age,sex,point,depth,thickness,improvement,good,hope) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (age,sex,point,depth,thickness,improvement,good,hope))
    conn.commit()
    cursor.close()

#データベースを閉じる
conn.close()