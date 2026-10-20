from fastapi import FastAPI

app = FastAPI()

customers_profiles = {
    101:{'name':"atharva",'risk':"high"},
    102:{'name':"ravi",'risk':"low"},
    103:{'name':"pratik",'risk':"medium"}
}

@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id:int):
    
    profile = customers_profiles[customer_id]
    
    return {"name":profile['name'],
            "risk":profile["risk"]}
    
    
@app.get("/customer")
def get_customer(name,risk):
    return {name,risk}