def parse_mongo_to_jsonable(item):
    item['id'] = str(item['_id'])
    del item['_id']
    return item
