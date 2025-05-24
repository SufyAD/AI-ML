from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from db_helper import get_order_status, get_next_order_id, get_total_order_price, insert_order_item

app = FastAPI(
    title="Order Tracker API",
    description="API for tracking orders",
    version="1.0.0",
)

@app.get("/")
async def get():
    return{
        "status": "ok"
    }

@app.post("/")
async def handle_webflow(request: Request):
    try:
        payload = await request.json()
        
        intent = payload['queryResult']['intent']['displayName']
        param  = payload['queryResult']['parameters']
        output_contexts = payload['queryResult']['outputContexts']
        # session_id = generic_helper.extract_session_id(output_contexts[0]["name"])

        # routing table for intents and their respective functions
        
        intent_handler_dict = { # TODO: Updates the context
            'order.add - context: ongoing-order': order_add,
            'order.remove - context: ongoing-order': order_cancel,
            'order.complete - context: ongoing-order': order_complete,
            'order.track - context: Take User ID': order_track
         }
        
        return intent_handler_dict[intent](param)

        
    except Exception as e:
        print(f"Webhook error: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})
        
        
        
def order_track(parameters: dict):
    # grab id from parameter
    
    quantity  = int(parameters['number'])
    gym_item = int(parameters['gym-item'])
    
    insert_order_item(gym_item, quantity, order_id)

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })
    
async def order_add(parameters: dict):
    
    return {
        "fulfillmentText": "Order added"
    }
    
async def order_cancel(parameters: dict):
     return {
        "fulfillmentText": "Order Cancelled"
    }
     
     



    
    