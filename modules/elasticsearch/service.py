from .schemas.elasticsearch import ElasticsearchBulkEndpointPayload, ElasticsearchCreateIndexPayload
from .utils.helpers import get_elastic_client

def bulk_update(data):
    elasticsearch_client = get_elastic_client(data)
    return elasticsearch_client.bulk(data.payload)


def create_index(data: ElasticsearchCreateIndexPayload):    
    index_name = data.index_name

    payload = {
        'settings': data.settings,
        'mappings': data.mappings,
        'aliases': data.aliases
    }

    [ payload.pop(key) if not payload[key] else payload[key] for key in payload.copy().keys()]

    if not len(payload.keys()):
        payload = None

    elasticsearch_client = get_elastic_client(data)

    return elasticsearch_client.create_index(index_name, payload)