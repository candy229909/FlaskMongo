FROM mongo:latest

# 設置環境變量以指定MongoDB的數據存儲路徑和日誌文件路徑
# 注意：Docker容器中的MongoDB默認存儲路徑是 /data/db，日誌路徑是 /var/log/mongodb
# 以下設置可以按需修改或保持默認
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=password
ENV MONGO_INITDB_DATABASE=mydatabase

# （可選）將初始化腳本複製到容器中，用於創建初始用戶和數據庫
# Docker容器啟動時會執行/docker-entrypoint-initdb.d目錄下的所有.js和.sh腳本
# COPY init-mongo.js /docker-entrypoint-initdb.d/

# （可選）如果你需要自定義配置文件，可以將其添加到容器中
# COPY mongod.conf /etc/mongo/mongod.conf

# 開放27017端口，以便外部訪問MongoDB服務
EXPOSE 27017