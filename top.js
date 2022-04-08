btn1 = document.getElementById("submit-btn1");
btn2 = document.getElementById("submit-btn2");
btn3 = document.getElementById("submit-btn3");
btn4 = document.getElementById("submit-btn4");
btn5 = document.getElementById("submit-btn5");
btn6 = document.getElementById("submit-btn6");
btn7 = document.getElementById("submit-btn7");
btn8 = document.getElementById("submit-btn8");
btn9 = document.getElementById("submit-btn9");
btn10 = document.getElementById("submit-btn10");
btn11 = document.getElementById("submit-btn11");
btn12 = document.getElementById("submit-btn12");
btn13 = document.getElementById("submit-btn13");
btn14 = document.getElementById("submit-btn14");
btn15 = document.getElementById("submit-btn15");
btn16 = document.getElementById("submit-btn16");
btn17 = document.getElementById("submit-btn17");
btn18 = document.getElementById("submit-btn18");
btn19 = document.getElementById("submit-btn19");
btn20 = document.getElementById("submit-btn20");

btnr = document.getElementById("rireki-btn");
btnr.setAttribute('onclick', 'pushButton2()');

btn1.setAttribute('onclick', 'pushButton1(this.id)');
btn2.setAttribute('onclick', 'pushButton1(this.id)');
btn3.setAttribute('onclick', 'pushButton1(this.id)');
btn4.setAttribute('onclick', 'pushButton1(this.id)');
btn5.setAttribute('onclick', 'pushButton1(this.id)');
btn6.setAttribute('onclick', 'pushButton1(this.id)');
btn7.setAttribute('onclick', 'pushButton1(this.id)');
btn8.setAttribute('onclick', 'pushButton1(this.id)');
btn9.setAttribute('onclick', 'pushButton1(this.id)');
btn10.setAttribute('onclick', 'pushButton1(this.id)');
btn11.setAttribute('onclick', 'pushButton1(this.id)');
btn12.setAttribute('onclick', 'pushButton1(this.id)');
btn13.setAttribute('onclick', 'pushButton1(this.id)');
btn14.setAttribute('onclick', 'pushButton1(this.id)');
btn15.setAttribute('onclick', 'pushButton1(this.id)');
btn16.setAttribute('onclick', 'pushButton1(this.id)');
btn17.setAttribute('onclick', 'pushButton1(this.id)');
btn18.setAttribute('onclick', 'pushButton1(this.id)');
btn19.setAttribute('onclick', 'pushButton1(this.id)');
btn20.setAttribute('onclick', 'pushButton1(this.id)');




function pushButton1(clicked_id) {
  let name = document.getElementById("user-name");
  let displayname = name.innerHTML;
  let user_id = document.getElementById("user_id");
  let userid = user_id.innerHTML;
  bun_num = clicked_id
  let tit = document.getElementById(bun_num);
  let item_cate = tit.value;
    let resurl=(`https://nyumallc.github.io/rensen/item.html?&userid=${userid}&displayname=${displayname}&itemcat=${item_cate}`)
    location.href=resurl
    
  };

  function pushButton2() {
    let user_id = document.getElementById("user_id");
    let userid = user_id.innerHTML;
    location.href=(`https://share.streamlit.io/nyumallc/streamlit_db/main/streamlit_db.py?f_num=rensen&userid=${userid}`)
     
    };
