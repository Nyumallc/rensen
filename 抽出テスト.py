import pandas as pd
text_file = open("タイトルリスト.txt", "r",encoding="utf-8")
lines = text_file.read().split('\n')
for line in lines:
    line = line.replace('ONE PIECE','ONEPIECE')
    df = pd.read_csv('item_list.csv')
    harflist=[]
    sarch_list = df[df['title'].str.contains(line)]
    print(sarch_list)
    titles = sarch_list["ID"]
    h1="<input  type=image src=表示用写真/"
    h2=".jpg title="
    h3=" id=but"
    h4=' onclick=pushButton1(this.id) width=100 height=150 >'
    cunt=1
    for title in titles:
        try:
            title=str(int(title))
        except ValueError as e: 
            title=str(title)

        cunt_st = str(cunt)
        pic_harf = h1+title+h2+title+h3+cunt_st+h4
        harflist.append(pic_harf)
        cunt = cunt +1 

        
    # harfdf = pd.DataFrame(harflist)
    # html = harfdf.to_html()
    # text_file = open(r"test_id.html","w")
    # text_file.write(html)

        harfdf = pd.DataFrame(harflist)
        s_txt ="src/" + line + ".txt"
        harfdf.to_csv(s_txt, sep='\t', header=False, index=False)