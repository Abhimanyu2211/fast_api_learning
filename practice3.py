from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class LoanApplication(BaseModel):
    age:int
    income:float
    loan_amount:float
    employment_years:float

@app.post('/predict')
def predict(Application: LoanApplication):
    if Application.income > 5000 and Application.employment_years > 2:
        decision = 'Approved'
    else:
        decision = 'Rejected'

    return{
    "application_age":Application.age,
    "result":decision
     }    

      