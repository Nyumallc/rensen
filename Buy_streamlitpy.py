import streamlit as st
import requests
import pandas as pd

if "dblist" not in st.session_state: 
    st.session_state.dblist = []
# if "pic_list" not in st.session_state: 
#     st.session_state.pic_list = []
# if "pic_list" not in st.session_state: 
#     st.session_state.pic_name = []


params = st.experimental_get_query_params()
# p_id = params['p_id'][0]
p_title = params['p_title'][0]
p_title  =p_title.replace('.jpg','')
userid = params['userid'][0]
displayname = params['displayname'][0]
# p_url = 'http://drive.google.com/uc?export=view&id=' + p_id

REQUEST_URL = 'https://script.google.com/macros/s/AKfycbxPjQ80xb6yU0k1NQilCD37UWljBt1QkaQzpZoD56maH8hYHd8pzj8B6JWBqZ1_o_cH/exec'

df=pd.read_csv('pic_url_pd.csv')
dfitem = pd.read_csv('item_list.csv')
# df = df[df['name'].str.contains('keyword')]
st.session_state.dblist=pd.DataFrame(data=dfitem.loc[:,["ID","title","price","state","remarke","last",]])
# st.session_state.pic_list=pd.DataFrame(data=df.loc[:,["src","title"]])

# pic_list=st.session_state.pic_list
# pic_index_num = pic_list.index[pic_list["title"] == int(p_title)]
# p_id = pic_list.iloc[pic_index_num]["src"]
try:
    p_title=str(int(p_title))
except ValueError as e: 
    p_title=str(p_title)
p_url ='商品写真表示用/' + p_title + ".jpg"

item_type=st.session_state.dblist
index_num = item_type.index[item_type["ID"] == p_title]
title = item_type.iloc[index_num]["title"]
price = item_type.iloc[index_num]["price"]
state = item_type.iloc[index_num]["state"]
remarke = item_type.iloc[index_num]["remarke"]
last = item_type.iloc[index_num]["last"]

st.image(p_url)
st.title(title.iloc[-1])
left_column, right_column = st.columns(2)
left_column.title(price.iloc[-1])
right_column.title(state.iloc[-1])
left_column.write(remarke.iloc[-1])
right_column.write(last.iloc[-1])

st.title('要購買此項商品嗎？')
option = st.text_input('備註:(例如：需要加強氣泡紙包裝）')
buy_but = st.button("購入依頼")
if buy_but:
    api_url = REQUEST_URL +'?&userid=' + userid +'&displayname=' + displayname + '&title=' + title + '&p_title=' + p_title + '&price=' + price + '&option=' + option
    response = requests.get(api_url)
    st.title('已收到您的訂單')
