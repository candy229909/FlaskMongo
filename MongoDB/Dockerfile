FROM mongo:latest

# �]�m�����ܶq�H���wMongoDB���ƾڦs�x���|�M��x�����|
# �`�N�GDocker�e������MongoDB�q�{�s�x���|�O /data/db�A��x���|�O /var/log/mongodb
# �H�U�]�m�i�H���ݭק�ΫO���q�{
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=password
ENV MONGO_INITDB_DATABASE=mydatabase

# �]�i��^�N��l�Ƹ}���ƻs��e�����A�Ω�Ыت�l�Τ�M�ƾڮw
# Docker�e���Ұʮɷ|����/docker-entrypoint-initdb.d�ؿ��U���Ҧ�.js�M.sh�}��
# COPY init-mongo.js /docker-entrypoint-initdb.d/

# �]�i��^�p�G�A�ݭn�۩w�q�t�m���A�i�H�N��K�[��e����
# COPY mongod.conf /etc/mongo/mongod.conf

# �}��27017�ݤf�A�H�K�~���X��MongoDB�A��
EXPOSE 27017