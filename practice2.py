from fastapi import FastAPI
app=FastAPI()
@app.get('/customer')
def get_customer(customer_id:int):
    return{
        "custommer id": customer_id,
        "name":"Manoj",
        "status":"Active"
    }