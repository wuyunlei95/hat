import requests
from lxml import etree
# 1.请求包图网拿到整体数据
response = requests.get("https://ibaotu.com/shipin/")
print(response.text)
# 把下载到的HTML源代码整理成XML文档对象
xml = etree.HTML(response.text)
# 2.抽取，视频标题，视频链接
tit_list = xml.xpath('//span[@class="video-title"]/text()')
src_list = xml.xpath('//div[@class="video-play"]/video/@src')
for tit, src in zip (tit_list, src_list):
    # pass
# 3.下载视频
    response = requests.get("http:" + src)
# 4.保存视频
    fileName = "D:\\video\\" + tit + ".mp4"
    with open(fileName, "wb") as f:
        f.write(response.content)