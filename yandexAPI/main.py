from pprint import pprint

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        href = self.get_href(file_path)
        response = requests.put(href, data=open(file_path, "rb"))
        return response

    def get_href(self, file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path, "overwrite": "true"}
        headers = {"Authorization": self.token}
        resp = requests.get(url=url, params=params, headers=headers).json().get("href", "")
        return resp


if __name__ == '__main__':
    path_to_file = "pr.png"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    pprint(result)
