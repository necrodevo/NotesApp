from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///notes.db",echo=True,pool_pre_ping=True)
def create_table():
    conn = engine.connect()
    result = conn.execute(text("CREATE TABLE IF NOT EXISTS NOTES" \
    "(note_id INTEGER PRIMARY KEY AUTOINCREMENT," \
    "AUTHOR TEXT NOT NULL," \
    "NOTE_DATA TEXT NOT NULL)"))
    conn.commit() # finalizing the query and commiting it
    conn.close() # closing the connection

def get_note(id:int):
    conn = engine.connect()
    result = conn.execute(text("Select AUTHOR, NOTE_DATA from NOTES where " \
    "note_id = :note_id"),{"note_id":id})
    conn.commit()
    conn.close()
    return result.fetchone()

def post_note(author:str,note:str):
    conn = engine.connect()
    result = conn.execute(text("Insert Into NOTES (AUTHOR,NOTE_DATA) " \
    "VALUES (:AUTHOR,:NOTE_DATA)"),{"AUTHOR":author,"NOTE_DATA":note})
    conn.commit()
    conn.close()
    return author