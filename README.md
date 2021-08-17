Simple python pip package to log to elasticsearch.
The main focus of this package is simplicity, such that errorlogging becomes super easy and needs only to be set up once. 

# Usage

```
from elasticlogger import ElasticLogger
el = Elasticlogger()

def boundToFail():
    array = [2, 6, "tendies"]
    for elem in array:
        try:
            elem = elem / 2
        except Exception as e:
            msg = {
                "error" : repr(e),
                "elementWhereItHappened": elem,
                "otherNotes": "boundToFail Function"
            }
            el.log(msg)
            # raise

boundToFail()
```
## Elasticsearch connection

The connection supports host, port, user and password for elastic. 

The default values are - which can be changed:

- host="localhost"
- port=9200
- es_user = None
- es_pass = None
- appname = "app"
- errorindexname = "errors"

es_user and es_pass only need to be passed if xpack security in Elasticsearch is enabled, together with the Elasticsearch user. 


# Description

The good thing with a NoSql database is, that you can basically submit anything you want to the `log()` function as it takes everything. 

I created this even though other packages exist to make it even simpler to log to elastic, and to support username and password with Elasticsearch.