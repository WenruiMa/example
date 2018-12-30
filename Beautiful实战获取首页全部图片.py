# coding:utf-8
from bs4 import BeautifulSoup
import requests
import urllib

def getlist():
    try:
        url = "http://www.youzi4.cc/"  # 所要请求的网址
        #url = "http://www.mm131.com/xinggan/"
        response = requests.get(url, timeout=5)  # 请求url 若超过5秒便自动放弃
        print(response.status_code)  # 打印网页状态码
        html = response.text  # 读取网页源代码
        soup = BeautifulSoup(html, "html.parser")  # 常规网页解析方式 python内置标准库，执行速度快
        # print(type(soup))
        ul = soup.find_all("img")# 查找网页中所有的img标签 ul 是一个列表
        list = [] # 初始化你一个空的列表用于存放 图片描述和链接
        for uls in ul: # 循环遍历ul
            #print(uls)  # <img alt="大腿上的玫瑰蛇纹身图案_大腿纹身图案" height="140" src="http://res.youzi4.cc//small/images/0129/09/52580962709.jpg?x-oss-process=image/resize,m_fill,w_190,h_140" width="190"/>
            alt = (uls.get("alt"))  #获取alt的文本描述
            # alt=uls["alt"]
            #print(type(alt))
            link = uls["src"] # 获取链接
            #print(link)
            content = (alt, link) #创建一个新的变量元组
            list.append(content) # 将元组中的数据添加到列表中
        print(len(list))
        return list # 返回列表

    except requests.exceptions.ConnectionError as e:  # 进行错误处理并输出原因
        print(e)


num = 1
for i in getlist(): # 循环遍历返回的列表值
    #print(i) # 返回一个元组元组的第一部分为图片描述 第二部分为链接
    if i[0] is None: # 有一部分为空的图片描述
        print("==================")
        print(type(i[0]))
    else:     
        name = i[0] # 获取图片描述，用于图片的名称
        url = i[1] # 获取图片的链接
        print(url)
        #print("正在保存" + name)
        print("正在保存" + str(name.encode("utf-8")))
        urllib.request.urlretrieve(url, "jpg/" + name + ".jpg") # 保存图片
        print(str(name.encode("utf-8")) + " 保存完成")
    num += 1 # num是用于循环一次继续循环的中间变量
