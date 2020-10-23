# -*- coding: UTF-8 -*-
from aip import AipOcr

# 定义常量
APP_ID = '21647273'
API_KEY = 'qk3p1gELsLrjMFI4E9ZKWGi3'
SECRET_KEY = 'WQVPU7F4HIHc4s15fmx3QjqeoGGGktyA'

# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('test5.png')
# 调用通用文字识别, 图片为本地图片
res = client.general(image)
print(res)

for item in res['words_result']:
    print(item['words'])