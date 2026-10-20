from fastapi import FastAPI
from pydantic import BaseModel

class Loanapplication(BaseModel):
    age:int
    loan_amount:int
    salary:int
    name:str
    
app = FastAPI()

@app.post("/abc")
def get_result(loanapplication:Loanapplication):
    if loanapplication.age <40 and loanapplication.salary>4000:
        decision = True
    else:
        decision= False
        
    return {'name':loanapplication.name,'decision':decision}