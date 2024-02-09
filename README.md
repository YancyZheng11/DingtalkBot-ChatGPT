# DingtalkBot-ChatGPT
将ChatGPT接入到钉钉机器人中
![1](https://github.com/YancyZheng11/DingtalkBot-ChatGPT/blob/main/example/1.jpg)
## 使用方法：
### 第一步：
打开[钉钉管理后台](https://oa.dingtalk.com/)

创建或进入一个应用

创建一个机器人

创建一个钉钉企业内部群

在群里添加之前创建的机器人

获取机器人的webhook

打开start.py

将webhook的值改成机器人的webhook

### 第二步：
打开[Openai后台](https://openai.com/)

获取api-key

（确保api-key里面还有额度）

打开start.py

将openai.api_key的值改成自己的api-key

将port的值改成想要的端口号

### 第三步：
进入之前创建的应用

进入应用功能-机器人与消息推送

将消息接受模式设置成HTTP模式

消息接收地址改成之前start.py里设置的接收地址

（确保这个地址能在公网上访问）

![4](https://github.com/YancyZheng11/DingtalkBot-ChatGPT/blob/main/example/4.png)

调试确定没有问题后发布

### 使用：
运行start.py

在企业的内部群里@该机器人

并在后面填写要发送的消息