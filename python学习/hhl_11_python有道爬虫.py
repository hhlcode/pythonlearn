import urllib.request as urls
import json
import urllib.parse as parses
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data={}
fanyistr= input("请输入翻译的内容")
data['type']='AUTO'
data['doctype']='json'
data['i']=fanyistr
data['xmlVersion']='2.1'
data['ue']='UTF-8'
data['Keyform']='fanyi.web'
data['typoResult']='fasle'
# 讲代码进行编码为utf-8形式
data = parses.urlencode(data).encode('utf-8')
# 访问有道翻译,提交数据
response = urls.urlopen(url,data)
# 获取有道翻译返回的数据并且进行解码
html = response.read().decode('utf-8')
# 进行json数据解码
target =json.loads(html)
print(target)
print("代码运行结束")