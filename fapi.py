from fastapi import FastAPI
from fastapi import HTTPException
import database as db # importing database

db.create_table() # creating the table in the database

app = FastAPI()

@app.get("/")
def get_main(name:str)->dict:
    return {"name":name}

@app.get("/note/{item_id}")
def get_notes(item_id:int)->dict:
    result = db.get_note(item_id)
    if result is not None: # none means no data was found
        return {"note":result[1],"author":result[0]} # returns the author and notes data from the returned result
    raise HTTPException(status_code=404,detail=f"Notes with {item_id} not found!")

@app.post("/note")
def create_product(author:str,note:str)->dict:
    result = db.post_note(author,note)
    if result is not None:
        print("check log!")
        return {"status":"Success"}
    raise HTTPException(status_code=405,detail=f"Issue With Internal Services!")