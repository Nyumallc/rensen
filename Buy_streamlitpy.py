import streamlit as st
import requests

params = st.experimental_get_query_params()
p_id = params['p_id'][0]
p_url = 'http://drive.google.com/uc?export=view&id=' + p_id
p_title = params['p_title'][0]
userid = params['userid'][0]
displayname = params['displayname'][0]
REQUEST_URL = 'https://script.google.com/macros/s/AKfycbw6u32KHeED0sedD72JwaEAMYLoeX6-VLk1kXY04Ac7r4Va-ppt1gGPI07X0J9kznM/exec'

st.image(p_url)
st.sidebar.title(p_title)
st.sidebar.title('この商品を購入しますか？')
option = st.sidebar.text_input('備考を入力してください。※例：未開封')
buy_but = st.sidebar.button("購入依頼")
if buy_but:
    api_url = REQUEST_URL +'?&userid=' + userid +'&displayname=' + displayname + '&p_id='+ p_id + '&p_title=' + p_title + '&option=' + option
    response = requests.get(api_url)
    print(api_url)
st.sidebar.button("キャンセル")