from fastapi import APIRouter

from modals.people import People
from config.db import conn
from schemas.people import peopleEntity , peoplesEntity
from bson.objectid import ObjectId

people = APIRouter()
@people.get('/')
async def find_all_people():
    print(conn.local.people.find())
    print(peoplesEntity(conn.local.people.find()))
    return peoplesEntity(conn.local.people.find())

@people.get('/{id}')
async def find_one_people(id):
    return peopleEntity(conn.local.people.find_one_and_delete({"_id":ObjectId(id)}))

@people.post('/')
async def create_people(people: People):
    conn.local.people.insert_one(dict(People))
    return peoplesEntity(conn.local.people.find())

@people.put('/{id}')
async def update_people(id,people: People):
    conn.local.people.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(people)
    })
    return peopleEntity(conn.local.people.find_one({"_id":ObjectId(id)}))

@people.delete('/{id}')
async def delete_people(id,people: People):
    return peopleEntity(conn.local.people.find_one_and_delete({"_id":ObjectId(id)}))