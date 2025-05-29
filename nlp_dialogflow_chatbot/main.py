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
            'order.add : context: place an order'     : order_add,
            'order.add - context: ongoing-order'      : order_add,
            'order.complete - context: complete order': order_complete,
            'order.remove - context: ongoing-order'   : order_cancel,
            'order.track - context: Take User ID'     : order_track
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
        fulfillmentText = f"Your order contains: {order_str} so far. Do you need anything else?"
        
    return JSONResponse(content={
        "fulfillmentText": fulfillmentText
    })

            
def order_complete(parameters: dict, session_id: str):
    
    if session_id not in inprog_order:
        fulfillmentText = "I'm having a trouble finding your order. Sorry! Can you place a new order please?"
    else:
        current_order = inprog_order[session_id] # get the inprog_order in the current order
        order_id      = db_helper.save_order_to_db(current_order)
        total_price   =  db_helper.get_total_order_price(order_id)
        print(f"Total price {total_price}")
        
        # maybe an error will occur in db to insert new order
        if order_id == -1:
            fulfillmentText = "I'm having a trouble saving your order. Sorry! Can you place a new order please"
        else:
            if isinstance(current_order, list):
                items_text = "\n".join([f"- {item['gym_item']} x{item['quantity']}" for item in current_order])
            else:
                items_text = str(current_order)  # Fallback if not a list
                fulfillmentText = (
                    f"🧾 Order Details:\n"
                    f"📦 Order ID: {order_id}\n"
                    f"🛒 Items:\n{items_text}\n"
                    f"💰 Total Price: Rs. {total_price}"
                )
                
        del inprog_order[session_id] # remove the inprog from input buffer 
        
    return JSONResponse(content={
        "fulfillmentText": fulfillmentText
    })
    
def order_track(parameters: dict, session_id: str):
    if session_id:
        order_id = int(parameters['order-id'])
        print(order_id)
        status = db_helper.get_order_status(order_id)
        fulfillmentText = (
            f"🧾 Order Status: {status}"
        )
        return JSONResponse(content={
            "fulfillmentText": fulfillmentText
        })
    
    
async def order_cancel(parameters: dict):
    pass
     



    
    