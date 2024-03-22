import json
import pandas as pd
from handle_stock import HandleStock
from datetime import date, timedelta, datetime
import pymongo

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_data(id: int, s_date: str, e_date: str, name: str) -> list:
    start_date = datetime.strptime(s_date, '%Y-%m-%d').date()
    end_date = datetime.strptime(e_date, '%Y-%m-%d').date()
    data = []
    for date in daterange(start_date, end_date):
        date_str = "".join((date.strftime("%Y-%m-%d")).split("-"))
        hs = HandleStock(id = id, date = date_str, stock_name = name)
        res = hs.get_analysis()
        if res!=None:
            data.append(res)

    return data

if __name__ == '__main__':
    # sid = input("Enter stock_id:")
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client["STOCK_DB"]
    print(f"Number of existed collections in STOCK_DB: {len(db.list_collection_names())} \n collections: {db.list_collection_names()}")
    collection = db['stock_col']
    start_date = input("Enter first date(format-> yyyy-m-d):")
    end_date = input("Enter second date(format-> yyyy-m-d):")
    stocks = json.load(open('./config/stock-ids.json', encoding="utf8"))
    for stock in stocks:
        d = get_data(id = stock['id'], s_date = start_date, e_date = end_date, name = stock['name'])
        if d:
            collection.insert_many(d)
