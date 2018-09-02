import requests as r
import json

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

        return r.post(FILES_AND_FOLDERS_ENDPOINT, data=json.dumps(params)).json()

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

if __name__ == "__main__":
    dyn = Dynalist("AwVgFithnTBvUxBwOxZNizIYYpJzuJyFHeJwk66w8oToWZWfe2c9uWnyv1UOUDtJfVMFbFWfNpVIpwNFLK38c8DYLQ_JBJVsSbywHdVz8L0xYQff2XkoFb1KcICPJ8u0")
    print(dyn.all())
    #print(dyn.doc("VpfKdXb72Br93aCC1tO2Yf6H"))