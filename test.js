btn1 = document.getElementById("submit-btn");
btn1.setAttribute('onclick', 'pushButton1()');

function pushButton1() {
    let name = document.getElementById("user-name");
    let displayname = name.innerHTML;
    let user_id = document.getElementById("user_id");
    let userid = user_id.innerHTML;
    // let key = document.getElementById("keyword");
    // let key = key.value;

    let resurl=(`https://nyumallc.github.io/rensen/test2.html?&userid=${userid}&displayname=${displayname}`)
    const res = fetch(resurl);
    
  };
