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

def insert_logs_unordered_bulk(logs):
    """�ϥ�Unordered Bulk�ާ@��q���J��x"""
    collection = connect_to_mongodb()
    bulk = collection.initialize_unordered_bulk_op()
    for log in logs:
        bulk.insert(log)
    result = bulk.execute()
    return result

def write_log_to_mongodb(log_message, start_time=None, end_time=None):
    """�N��x�T���ΰ���ɶ��g�J��MongoDB"""
    log_entry = {
        "message": log_message,
        "timestamp": datetime.now(),
        "executime": execution_time
    }
    if start_time and end_time:
        log_entry['execution_time'] = (end_time - start_time).total_seconds()
    log_collection.insert_one(log_entry)



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

    # �Ыؤ@��Unordered Bulk�ާ@
bulk = collection.initialize_unordered_bulk_op()

result = insert_logs_unordered_bulk(logs)

# �K�[�h�Ӵ��J�ާ@
for i in range(10):  # �@���ܨҡA�ڭ̱N���J10����x
    log_entry = {
        "level": "info",
        "message": f"Log message {i}",
        "timestamp": datetime.datetime.now()
    }
    bulk.insert(log_entry)

# ����Bulk�ާ@
result = bulk.execute()