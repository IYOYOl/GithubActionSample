import requests
import json

url = "https://env-00jxtfd3wr9d.api-hz.cloudbasefunction.cn/functions/invokeFunction"

payload = {
  "method": "zeppStep",
  "params": [
    {
      "ip": "249.97.208.192",
      "zeppId": "1133421351",
      "appToken": "ZQVBQFJyQktGHlp6QkpbRl5LRl5qek4uXAQABAAAAAHypV5bKTBuTiDW9vN7FR4ODxDhoGkmBXWYj9WzJZCwnrcll35hRNWuO8qkxAkex5bL1vIu1FdwDnan-h0fat4cp9JPIi7nYKVhWc0NU2LjzE-5askc0outOPWcJU2tK8o-M7Hd_hSckCdKLDtDmaqR6othzUVvS6bg-ZjbGiQqxtdHxhJJomSGshQdcpMiC2Q",
      "step": "66666"
    }
  ],
  "clientInfo": {
    "PLATFORM": "web",
    "OS": "android",
    "APPID": "__UNI__3F9343F",
    "DEVICEID": "17468956407381144508",
    "scene": 1001,
    "appId": "__UNI__3F9343F",
    "appLanguage": "zh-Hans",
    "appName": "出去走走",
    "appVersion": "1.0.0",
    "appVersionCode": "100",
    "browserName": "chrome",
    "browserVersion": "134.0.6998.39",
    "deviceId": "17468956407381144508",
    "deviceModel": "V2207A",
    "deviceType": "phone",
    "hostName": "chrome",
    "hostVersion": "134.0.6998.39",
    "osName": "android",
    "osVersion": "14",
    "ua": "Mozilla/5.0 (Linux; Android 14; V2207A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.39 Mobile Safari/537.36",
    "uniCompilerVersion": "4.64",
    "uniPlatform": "web",
    "uniRuntimeVersion": "4.64",
    "locale": "zh-Hans",
    "LOCALE": "zh-Hans"
  }
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 14; V2207A Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.39 Mobile Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'x-to-function-name': "zeppTodo",
  'x-request-id': "14c6a6bb-98df-43c8-9ca8-79da0999dca5",
  'Authorization': "HMAC-SHA256 Credential=hzDTSCpEIdojYZSE, SignedHeaders=x-client-timestamp;x-from-app-id;x-from-env-id;x-from-function-name;x-from-instance-id;x-to-env-id;x-to-function-name, Signature=a59bfcc00d74d1e34fa63c0dc0a42a63de97d01fb29f77e8052a8e1df3f0361a",
  'x-from-env-id': "env-00jxtfd3wr9d",
  'sec-ch-ua': "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Android WebView\";v=\"134\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'x-from-instance-id': "1746981963411",
  'x-client-timestamp': "1746981963411",
  'x-to-env-id': "env-00jxtfd3wr9d",
  'x-trace-id': "14c6a6bb-98df-43c8-9ca8-79da0999dca5",
  'x-from-app-id': "2021005136661698",
  'x-alipay-source': "client",
  'x-from-function-name': "zeppTodo",
  'x-alipay-callid': "14c6a6bb-98df-43c8-9ca8-79da0999dca5",
  'Origin': "https://mm-2g2i5f9t68b62f2e-1305007022.tcloudbaseapp.com",
  'X-Requested-With': "privacy.explorer.fast.safe.browser",
  'Sec-Fetch-Site': "cross-site",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://mm-2g2i5f9t68b62f2e-1305007022.tcloudbaseapp.com/",
  'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)