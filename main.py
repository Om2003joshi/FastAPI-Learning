from fastapi import FastAPI, Path,HTTPException,Query
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


@app.get('/patient/{patient_id}')
def view_patient(patient_id:str = Path(..., description="The ID of the patient in DB",example="P001")):
    # load all patitent_id
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")    

@app.get('/sort')
def sort_patient(sort_by:str=Query(...,description="sort on the bbasic od height,weight,and bmi"),order:str=Query('asc',description='sort in asc or descding order')):
    valid_fields = ['height', 'weight', 'bmi']
                    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid sort_by field. Must be one of {valid_fields}") 

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="Invalid order. Must be 'asc' or 'desc'")

    data = load_data()
    sort_order= True if order=='desc' else False
    sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=False)    
