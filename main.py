from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patient.json','r') as f :
        data = json.load(f)

    return data    

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
# segitcong change
@app.get('/about')
def about():
    return{"message":"hello i am om joshi, learning fast api"}

@app.get('/view')
def view():
    data = load_data()
    return data
