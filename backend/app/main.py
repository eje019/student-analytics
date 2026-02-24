from fastapi import FastAPI

app = FastAPI(title="Student Analytics API")

@app.get("/")
def root():
    return {"message": "C'est maginifique"}

@app.get("/test")
def test():
    return{"message": "on est sur la page test"}