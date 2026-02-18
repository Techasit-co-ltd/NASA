
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/status")
def mission_status():
    return {
        "mission": "OPLS",
        "status": "Operational",
        "timestamp": datetime.utcnow()
    }
