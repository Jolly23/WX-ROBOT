# coding=utf8
import json
import requests
from hashlib import md5


def chat_api(text, user_id=None):
    payload = {'key': 'a90fdac0979a333ec36ebc25f11ee1c9', 'info': text}
    if user_id:
        payload['userid'] = md5(str(user_id)).hexdigest()
    try:
        r_data = requests.get(
            url='http://www.tuling123.com/openapi/api',
            params=payload,
            timeout=1.5
        )
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
        return u'机器人可能生病了，睡得很香，暂时不能陪你聊天啦'
    data = json.loads(r_data.text)
    text = data.get('text')
    if data.get('code') == 200000:
        text += u', <a href="{}">点击查看</a>'.format(data.get('url'))
    return text
