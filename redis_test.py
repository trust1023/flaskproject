from redis import StrictRedis,ConnectionPool

# 使用默认方式连接到数据库
#pool = ConnectionPool(host='r-uf6443e9959cf3d4pd.redis.rds.aliyuncs.com',password='rds123QWEasd', port=6379, db=0)
# pool = ConnectionPool(host='r-bp1tuos481ooicxh3bpd.redis.rds.aliyuncs.com',password='rds123QWEasd', port=6379, db=0)
#
# redis_conn = StrictRedis(connection_pool=pool)
# print(redis_conn.dbsize()) #5736




# 使用默认方式连接到数据库
redis = StrictRedis(host='47.99.42.184', password='redis123456S',port=6379, db=0)
data = redis.rpop('qq')
print(data)

from multiprocessing import Queue

Queue.queue

