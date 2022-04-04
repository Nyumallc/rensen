import pandas as pd

df = pd.read_csv('item_list.csv')
harflist=[]
sarch_list = df.query('title.str.contains("フィギュア")', engine='python')
titles = sarch_list["ID"]
h1="<input  type=image src=表示用写真/"
h2=".jpg title="
h3=" id=but"
h4=" width=100 height=150 >"
cunt=1
for title in titles:
    cunt_st = str(cunt)
    pic_harf = h1+str(int(title))+h2+str(int(title))+h3+cunt_st+h4
    harflist.append(pic_harf)
    cunt = cunt +1 

    
# harfdf = pd.DataFrame(harflist)
# html = harfdf.to_html()
# text_file = open(r"test_id.html","w")
# text_file.write(html)

harfdf = pd.DataFrame(harflist)
harfdf.to_csv('test_id.txt', sep='\t', header=False, index=False)