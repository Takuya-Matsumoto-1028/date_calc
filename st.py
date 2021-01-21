import streamlit as st
import numpy as np
import datetime
import pandas as pd

# sidebarにおけるパラメータ設定

df = pd.DataFrame({
  'No': ['03-01010', '03-02010', '03-03010', '03-04010', '03-05010', '03-06010', '03-07010', '03-08010', '03-09010', '03-51010', '03-25010', '03-53010', '-', '-', '-', '-', '-'],
  '商品名': ['オリーブオイル・サーディン', 'サンフラワーオイル・サーディン', 'マリネサーディン・白ワインと香草風味', 'オイルサーディン・グリーンペッパー風味', 'オイルサーディン・ピメント風味', 'オイルサーディン・シトロン風味', 'オイルサーディン・オリーブの実', 'バターサーディン', 'トマト＆バジルサーディン', 'ビスクドオマール', 'スープポワソン', 'スープポワソン プロヴァンス', 'サバ 白ワイン', 'サバ マスタード', 'サバ トマト', 'サバ ハリッサ', 'シトロン'],
  '賞味日数': [2192, 2192, 1096, 2192, 2192, 2192, 2192, 1462, 1462, 1096, 1096, 1096, 1096, 1096, 1096, 1096, 1462],
})

item_list = df['商品名'].unique()

selected_item = st.sidebar.selectbox(
    '商品を選択：',
    item_list
)

df_filter = df [df['商品名']== selected_item]

today = st.sidebar.date_input('today', datetime.date.today())
st.write(today)

limited_date = st.sidebar.date_input('賞味期限', datetime.date.today())
warranty_period_per = st.sidebar.number_input('保障期限残(%) *数値のみ入力',  min_value=0, max_value=100, step=1, value=30)
warranty_period = (st.sidebar.number_input('保障日数(個別設定)', value=365) + 2)

dt1 = limited_date - today
dt2 = limited_date - datetime.timedelta(days=warranty_period) + datetime.timedelta(days=2)
dt3 = dt2 - today


# メインコンテンツ
st.header('ゆみの計算アプリ')
st.markdown(r'''計算が苦手なゆみのための日付計算アプリです''')
st.markdown(r'''* * *''')
# st.subheader('選択した商品情報')
# st.table(df_filter.set_index('No'))

dt_1 = int(df_filter['賞味日数'])
dt_2 = int((dt_1 * (warranty_period_per)/100) + 2)
dt_3 = limited_date - datetime.timedelta(days=dt_1)
dt_4 = limited_date - datetime.timedelta(days=dt_2)
dt_5 = dt_4 - today

st.header(selected_item)
st.subheader('賞味期限の残%で計算')
st.markdown(rf'''
    <table>
      <tr>
        <th>設定割合(％)</th><th>賞味期限</th><th>賞味日数</th><th>保障日数</th><th>保障期限</th><th>保障残日数</th>
      </tr>
      <tr>
        <td>{warranty_period_per}</td><td>{limited_date}</td><td>{dt_1}</td><td>{dt_2}</td><td>{dt_4}</td><td>{dt_5.days}</td>
      </tr>
    </table>
    <p>※保障日数は到着日までの+2日で計算に含まれています</p>
    ''', unsafe_allow_html=True)

if dt_4 < today:
  st.markdown(r'''
    <center><font size=5 color="#00B06B">保障期限切れのため、出荷できません</font></center>
    ''', unsafe_allow_html=True)
else:
  st.markdown(r'''
    <center><font size=5 color="#00B06B">出荷できます</font></center>
    ''', unsafe_allow_html=True)

st.subheader('賞味期限の残日数で計算')
st.markdown(rf'''
    <table>
      <tr>
        <th>設定日数(日)</th><th>賞味期限</th><th>賞味日数</th><th>保障日数</th><th>保障期限</th><th>保障残日数</th>
      </tr>
      <tr>
        <td>{warranty_period}</td><td>{limited_date}</td><td>{dt_1}</td><td>{warranty_period}</td><td>{dt2}</td><td>{dt3.days}</td>
      </tr>
    </table>
    <p>※保障日数は到着日までの+2日で計算に含まれています</p>
    ''', unsafe_allow_html=True)

if dt2 < today:
  st.markdown(r'''
    <center><font size=5 color="#00B06B">保障期限切れのため、出荷できません</font></center>
    ''', unsafe_allow_html=True)
else:
  st.markdown(r'''
    <center><font size=5 color="#00B06B">出荷できます</font></center>
    ''', unsafe_allow_html=True)