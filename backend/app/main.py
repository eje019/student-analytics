from fastapi import FastAPI

app = FastAPI(title="Student Analytics API")

@app.get("/")
def root():
    return {"message": "API Student Analytics"}