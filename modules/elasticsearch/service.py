from .schemas.elasticsearch import ElasticsearchBulkEndpointPayload, ElasticsearchCreateIndexPayload
from .utils.elasticsearch import Elasticsearch


async def bulk_update(payload: ElasticsearchBulkEndpointPayload):
    return payload


def create_index(data: ElasticsearchCreateIndexPayload):
    host = data.host
    token = data.token if data.token else None
    
    index_name = data.index_name

    payload = {
        'settings': data.settings,
        'mappings': data.mappings,
        'aliases': data.aliases
    }

    elasticsearch_client = Elasticsearch(host, token)

    return elasticsearch_client.create_index(index_name, payload)