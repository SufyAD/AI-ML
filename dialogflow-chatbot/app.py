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

@app.post("/")
async def dialogflow_webhook(request: Request):
    try:
        payload = await request.json()
        
        intent = payload['queryResult']['action']
        param  = payload['queryResult']['parameters']
    
        if intent == "order.track":
            order_id   = param.get('order_id')
            return await order_track(order_id)
        
        return JSONResponse(content={"fulfillmentText": "Intent not handled."})
    except Exception as e:
        print(f"Webhook error: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
        
        
        
async def order_track(order_id: str|int):
    # order = track_order_by_id(order_id)
    # if order:
    #     message = f"Order {order['order_id']} is currently {order['status']}."
    # else:
    #     message = "Sorry, we couldn't find your order."

    return JSONResponse(content={
        "fulfillmentText": "HUrray OKAAaaaaaaaaaaaaay"
    })
    
    
async def order_add(param: dict):
    return {
        "fulfillmentText": "Order added"
    }
    
async def order_cancel(param: dict):
     return {
        "fulfillmentText": "Order Cancelled"
    }
     
     



    
    