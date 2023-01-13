# urllib.request模块  get请求
import urllib.request

url='http://localhost:8080/NoteWebService/note.do?action=query&ID=10'

req=urllib.request.Request(url)   #创建Request请求  默认是get请求
with urllib.request.urlopen(req) as response:  #发送网咯请求 response是需要释放的对象
    data=response.read() #读取数据 为字节序列数据
    json_data=data.decode() #将字节序列数据 转换为字符串
    print(json_data)


# urllib.request模块  post请求
import urllib.request

url='https://www.baidu.com'

#准备http参数
params_dict={"action":"query","ID":'10'}
params_str=urllib.parse.urlencode(params_dict)  #将字典参数转化为字符串
print(params_str)

#字符串转化为字节序列对象
params_bytes=params_str.encode()  #发送post请求时 参数以字节序列形式发送

req=urllib.request.Request(url,data=params_bytes)  #发送post请求 创建了Request请求

with urllib.request.urlopen(req) as response:  #发送网咯请求 response是需要释放的对象
    data=response.read() #读取数据 为字节序列数据
    json_data=data.decode() #将字节序列数据 转换为字符串
    print(json_data)