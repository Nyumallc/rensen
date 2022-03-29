from pyrsistent import v
import streamlit as st
import requests
import streamlit as st
import pandas as pd
import numpy as np

params = st.experimental_get_query_params()
try:
    keyword = params['keyword'][0]
except KeyError as e:
    Keyword_non=""
try:
    userid = params['userid'][0]
except KeyError as e:
    st.write('ログイン後に完了してから移動してください')
try:
    displayname = params['displayname'][0]
except KeyError as e:
    st.write('ログイン後に完了してから移動してください')

REQUEST_URL = 'https://script.google.com/macros/s/AKfycbzPDS6SjcPf_Ud5a8FVeun7V2drrkrbV41YX-02KLr7vQKgV9eqZftrSHk1_Uh9sTQ/exec'

if "pagecategoly" not in st.session_state:
    st.session_state.pagecategoly = 0
if "pagenumber" not in st.session_state:
    st.session_state.pagenumber = 0
if "itemtitle" not in st.session_state:
    st.session_state.itemtitle = 0
if "itemprice" not in st.session_state:
    st.session_state.itemprice = 0    
if "itemstate" not in st.session_state:
    st.session_state.itemstate = 0
if "itemremarke" not in st.session_state:
    st.session_state.itemremarke = 0
if "itemlast" not in st.session_state:
    st.session_state.itemlast = 0
if "itemserch_word" not in st.session_state:
    st.session_state.itemserch_word= 0    
if "pic_src" not in st.session_state:
    st.session_state.pic_src = 0    
if "dblist" not in st.session_state: 
    st.session_state.dblist = []
if "pic_list" not in st.session_state: 
    st.session_state.pic_list = []
if "pic_list" not in st.session_state: 
    st.session_state.pic_name = []




