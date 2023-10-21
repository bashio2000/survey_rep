import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import psycopg2



#PostgreSQLデータベースへの接続
conn = psycopg2.connect(
    database = 'アンケートアプリ',
    user = 'shunsuke',
    password = 'Is1484317',
    host = 'localhost',
    port = '5432'
)


st.title('アンケート結果')


#更新ボタンを押して、集計結果を表示
if st.button('更新'):
    
    # SQLクエリの実行
    query = "SELECT * FROM ramen_survey"
    df = pd.read_sql_query(query, conn)
    
    # 年齢ごとに人数を集計
    st.title('年齢ごとの人数の集計')
    age_counts = df['age'].value_counts().reset_index()
    age_counts.columns = ['年齢', '人数']
    # 棒グラフを表示
    st.bar_chart(age_counts.set_index('年齢'))
    st.write("&nbsp;")  # スペースを挿入

    st.title('味の濃さの結果の集計')
    # 味の結果を集計
    depth_counts = df['depth'].value_counts().reset_index()
    depth_counts.columns = ['味の濃さ', '人数']
    # 棒グラフを表示
    st.bar_chart(depth_counts.set_index('味の濃さ'))
    st.write("&nbsp;")  # スペースを挿入

    st.title('麺の太さの結果の集計')
    # 味の結果を集計
    thickness_counts = df['thickness'].value_counts().reset_index()
    thickness_counts.columns = ['麺の太さ', '人数']
    # 棒グラフを表示
    st.bar_chart(thickness_counts.set_index('麺の太さ'))
    st.write("&nbsp;")  # スペースを挿入

#データベースを閉じる
conn.close()