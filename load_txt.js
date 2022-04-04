const url = new URL(window.location.href);
let params = url.searchParams;
let displayname=params.get('displayname');
let userid=params.get('userid');
let item_cate=params.get('itemcat');

