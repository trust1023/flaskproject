from multiprocessing import Pool
import os
import time


def test():
    print('test pid is %d and ppid is %d' % (os.getpid(), os.getppid()))
    for i in range(3):
        print('----i--- is %d' % i)
        time.sleep(1)
    return 'haha'  # 这个返回值会传递给callback设置的back函数


def back(args):
    print('--test callback pid is %d' % os.getpid())  # 这个函数是被主进程执行的，此处得到的是主进程的pid
    print('--test callback args is %s' % args)


if __name__ == '__main__':
    pool = Pool(10)  # 只添加了一个待执行的任务，此处写多少都没啥用，只一个进程会执行
    pool.apply_async(test, callback=back)
    # pool.close()
    # pool.join()
    print('---main pid is %d' % os.getpid())