from ..schemas.elasticsearch import ElasticsearchBasePayload
from ..utils.elasticsearch import Elasticsearch


def get_elastic_client(data: ElasticsearchBasePayload):
    host = data.host
    token = data.token if data.token else None

    return Elasticsearch(host, token)