const p_url = new URL(window.location.href);
url=decodeURIComponent(p_url)
let params = url.searchParams;
let displayname=params.get('displayname');
let userid=params.get('userid');
let item_cate=params.get('itemcat');
let item=decodeURI(item_cate)


