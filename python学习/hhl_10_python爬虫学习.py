import urllib.request as url
# # 访问一个网站,这个response是一个对象
# response=url.urlopen("http://www.fishc.com")
# # 将这个对象读取是二进制的文件
# html=response.read()
# print("第一次读取的网站源码",html)
# # 读取的文件应该是二进制的,将其解码
# html=html.decode("utf-8")
# print("解码以后的网站源码",html)
response= url.urlopen("http://placekitten.com/400/400")
cat_img=response.read()
# open() 函数用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。
# 'wb'是以二进制格式写入
with open('cat_img_400*400.jpg','wb')as f:
    f.write(cat_img)