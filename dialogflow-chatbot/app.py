from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI()


@app.post("/")
async def dialogflow_webhook(request: Request):
    payload = await request.json()
    
    # i.e order.track
    intent        = payload['queryResult']['action']
    param         = payload['queryResult']['parameter']
    outputContext = payload['queryResult']['outputContexts']['name']
 
    # Example logic based on intent
    if intent == "order.track":
        # we need to call track order here
        track_order(parameter=param)
        
        
async def track_order(parameter:dict):
    return JSONResponse(content={
        "fulfillmentText": "Your order is being processed.",
        "parameter": {parameter}
    })
    