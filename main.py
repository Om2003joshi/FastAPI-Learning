from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get('/about')
def about():
    return{"message":"hello i am om joshi, learning fast api"}
