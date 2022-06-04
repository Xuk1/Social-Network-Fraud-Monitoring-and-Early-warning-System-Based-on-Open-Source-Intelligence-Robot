import json
def get_fraud_info(page, limit):
    with open("./data/fraud_info.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    page = int(page)
    limit = int(limit)
    print(page, limit)

    start = (page-1)*limit
    end = start+limit

    data['data'] = data['data'][start: end]
    return data


def get_spider_info(page, limit):
    with open("./data/spider_info.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    page = int(page)
    limit = int(limit)
    # print(page, limit)

    start = (page-1)*limit
    end = start+limit

    data = data['data']
    data = data[start: end]
    print(data)
    return data
