import json
import re
import requests
import os
url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAqPm9xT_e2WIzApToAw-f9NsYzB_YrVLknWDzZ1V71uYKl4Uu0z9AmlAGvPirBmpH&count=21&max_cursor=1587728446000&aid=1128&_signature=o.0ycBAX.TZLJxANsBCt3KP9Mm&dytk=9669ddacdaafd1b8bfe2e55f4e137e90'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch'
                         'rome/83.0.4103.61 Safari/537.36'}
r = requests.get(url=url, headers=headers)
print(type(r), type(r.text))
url_list = list()
for i in range(len(json.loads(r.text)['aweme_list'])):
    url_list.append(json.loads(r.text)['aweme_list'][i]['video']['download_addr'])

# r = json.loads(r.text)['aweme_list'][0]['video']['download_addr']
# print(type(r))
pattern = re.compile('"(https://aweme.snssdk.com/aweme/v1/play/.*?)"')
r1 = json.dumps(url_list)
# print(len(r1))
result = pattern.findall(r1)
result = [i.split("&ratio")[0] for i in result]
# print(result)
result2 = [i.replace("/play/", "/playwm/") for i in result]

for i in result:
    print(i)
print(len(result))

# if not os.path.exists("无水印"):
#     os.mkdir("无水印")
if not os.path.exists(r"c:/f/tiktok"):
    os.mkdir(r"c:/f/tiktok")

count = 0
for res2 in result2:
    count += 1
    videoBin = requests.get(res2, timeout=5, headers=headers)
    with open(f'c:/f/tiktok/{count}.mp4', 'wb') as fb:
        fb.write(videoBin.content)