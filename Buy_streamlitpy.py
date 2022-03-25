import streamlit as st
import requests
import pandas as pd

params = st.experimental_get_query_params()
p_id = params['p_id'][0]
p_title = params['p_title'][0]
p_title  =p_title.replace('.jpg','')
userid = params['userid'][0]
displayname = params['displayname'][0]
p_url = 'http://drive.google.com/uc?export=view&id=' + p_id




REQUEST_URL = 'https://script.google.com/macros/s/AKfycbzPDS6SjcPf_Ud5a8FVeun7V2drrkrbV41YX-02KLr7vQKgV9eqZftrSHk1_Uh9sTQ/exec'

dfitem = pd.read_csv('商品リスト.csv')
# df = df[df['name'].str.contains('keyword')]
st.session_state.dblist=pd.DataFrame(data=dfitem.loc[:,["ID","title","price","state","remarke","last",]])


item_type=st.session_state.dblist
index_num = item_type.index[item_type["ID"] == int(p_title)]
title = item_type.iloc[index_num]["title"]
price = item_type.iloc[index_num]["price"]
state = item_type.iloc[index_num]["state"]
remarke = item_type.iloc[index_num]["remarke"]
last = item_type.iloc[index_num]["last"]


st.image(p_url)
st.sidebar.title(title.iloc[-1])
st.sidebar.write(price.iloc[-1])
st.sidebar.write(state.iloc[-1])
st.sidebar.write(remarke.iloc[-1])
st.sidebar.write(last.iloc[-1])

st.sidebar.title('この商品を購入しますか？')
option = st.sidebar.text_input('備考を入力してください。※例：加泡泡紙')
buy_but = st.sidebar.button("購入依頼")
if buy_but:
    api_url = REQUEST_URL +'?&userid=' + userid +'&displayname=' + displayname + '&p_id='+ p_id + '&p_title=' + p_title + '&option=' + option
    response = requests.get(api_url)
