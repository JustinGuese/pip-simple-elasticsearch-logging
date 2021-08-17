from elasticsearch import Elasticsearch
from datetime import datetime
import json

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
        # errormessage should be a dict
        errordict = dict()
        if not isinstance(errormessage, dict):
            try:
                errordict = json.loads(errormessage)
            except (TypeError, ValueError):
                errordict = {"error" : errormessage}
        msg = {
            "app" : self.appname,
            "timestamp" : datetime.utcnow(),
        }
        errordict.update(msg)
        res = self.es.index(index=self.errorindexname, body=errordict)
        return res["result"]