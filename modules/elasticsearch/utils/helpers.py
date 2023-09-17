from ..schemas.elasticsearch import ElasticsearchBasePayload
from ..utils.elasticsearch import Elasticsearch
from fastapi.responses import JSONResponse


def get_elastic_client(data: ElasticsearchBasePayload):
    host = data.host
    token = data.token if data.token else None

    return Elasticsearch(host, token)


def format_elasticsearch_response(response: object):
    status = response.get('status')if response.get('status') else 201
    return JSONResponse(status_code=status, content=response)