from .schemas.elasticsearch import ElasticsearchBulkEndpointPayload

async def bulk_update(payload: ElasticsearchBulkEndpointPayload):
    return payload

