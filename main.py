from fastapi import FastAPI,HTTPException,status,Body
from models import Note,User,UserLogin,Token
from auth import create_access_token,get_current_user
from db_config import notes_collection,user_collection
from passlib.context import CryptContext
from bson import ObjectId
import datetime
import bcrypt

app =FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)

@app.post("/create_user/",description="Create a new user")
def create_user(user:User):
    if user_collection.find_one({"email":user.email}):
        return {"message":"User already exists with this email"}
    user_dict={
        "username":user.username,
        "email":user.email,
        "password": get_password_hash(user.password),

    }
    user_collection.insert_one(user_dict)
    return {"message":"User created successfully"}

@app.post("/login/")
def login(user:User):
    user_data=user_collection.find_one({"email":user.email})
    if user_data and verify_password(user.password,user_data["password"]):
        token=create_access_token({"sub":user.email})
        return {"access_token":token,"token_type":"bearer"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")


@app.post("/notes/",description="Creatte a new note")
async def create_note(note:Note = Body(...),token: Token= Body(...)):
    user=await get_current_user(token.access_token)
    if not user:
        return {"message":"User does not exist"}
    if notes_collection.find_one({"title":note.title}):
        return {"message":"Note already exists with this title"}
    note_dict={
        "title":note.title,
        "content":note.content,
        "tags":note.tags,
        "created_at":datetime.datetime.now(),
        "updated_at":datetime.datetime.now(),
        "reminder_date":note.reminder_date,
    }
    notes_collection.insert_one(note_dict)
    return {"message":"Note created successfully"}


@app.get("/notes/", description="Get all notes")  
def get_all_notes():
    notes = notes_collection.find()
    all_notes = []
    for note in notes:
        note["_id"] = str(note["_id"]) 
        all_notes.append(note)
    return all_notes

@app.get('/note/{id}/', description='Get a single note by Id')
def get_single_note(id:str):
    note= notes_collection.find_one({'_id':ObjectId(id)})
    if note:
        note['_id']=str(note['_id'])
        return note
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Note not found')

@app.put('/note/{id}/', description='Update a note by Id')
def update_note(id:str, note:Note):
    note_dict={
        "title":note.title,
        "content":note.content,
        "tags":note.tags,
        "updated_at":datetime.datetime.now(),
        "reminder_date":note.reminder_date,
    }
    res=notes_collection.update_one({'_id':ObjectId(id)},{'$set':note_dict})
    if res.modified_count==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Note not found')
    return {"message":"Note updated successfully"}

@app.delete('/note/{id}/', description='Delete a note by Id')
def delete_note(id:str):
    res=notes_collection.delete_one({'_id':ObjectId(id)})
    if res.deleted_count==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Note not found')
    return {"message":"Note deleted successfully"}

@app.get('/notes/search/', description='Search notes by title')
def search_notes(title:str):
    notes=notes_collection.find({'title':{'$regex':title,'$options':'i'}})
    all_notes=[]
    for note in notes:
        note['_id']=str(note['_id'])
        all_notes.append(note)
    return all_notes

@app.get('/notes/reminders/', description='Get notes with reminders')
def get_reminder_notes():
    notes=notes_collection.find({'reminder_date':{'$lte':datetime.datetime.now()}})
    all_notes=[]
    for note in notes:
        note['_id']=str(note['_id'])
        all_notes.append(note)
    return all_notes