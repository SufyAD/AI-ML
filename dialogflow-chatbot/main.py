from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import db_helper
import api_helper

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

inprog_order = {}

@app.post("/")
async def handle_webflow(request: Request):
    try:
        payload = await request.json()
        
        intent          = payload['queryResult']['intent']['displayName']
        param           = payload['queryResult']['parameters']
        output_contexts = payload['queryResult']['outputContexts']
        session_id      = api_helper.get_session_id(output_contexts[0]["name"]) # of existing order

        # routing table for intents and their respective functions
        intent_handler_dict = { # TODO: Updates the context
            'order.add : context: place an order'    : order_add,
            'order.add - context: ongoing-order'     : order_add,
            'order.complete - context: Place the order': order_complete,
            'order.remove - context: ongoing-order'  : order_cancel,
            'order.track - context: Take User ID'    : order_track
         }
        return intent_handler_dict[intent](param, session_id)
    
    except Exception as e:
        print(f"Webhook error: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})


def order_add(parameters: dict, session_id: str):
    order_items = parameters["gym-item"]
    quantities  = parameters["number"]
    
    if len(order_items) != len(quantities):
        fulfillmentText = "Please specify quantity with ordered item(s)"
    else:
        new_order = dict(zip(order_items, quantities))
        # check if it is new or existing order
        if session_id in inprog_order:
            current_order = inprog_order[session_id]
            current_order.update(new_order)
            inprog_order[session_id] = current_order # update the inprogress order
        else:
            inprog_order[session_id] = new_order
        
        order_str = api_helper.get_str_from_dict(inprog_order[session_id]) # for safe side
        # for debugging
        print(order_str) 
        
        fulfillmentText = f"So you have ordered: \n{order_str} so far. Do you need anything else?"
        
        return JSONResponse(content={
        "fulfillmentText": fulfillmentText
    })

            
def order_complete(parameters: dict, session_id: str):
    if session_id not in inprog_order:
        fulfillmentText = "I'm having a trouble finding your order. Sorry! Can you place a new order please?"
    else:
        current_order    = inprog_order[session_id] # get the inprog_order in the current order
        print(current_order)
        order_id = db_helper.save_order_to_db(current_order)
        total_price =  db_helper.get_total_order_price(order_id)
        print(total_price)
        
        # maybe an error will occur in db to insert new order
        if order_id == -1:
            fulfillmentText = "I'm having a trouble saving your order. Sorry! Can you place a new order please"
        else:
            fulfillmentText = f"Here are your order details:\n Order items : {current_order}\nTotal price: {total_price}"
        
        del inprog_order[session_id] # remove the inprog from input buffer 
        
    return JSONResponse(content={
        "fulfillmentText": fulfillmentText
    })
    
def order_track(parameters: dict):
    pass
    
async def order_cancel(parameters: dict):
    pass
     



    
    