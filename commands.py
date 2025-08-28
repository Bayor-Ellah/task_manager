import db

def save_task(task):
    #save task to database
    db.tasks.insert_one(task)
    #return response
    return True

def delete_task(id):
    #delete the task from the database
    db.tasks.delete_one({"_id": id})
    #treturn response
    return True

def get_tasks():
    #get all the task from database
    all_tasks = db.tasks.find()
    #return response
    return all_tasks



def update_tasks(id, update):
    #update task in database
    db.tasks.update_one({"_id": id}, {"$set": update})
    #return response
    return True