from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()
notes = []

@app.get("/")
def get_main(name:str)->dict:
    return {"name":name}

@app.get("/note/{item_id}")
def get_notes(item_id:int)->dict:
    for dicts in notes:
        if dicts.get("id") == item_id:
            return {"id":item_id,"author":dicts.get("author"),"note":dicts.get("note")}
    raise HTTPException(status_code=404,detail=f"Notes with id {item_id} not found!")

@app.post("/note")
def create_product(author:str,note:str)->dict:
    notes.append({"id":len(notes),"author":author,"note":note})
    return {"id":len(notes) -1 ,"author":author,"note":note}
# using len -1 as index adjustment because when a new post is made the length is incremented by one 
# to resolve that we use -1 