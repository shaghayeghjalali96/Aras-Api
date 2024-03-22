import pandas as pd
import requests 
import json
from io import StringIO
import uuid
from datetime import date, timedelta, datetime

class HandleStock:
    def __init__(self, id:int, date:int, stock_name:str) -> None:
        self.id = id
        self.date = date
        self.name = stock_name
        self.df = self.get_stock() 

    def get_stock(self):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        base_url = f'https://cdn.tsetmc.com/api/ClientType/GetClientTypeHistory/{self.id}/{self.date}'
        r = requests.get(base_url, headers=headers)
        if r.status_code==200:
            data = json.loads(r.text)
            return data["clientType"]
        return None
        
    def get_analysis(self):

        if self.df != None:
            string_date = self.date
            self.date = "-".join([self.date[:4],self.date[4:6] ,self.date[6:]])
            # print(datetime.strptime(self.date, '%Y-%m-%d').date())
            response = {"_id": str(uuid.uuid4()), "stock_id": self.id ,"name": self.name ,"date": datetime.strptime(self.date, '%Y-%m-%d').isoformat(), "date_string": string_date, 'buy_haghighi_Count': int(self.df["buy_I_Count"]), 'buy_hoghooghi_Count': int(self.df["buy_N_Count"]), "sell_haghighi_Count": int(self.df["sell_I_Count"]), 'sell_hoghooghi_Count': int(self.df["sell_N_Count"])}
            return response
        else:
            return None
