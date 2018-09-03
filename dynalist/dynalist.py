import requests as r
import json
from .exceptions import InvalidTokenError, RateLimitedError

FILES_AND_FOLDERS_ENDPOINT = "https://dynalist.io/api/v1/file/list"
DOCS_ENDPOINT = "https://dynalist.io/api/v1/doc/read"
SEND_TO_INBOX = "https://dynalist.io/api/v1/inbox/add"

class Dynalist():
    def __init__(self, token):
        self.token = token

    def all(self):
        params = {
            "token": self.token
        }

        res = r.post(FILES_AND_FOLDERS_ENDPOINT, data=json.dumps(params)).json()

        if res["_code"] == "InvalidToken":
            raise InvalidTokenError(res["_msg"])
        if res["_code"] == "TooManyRequests":
            raise RateLimitedError(res["_msg"])

        return res

    def doc(self, id):
        params = {
            "token": self.token,
            "file_id": id
        }

        return r.post(DOCS_ENDPOINT, data=json.dumps(params)).json()


    def to_inbox(self, content, note="", index=-1, checked=False, top=False):
        params = {
            "token": self.token,
            "index": index,
            "content": content,
            "note": note,
            "checked": checked
        }

        if top:
            params[index] = 0

        return r.post(SEND_TO_INBOX, data=json.dumps(params)).json()