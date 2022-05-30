import json
def get_fraud_info(page, limit):
    with open("./data/fraud_info.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
