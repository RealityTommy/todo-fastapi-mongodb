def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"],
        "uid": todo["uid"]
    }

def list_serial(todos) -> list:
    return [individual_serial(todo) for todo in todos]