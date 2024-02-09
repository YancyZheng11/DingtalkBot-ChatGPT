# DingtalkBot-ChatGPT
将ChatGPT接入到钉钉机器人中
![1](https://github.com/YancyZheng11/DingtalkBot-ChatGPT/blob/main/example/1.jpg)
## 使用方法：
### 第一步：
打开[钉钉管理后台](https://oa.dingtalk.com/)

创建或进入一个应用

获取应用的appKey和appSecret

打开start.py

将data_token里面的appKey和appSecret换成钉钉企业应用里面的appKey和appSecret

### 第二步：
打开[Openai后台](https://openai.com/)

获取api-key

（确保api-key里面还有额度）

打开start.py

将openai.api_key的值改成自己的api-key

将port的值改成想要的端口号

### 第三步：
打开钉钉企业应用管理

进入应用-应用功能-机器人与消息推送

将消息接受模式设置成HTTP模式

消息接收地址改成之前start.py里设置的接收地址

（确保这个地址能在公网上访问）

保存配置

（还没写完）
