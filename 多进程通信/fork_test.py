import os

def create_child(i):
    pid = os.fork()
    if pid > 0:
        print('in father process')
        return pid
    elif pid == 0:
        print('in child process', i)
        return 0
    else:
        raise

for i in range(10):  # 循环10次，创建10个子进程
    pid = create_child(i)
    # pid==0是子进程，应该立即退出循环，否则子进程也会继续生成子进程
    # 子子孙孙，那就生成太多进程了
    if pid == 0:
        break



