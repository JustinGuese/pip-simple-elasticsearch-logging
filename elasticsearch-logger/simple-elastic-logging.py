from elasticsearch import Elasticsearch
from datetime import datetime

class ElasticLogger:
    def __init__(self, host="localhost", port=9200, es_user = None,es_pass = None, appname = "app", errorindexname = "errors") -> None:
        if not (es_user is None and es_pass is None):
            auth = (es_user, es_pass)
            self.es = Elasticsearch(host = host, port = port, http_auth = auth)
        else:
            self.es = Elasticsearch(host = host, port = port)
        self.errorindexname = errorindexname
        self.appname = appname
        
    def log(self, errormessage):
        msg = {
            "app" : self.appname,
            "timestamp" : datetime.utcnow(),
            "error" : errormessage
        }
        res = self.es.index(index=self.errorindexname, body=msg)
        return res["result"]