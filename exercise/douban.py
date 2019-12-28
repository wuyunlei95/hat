import requests
import json

# 请求豆瓣网
response = requests.get("https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0")
print(response)
py_data = json.loads(response.text)
print(py_data)
# for i in py_data:
    # for j in i:
#     #     print(j)