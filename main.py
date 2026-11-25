from fastapi import FastAPI

app = FastAPI(title="Pol-eat-heck API", version="0.1")

@app.get("/")
async def home():
    return {"version": "0.1"}