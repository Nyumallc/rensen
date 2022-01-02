
window.onload = function() {
  const liffClient = setLiffClient()

  // setup をする
  liffClient(() => { if(!liff.isLoggedIn())liff.login(); })
  getProfile(liffClient)
};

const setLiffClient = () => {
  return (func) => { liff.init({ liffId: LIFF_ID }).then(func) }
};

const getProfile = async (liffClient) => {
  liffClient(() => {
    liff.getProfile().then((profile) => {
      // 02. プロフィールにユーザー名を表示してみよう
      document.getElementById('user-name').innerText = profile.displayName
      document.getElementById('icon').src = profile.pictureUrl
      document.getElementById('user_id').innerText = profile.userId
    })
  })
};