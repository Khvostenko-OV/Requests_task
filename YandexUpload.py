import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth ' + self.token}
        params = {'path': disk_file_path, 'overwrite': 'true'}
        resp = requests.get(url, headers=headers, params=params)
        return resp.json()

    def upload(self, disk_file_path, file_name):
        url = self._get_upload_link(disk_file_path)['href']
        resp = requests.put(url, data=open(file_name, 'rb'))
        return resp.status_code


if __name__ == '__main__':
    token = ''
    path_to_file = 'test.txt'
    yandex_disk_file_path = 'test.txt'

    uploader = YaUploader(token)
    result = uploader.upload(yandex_disk_file_path, path_to_file)
    if result == 201:
        print('Success!')
    else:
        print('Error!')
