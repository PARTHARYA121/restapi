def peopleEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "name":item["name"],
        "age":str(item["_age"]),
        "gender":item["gender"]
    }

def peoplesEntity(entity) -> list:
    return [peopleEntity(item) for item in entity]