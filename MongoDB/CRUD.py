from pymongo import MongoClient
from bson.objectid import ObjectId

# 初始化MongoDB客戶端和選擇數據庫及集合
client = MongoClient('localhost', 27017)
db = client['log_db']
log_collection = db['logs']

def create_log(level, message):
    """創建一條日誌記錄"""
    log_entry = {"level": level, "message": message, "timestamp": datetime.datetime.now()}
    result = log_collection.insert_one(log_entry)
    print(f"Inserted log with id {result.inserted_id}")

def read_logs(level=None):
    """讀取日誌記錄，可以根據級別篩選"""
    query = {"level": level} if level else {}
    return list(log_collection.find(query))

def update_log(log_id, updated_message):
    """更新指定ID的日誌記錄"""
    result = log_collection.update_one(
        {"_id": ObjectId(log_id)},
        {"$set": {"message": updated_message}}
    )
    print(f"Updated {result.modified_count} log(s)")

def delete_log(log_id):
    """刪除指定ID的日誌記錄"""
    result = log_collection.delete_one({"_id": ObjectId(log_id)})
    print(f"Deleted {result.deleted_count} log(s)")

def insert_logs_unordered_bulk(logs):
    """使用Unordered Bulk操作批量插入日誌"""
    collection = connect_to_mongodb()
    bulk = collection.initialize_unordered_bulk_op()
    for log in logs:
        bulk.insert(log)
    result = bulk.execute()
    return result

def write_log_to_mongodb(log_message, start_time=None, end_time=None):
    """將日誌訊息及執行時間寫入到MongoDB"""
    log_entry = {
        "message": log_message,
        "timestamp": datetime.now(),
        "executime": execution_time
    }
    if start_time and end_time:
        log_entry['execution_time'] = (end_time - start_time).total_seconds()
    log_collection.insert_one(log_entry)



# 示範如何使用這些函數
if __name__ == "__main__":
    import datetime

    # 創建日誌
    create_log("info", "This is an info log")
    create_log("error", "This is an error log")

    # 讀取所有日誌
    for log in read_logs():
        print(log)

    # 更新日誌
    # 注意：你需要將'<log_id>'替換為實際的日誌條目ID
    # update_log('<log_id>', "Updated log message")

    # 刪除日誌
    # 注意：你也需要將'<log_id>'替換為實際的日誌條目ID
    # delete_log('<log_id>')

    # 創建一個Unordered Bulk操作
bulk = collection.initialize_unordered_bulk_op()

result = insert_logs_unordered_bulk(logs)

# 添加多個插入操作
for i in range(10):  # 作為示例，我們將插入10條日誌
    log_entry = {
        "level": "info",
        "message": f"Log message {i}",
        "timestamp": datetime.datetime.now()
    }
    bulk.insert(log_entry)

# 執行Bulk操作
result = bulk.execute()