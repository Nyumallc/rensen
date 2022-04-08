function pushButton1(clicked_id) {
    bun_num = clicked_id
    let tit = document.getElementById(bun_num);
    let p_title = tit.title;
//     let name = document.getElementById("user-name");
//     let displayname = name.innerHTML;
//     let user_id = document.getElementById("user_id");
//     let userid = user_id.innerHTML;
    let resurl=(`https://share.streamlit.io/nyumallc/rensen/main/Buy_streamlitpy.py?&userid=${userid}&displayname=${displayname}&p_title=${p_title}`)
    location.href=resurl

    };
