from flask import request
from flask import Flask
import requests
import openai
import json

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def handle_request():
    if request.method == 'GET':
        return '200'

    elif request.method == 'POST':
        data_str = request.get_data(as_text=True)
        print(data_str)
        print(type(data_str))
        data = json.loads(data_str)
        input_ = data['text']['content']
        talk(input_)
        return '200'

    else:
        return 'error'

headers={'Content-Type': 'application/json'}
memory = []
port = 1145 # 填写端口号
openai.api_key = '' # 这里填写自己的openai api-key
webhook = '' # 这里填写钉钉机器人的webhook

def send(a):
    data = {"msgtype": "text", "text": {"content": a}}
    res = requests.post(webhook, data=json.dumps(data), headers=headers)
    print(res.text)

def talk(input):
    global out
    dic = {"role": "user", "content": input}
    memory.append(dic)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # 可自行更换语言模型
        messages = memory
    )

    global memory_short
    memory_short = completion.choices[0].message.content
    send(memory_short)
    memory.append(completion.choices[0].message)

if __name__ == '__main__':
    app.run(port=port)
