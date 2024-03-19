from pymongo import MongoClient
from bson.objectid import ObjectId

# ��l��MongoDB�Ȥ�ݩM��ܼƾڮw�ζ��X
client = MongoClient('localhost', 27017)
db = client['log_db']
log_collection = db['logs']

def create_log(level, message):
    """�Ыؤ@����x�O��"""
    log_entry = {"level": level, "message": message, "timestamp": datetime.datetime.now()}
    result = log_collection.insert_one(log_entry)
    print(f"Inserted log with id {result.inserted_id}")

def read_logs(level=None):
    """Ū����x�O���A�i�H�ھگŧO�z��"""
    query = {"level": level} if level else {}
    return list(log_collection.find(query))

def update_log(log_id, updated_message):
    """��s���wID����x�O��"""
    result = log_collection.update_one(
        {"_id": ObjectId(log_id)},
        {"$set": {"message": updated_message}}
    )
    print(f"Updated {result.modified_count} log(s)")

def delete_log(log_id):
    """�R�����wID����x�O��"""
    result = log_collection.delete_one({"_id": ObjectId(log_id)})
    print(f"Deleted {result.deleted_count} log(s)")

# �ܽd�p��ϥγo�Ǩ��
if __name__ == "__main__":
    import datetime

    # �Ыؤ�x
    create_log("info", "This is an info log")
    create_log("error", "This is an error log")

    # Ū���Ҧ���x
    for log in read_logs():
        print(log)

    # ��s��x
    # �`�N�G�A�ݭn�N'<log_id>'��������ڪ���x����ID
    # update_log('<log_id>', "Updated log message")

    # �R����x
    # �`�N�G�A�]�ݭn�N'<log_id>'��������ڪ���x����ID
    # delete_log('<log_id>')