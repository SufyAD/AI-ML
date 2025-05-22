from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict
from db_helper import track_order_by_id

app = FastAPI()

@app.get("/")
async def get():
    return{
        "status": "ok"
    }

@app.post("/webhook")
async def dialogflow_webhook(request: Request):
    payload = await request.json()
    
    intent        = payload['queryResult']['action']
    param         = payload['queryResult']['parameter']
 
    if intent == "order.track":
        order_id   = param.get('order_id')
        return await track_order(order_id)
    
    return JSONResponse(content={"fulfillmentText": "Intent not handled."})
        
        
async def track_order(order_id: str|int):
    order = track_order_by_id(order_id)
    if order:
        message = f"Order {order['order_id']} is currently {order['status']}."
    else:
        message = "Sorry, we couldn't find your order."

    return JSONResponse(content={
        "fulfillmentText": message
    })
    