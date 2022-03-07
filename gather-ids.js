const fetch = require('fetch');

let headers = {
  'authority': 'api.twitter.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'none',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': 'personalization_id="v1_/yodfCSk8JMagf13sKeqQg=="; guest_id_marketing=v1%3A164356996542741341; guest_id_ads=v1%3A164356996542741341; guest_id=v1%3A164356996542741341; _gid=GA1.2.1832682732.1643569973; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCN2MZ6x%252BAToMY3NyZl9p%250AZCIlZjYxNGQwMWJiMTUxMWYwNjkwMjVkZTdkYmY0OWEyZjY6B2lkIiViZmQz%250AMTUyNTgzMGYzMzgyMWNhYTg4MGQ1OTQ5NjJkNQ%253D%253D--9aed3d5358f5d0b25528189f424daed29c5b80a4; kdt=WKRdNJrFTlbdFX1nA9uPV175NdmXaWZUXV1gwhjT; auth_token=2af39001f730c3846ada05f62c3c68e46b6a5818; ct0=c0742c38bf47f3982ca2f87a506e39b7940a83dc8446735d0ef6dc4258d95a2e1639027af147e7867f2739fbcc3970ca1d7bf2f79177a9f2995ade06c602353b7e3f639c8673e7692a3bc4d8562a98e8; twid=u%3D260175489; at_check=true; lang=en; _ga_BYKEBDM7DS=GS1.1.1643878898.1.0.1643879005.0; des_opt_in=Y; _gcl_au=1.1.1349307406.1643879244; eu_cn=Y; external_referer=padhuUp37zixoA2Yz6IlsoQTSjz5FgRcKMoWWYN3PEQ%3D|0|8e8t2xd8A2w%3D; mbox=session#a123bfd35b3f4fa48ee40631240797ba#1643882861|PC#a123bfd35b3f4fa48ee40631240797ba.37_0#1707125801; _ga=GA1.1.1326940938.1643569973; _ga_34PHSZMC42=GS1.1.1643878910.1.1.1643881012.0',
}

fetch(`https://api.twitter.com/1.1/users/search.json?q=${.replace(' ','+')}`, headers)
