from handle_stock import HandleStock
import json
import pymongo
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from datetime import datetime
from typing import Optional

client = pymongo.MongoClient('mongodb://localhost:27017/')
collection = client["STOCK_DB"]['stock_col']
app = FastAPI()


@app.get("/stock_data/")
async def get_aggregated_stock_data_count(stock_id: int = Query(..., description="Stock ID"),
                                            start_date: str = Query(..., description="Start date (YYYY-MM-DD)"),
                                            end_date: str = Query(..., description="End date (YYYY-MM-DD)")):

    query = {
        "stock_id": int(stock_id),
        "date_string": {"$gte": start_date, "$lte": end_date}
    }
    cursor = list(collection.find(query))
    if cursor:
        try: 
            total_buy_haghighi_count, total_buy_hoghooghi_count, total_sell_haghighi_count, total_sell_hoghooghi_count = 0, 0, 0, 0 
            for doc in cursor:
                total_buy_haghighi_count += int(doc['buy_haghighi_Count'])
                total_buy_hoghooghi_count+= int(doc['buy_hoghooghi_Count']) 
                total_sell_haghighi_count+= int(doc['sell_haghighi_Count']) 
                total_sell_hoghooghi_count+= int(doc['sell_hoghooghi_Count']) 
            
            return {"total_buy_haghighi_count": total_buy_haghighi_count, 
                    "total_buy_hoghooghi_count": total_buy_hoghooghi_count,
                    "total_sell_haghighi_count": total_sell_haghighi_count, 
                    "total_sell_hoghooghi_count": total_sell_hoghooghi_count}
        except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="there is nothing in the mentioned period, check the time period or stock id")
    
@app.get("/stock_data_name/")
async def get_aggregated_stock_data_name_count(stock_name: str = Query(..., description="Stock Name"),
                                            start_date: str = Query(..., description="Start date (YYYY-MM-DD)"),
                                            end_date: str = Query(..., description="End date (YYYY-MM-DD)")):
        
    query = {
        "name": stock_name,
        "date_string": {"$gte": start_date, "$lte": end_date}
    }
    cursor = list(collection.find(query))
    if cursor:
        try: 
            total_buy_haghighi_count, total_buy_hoghooghi_count, total_sell_haghighi_count, total_sell_hoghooghi_count = 0, 0, 0, 0 
            for doc in cursor:
                total_buy_haghighi_count += int(doc['buy_haghighi_Count'])
                total_buy_hoghooghi_count+= int(doc['buy_hoghooghi_Count']) 
                total_sell_haghighi_count+= int(doc['sell_haghighi_Count']) 
                total_sell_hoghooghi_count+= int(doc['sell_hoghooghi_Count']) 
            
            return {"total_buy_haghighi_count": total_buy_haghighi_count, 
                    "total_buy_hoghooghi_count": total_buy_hoghooghi_count,
                    "total_sell_haghighi_count": total_sell_haghighi_count, 
                    "total_sell_hoghooghi_count": total_sell_hoghooghi_count}
        except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail="there is nothing in the mentioned period, check the time period or stock name")
    
