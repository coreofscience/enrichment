import collections
import requests
import json
from pymongo import MongoClient

client = MongoClient()
db = client.research


def main():
    page_size = 1000
    collection = db.products
    for i in range(3):
        r = requests.get(
            "https://www.datos.gov.co/resource/38rq-6esx.json",
            params={"$offset": page_size * i, "$limit": page_size},
        )
        for product in r.json():
            collection.insert_one(product)

        print(json.dumps(r.json(), indent=2))


if __name__ == "__main__":
    main()
