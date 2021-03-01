import pika

mq_host = '101.132.179.55'
mq_port = 5672
mq_name = 'guest'
mq_pwd = 'guest1111'

#身份验证凭证
credentials = pika.PlainCredentials(mq_name, mq_pwd)

#创建连接
s_conn = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host,port=mq_port,credentials=credentials))

#在