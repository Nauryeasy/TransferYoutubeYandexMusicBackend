import requests
from flask import Flask, request
from transfer_music import *
from threading import Thread

app = Flask(__name__)


def download_song(data):
    post_target = data['post_target']
    url_song = data['url_song']
    send_to_yandex(get_info(url_song), post_target)


@app.route('/', methods=['POST'])
def get_music():
    data = request.get_json()
    th = Thread(target=download_song, kwargs={'data': data})
    th.start()
    return {'result': 'OK'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4989)
