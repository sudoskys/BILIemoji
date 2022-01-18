# _*_ coding: utf-8 _*_
"""
__project__ = 'biliemoji'
__file_name__ = 'main'
__author__ = 'sudoskys'
__time__ = '1/18/22 8:36 PM'
__product_name__ = 'PyCharm'
__version__ = 'Jan182036'
# code is far away from bugs with the god，author here https://github.com/sudoskys
    ____  _
   / __ \(_)___ _____  ____ _
  / / / / / __ `/ __ \/ __ `/
 / /_/ / / /_/ / / / / /_/ /
/_____/_/\__,_/_/ /_/\__,_/
"""

# from PIL import ImageGrab
import os
# 批量修改图片尺寸
# imageResize(r"D:\tmp", r"D:\tmp\3", 0.7)
import time

import PIL.Image as Image

me = os.getcwd()


# 以第一个像素为准，相同色改为透明
def transparent_back(img):
    img = img.convert('RGBA')
    l, h = img.size
    color_0 = img.getpixel((0, 0))
    for h in range(h):
        for l in range(l):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot, color_1)
    return img


def mains(input_path, output_path, scale, width, height):
    # 获取输入文件夹中的所有文件/夹，并改变工作空间
    files = os.listdir(input_path)
    os.chdir(input_path)
    # 判断输出文件夹是否存在，不存在则创建
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for file in files:
        # 判断是否为文件，文件夹不操作
        if os.path.isfile(file):
            # img = Image.open(file)
            # width = int(img.size[0] * scale)
            # height = int(img.size[1] * scale)
            img = transparent_back(Image.open(file))
            # img.save("T_"+file)
            # img = Image.open(file)
            img = img.resize((width, height), Image.ANTIALIAS)
            img.save(os.path.join(output_path, "New_" + file))


def _file_safer(filename):
    import os
    file_dir = os.path.split(filename)[0]
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    if not os.path.exists(filename):
        os.system(r'touch %s' % filename)
    return filename


def pull(ids):
    names = []
    urls = []
    import requests
    import json
    # 请求地址
    url = "http://api.bilibili.com/x/emote/package?business=reply&ids=" + str(ids)
    response = requests.get(url)
    # 获取请求状态码 200为正常
    if response.status_code == 200:
        # 获取相应内容
        content = response.text
        # 字典
        json_dict = json.loads(content)
        if json_dict['code'] == 0:
            if json_dict['data']['packages']:
                json_list = json_dict['data']['packages'][0]['emote']
                # 打印所有结果
                for i in range(len(json_list)):
                    name = (str(json_list[i].get('package_id')) + '_' + str(json_list[i].get('text')))
                    url = (json_list[i].get('url'))
                    names.append(name)
                    urls.append(url)
                    print(name + "-->" + url)
                dicts = dict(zip(names, urls))
                print(dicts)
    else:
        print("请求失败!")
        dicts = False
    return dicts


def urllib_download(home, url, path):
    from urllib.request import urlretrieve
    ros = home + "/" + path + ".png"
    _file_safer(ros)
    urlretrieve(url, ros)


def run(opps):
    target = me + "/" + str(opps)
    home = target + "/work" + str(opps)
    do_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    datadict = pull(opps)
    if not datadict:
        print("No_data")
        with open(me + '/log.txt', 'a+') as f:
            f.write(do_time + "_NO_" + str(opps) + "\n")
        pass
    else:
        for n, u in datadict.items():
            print("STARTing//--//" + n)
            urllib_download(home, u, n)
        print("OK---*-*-*-*-*-*-*-*")
        with open(me + '/log.txt', 'a+') as f:
            f.write(do_time + "_DONE_" + str(opps) + "\n")
    # 执行图片处理
    mains(home, target + "/work_deal" + str(opps), 0.7, 512, 512)


if __name__ == '__main__':
    run(288)


    #  - 221 大航海嘉然  - 237 贝拉kira  - 245 嘉然今天吃什么 -288 向晚大魔王 -333 乃琳Queen  -339 珈乐Carol
