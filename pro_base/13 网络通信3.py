import urllib.request

url='http://localhost:8080/NoteWebService/logo.png'

req=urllib.request.Request(url)
with urllib.request.urlopen(url) as response:
    data=response.read()
    f_name='download.png'
    with open(f_name,'wb') as f:
        f.write(data)
        print('文件下载成功')






import urllib.request
import json

url='http://localhost:8080/NoteWebService/note.do?action=query&ID=10'

req=urllib.request.Request(url)   #创建Request请求  默认是get请求
with urllib.request.urlopen(req) as response:  #发送网咯请求 response是需要释放的对象
    data=response.read() #读取数据 为字节序列数据
    json_data=data.decode() #将字节序列数据 转换为字符串
    print(json_data)

    py_dict=json.loads(json_data)  #解码JSON字符串 返回字典
    record_array=py_dict["Record"]

    for record_obj in record_array:
        print('备忘录记录---------------')
        print("备忘录ID",py_dict["ID"])
        print("备忘录日期", py_dict["cDate"])
        print("备忘录内容", py_dict["Content"])
        print("用户ID", py_dict["UserID"])