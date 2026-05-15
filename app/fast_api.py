from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_status():
    return {"message": "Running"}