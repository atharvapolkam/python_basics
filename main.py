from fastapi  import FastAPI

app = FastAPI()

@app.get("/customer")
def get_customer(customer_id:int):
    return {"customer_id":customer_id,'name':'atharva'}


"""
you will get below response on these url
http://127.0.0.1:8000/customer?customer_id=10

{"customer_id":10,"name":"atharva"}

"""
