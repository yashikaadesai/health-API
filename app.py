from fastapi import FastAPI, Request
from utils.analysis import assess_health
import json

app=FastAPI()

@app.post("/project-health")
def get_project_health():
    with open("data/mock_project_data.json","r") as f:
        data=json.load(f)
    result = assess_health(data)
    return result 