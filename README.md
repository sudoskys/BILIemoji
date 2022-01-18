# BILIemoji

哔哩哔哩表情包， 自动抠图透明化背景， 下载表情， 使用Python, 自动缩放调大小

### USE
```python
if __name__ == '__main__':
    run(237)
    # - 288 向晚 - 237 贝拉  - 221 大航海嘉然  - 237 贝拉kira  - 245 嘉然今天吃什么 -288 向晚大魔王 -333 乃琳Queen  -339 珈乐Carol
    # 这里填表情包ID
    # Id从http://api.bilibili.com/x/emote/user/panel/web?business=reply查看自己的，来源
```

>TIPS：main.py 适用于各个平台，使用os获取路径，linux&windows都可以运行.

### ID获取方法
http://api.bilibili.com/x/emote/user/panel/web?business=reply 查看自己的，浏览器需要登陆bilibili

#### 数据举例
```
{"id":5112,"package_id":237,"text":"[贝拉kira_笔芯]","url":"http://i0.hdslb.com/bfs/emote/3cbc05078eee45c0861ce37e63092e379ae93d57.png","mtime":1637148616,"type":3,"attr":0,"meta":{"size":2,"suggest":[""],"alias":"笔芯"}
```
```package_id``` 即需要的参数.


#### Source
https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/emoji/list.md#%E8%8E%B7%E5%8F%96%E6%88%91%E7%9A%84%E8%A1%A8%E6%83%85%E5%88%97%E8%A1%A8



### 默认调大小512
```python
mains(HOMEWORK, HOME + "/workdeal"+ str(opps), 0.7, 512, 512)
# 0.7为缩放比例，但是因为我注释掉了，所以不起作用..
```