if st.session_state.pagecategoly == 0:
    left_column, right_column = st.columns(2)
    next_page=right_column.button('次のページ')
    if next_page:
        st.session_state.pagenumber+=1
    back_page=left_column.button('前のページ')
    if back_page:
        st.session_state.pagenumber-=1
    
    page=st.session_state.pagenumber
    df=pd.read_csv('pic_url_pd.csv')
    st.session_state.pic_list=pd.DataFrame(data=df.loc[:,["src",]])
    st.session_state.pic_name=pd.DataFrame(data=df.loc[:,["name","src"]])
    # ------------ここから写真のURLを作る行程------------
    start_num = 0+int(page*10)
    p_url=['']*10
    p_ids=['']*10
    for i in range(10):
        p_ids[i] = st.session_state.pic_list.iloc[start_num+i][0]
        p_url[i] ='http://drive.google.com/uc?export=view&id=' + p_ids[i]

    # ------------ここまで写真のURLを作る行程------------
    # ------------ここからボタンのURLを作る行程------------
    dfitem = pd.read_csv("商品リスト.csv")
    # df = df[df['name'].str.contains('keyword')]
    st.session_state.dblist=pd.DataFrame(data=dfitem.loc[:,["ID","title","price","state","remarke","last",]])
    # st.dataframe(st.session_state.dblist)
    serch_word=['']*10
    item_type=['']*10
    index_num=['']*10
    title=['']*10
    price=['']*10
    state=['']*10
    remarke=['']*10
    text=['']*10 
    last=['']*10
    itempage=['']*10
    for ic in range(10):
        serch_word[ic] = st.session_state.pic_name.iloc[start_num+ic][0]
        # serch_word[ic] =serch_word[ic].replace('.jpg','')
        item_type[ic]=st.session_state.dblist
        index_num[ic] = item_type[ic].index[item_type[ic]['ID'] == serch_word[ic]]
        title[ic] = item_type[ic].iloc[index_num[ic]]["title"]
        price[ic] = item_type[ic].iloc[index_num[ic]]["price"]
        state[ic] = item_type[ic].iloc[index_num[ic]]["state"]
        remarke[ic] = item_type[ic].iloc[index_num[ic]]["remarke"]
        last[ic] = item_type[ic].iloc[index_num[ic]]["last"]
        
        text[ic]=title[ic].iloc[-1] +"   JPY:"+ price[ic].iloc[-1]
    # # -----------ここから1個のラベル作る工程-----------------------
    # serch_word1 = st.session_state.pic_name.iloc[start_num][0]
    # serch_word1 =serch_word1.replace('.jpg','')
    # item_type1=st.session_state.dblist
    # index_num1 = item_type1.index[item_type1['ID'] == serch_word1]
    # name1 = item_type1.iloc[index_num1]["name"]
    # price1 = item_type1.iloc[index_num1]["price"]
    # text1=name1.iloc[-1] +"  "+ price1.iloc[-1]
    # # -----------ここまで1個のラベル作る工程-----------------------
    for colum_i in range(0,10,2):
        left_column.image(p_url[colum_i])
        right_column.image(p_url[colum_i+1])
        itempage[colum_i]=left_column.button(text[colum_i])
        itempage[colum_i+1]=right_column.button(text[colum_i+1])
    if itempage[0]:
        st.session_state.pic_src = p_url[0]
        st.session_state.itemserch_word = serch_word[0]
        st.session_state.itemtitle = title[0]
        st.session_state.itemprice = price[0]
        st.session_state.itemstate = state[0]
        st.session_state.itemremarke = remarke[0]
        st.session_state.itemlast = last[0]
        st.session_state.pagecategoly = 1
    if itempage[1]:
        st.session_state.pic_src = p_url[1]
        st.session_state.itemserch_word = serch_word[1]
        st.session_state.itemtitle = title[1]
        st.session_state.itemprice = price[1]
        st.session_state.itemstate = state[1]
        st.session_state.itemremarke = remarke[1]
        st.session_state.itemlast = last[1]
        st.session_state.pagecategoly = 1
    if itempage[2]:
        st.session_state.pic_src = p_url[2]
        st.session_state.itemserch_word = serch_word[2]
        st.session_state.itemtitle = title[2]
        st.session_state.itemprice = price[2]
        st.session_state.itemstate = state[2]
        st.session_state.itemremarke = remarke[2]
        st.session_state.itemlast = last[2]
        st.session_state.pagecategoly = 1
    if itempage[3]:
        st.session_state.pic_src = p_url[3]
        st.session_state.itemserch_word = serch_word[3]
        st.session_state.itemtitle = title[3]
        st.session_state.itemprice = price[3]
        st.session_state.itemstate = state[3]
        st.session_state.itemremarke = remarke[3]
        st.session_state.itemlast = last[3]
        st.session_state.pagecategoly = 1
    if itempage[4]:
        st.session_state.pic_src = p_url[4]
        st.session_state.itemserch_word = serch_word[4]
        st.session_state.itemtitle = title[4]
        st.session_state.itemprice = price[4]
        st.session_state.itemstate = state[4]
        st.session_state.itemremarke = remarke[4]
        st.session_state.itemlast = last[4]
        st.session_state.pagecategoly = 1
    if itempage[5]:
        st.session_state.pic_src = p_url[5]
        st.session_state.itemserch_word = serch_word[5]
        st.session_state.itemtitle = title[5]
        st.session_state.itemprice = price[5]
        st.session_state.itemstate = state[5]
        st.session_state.itemremarke = remarke[5]
        st.session_state.itemlast = last[5]
        st.session_state.pagecategoly = 1
    if itempage[6]:
        st.session_state.pic_src = p_url[6]
        st.session_state.itemserch_word = serch_word[6]
        st.session_state.itemtitle = title[6]
        st.session_state.itemprice = price[6]
        st.session_state.itemstate = state[6]
        st.session_state.itemremarke = remarke[6]
        st.session_state.itemlast = last[6]
        st.session_state.pagecategoly = 1
    if itempage[7]:
        st.session_state.pic_src = p_url[7]
        st.session_state.itemserch_word = serch_word[7]
        st.session_state.itemtitle = title[7]
        st.session_state.itemprice = price[7]
        st.session_state.itemstate = state[7]
        st.session_state.itemremarke = remarke[7]
        st.session_state.itemlast = last[7]
        st.session_state.pagecategoly = 1
    if itempage[8]:
        st.session_state.pic_src = p_url[8]
        st.session_state.itemserch_word = serch_word[8]
        st.session_state.itemtitle = title[8]
        st.session_state.itemprice = price[8]
        st.session_state.itemstate = state[8]
        st.session_state.itemremarke = remarke[8]
        st.session_state.itemlast = last[8]
        st.session_state.pagecategoly = 1
    if itempage[9]:
        st.session_state.pic_src = p_url[9]
        st.session_state.itemserch_word = serch_word[9]
        st.session_state.itemtitle = title[9]
        st.session_state.itemprice = price[9]
        st.session_state.itemstate = state[9]
        st.session_state.itemremarke = remarke[9]
        st.session_state.itemlast = last[9]
        st.session_state.pagecategoly = 1        

if st.session_state.pagecategoly == 1:
    st.image(st.session_state.pic_src)
    st.write(st.session_state.itemtitle.iloc[-1])
    st.write(st.session_state.itemprice.iloc[-1])
    st.write(st.session_state.itemstate.iloc[-1])
    st.write(st.session_state.itemremarke.iloc[-1])
    st.write(st.session_state.itemlast.iloc[-1])
    option = st.text_input('備考を入力してください。※例：未開封')
    left_column, right_column = st.columns(2)
    back_list_page=left_column.button('標品一覧へ戻る')
    if back_list_page:
        st.session_state.pagecategoly =0
    buy_but = right_column.button("購入依頼")
    if buy_but:
        api_url = REQUEST_URL +'?&userid=' + userid +'&displayname=' + displayname +  '&p_id='+ st.session_state.pic_src + '&p_title=' + st.session_state.itemserch_word + '&option=' + option
        response = requests.get(api_url)
        st.title('已收到您的訂單')


# st.image(p_url)
# st.sidebar.title(p_title)
# st.sidebar.title('この商品を購入しますか？')
# option = st.sidebar.text_input('備考を入力してください。※例：未開封')
# buy_but = st.sidebar.button("購入依頼")
# if buy_but:
#     api_url = REQUEST_URL +'?&userid=' + userid +'&displayname=' + displayname +  '&p_title=' + p_title + '&option=' + option
#     response = requests.get(api_url)
#     print(api_url)
# st.sidebar.button("キャンセル")
