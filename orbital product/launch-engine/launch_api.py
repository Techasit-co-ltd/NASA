
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Launch Engine Ready 🚀"}

@app.post("/launch")
def launch_product(product_name: str):
    return {
        "product": product_name,
        "launch_status": "Liftoff Successful 🚀",
        "orbit": "Stable",
        "timestamp": datetime.utcnow()
    }
