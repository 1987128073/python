import time
import requests
import pymongo
from queue import Queue
from threading import Thread as Task
import redis


class Test_Proxie(object):
    num = 0

    def __init__(self):
        self.proxie_queue = Queue()

    def test_proxie(self):
        while True:
            print('开始测试')
            IP_PORT = self.proxie_queue.get()

            proxie = {
                'http': IP_PORT
            }

            try:
                response = requests.get(url='http://www.baidu.com', proxies=proxie, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}, timeout=20)
                if response.status_code == 200:
                    print(IP_PORT)
                    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
                    r = redis.Redis(connection_pool=pool)
                    r.sadd('ip_port_list', IP_PORT)
                    self.proxie_queue.task_done()
            except Exception as e:
                self.proxie_queue.task_done()

    def get_proxie_list_task(self):
        clent = pymongo.MongoClient("mongodb://localhost:27017/")
        items = clent.proxies.items

        for data in items.find({}, {'代理地址': 1}):
            ip_port = data['代理地址']
            daili = ip_port.replace('http://', '')

            self.proxie_queue.put(daili)
        print('代理获取完毕')

    def run(self):

        tasks = []
        get_proxie_list_task = Task(target=self.get_proxie_list_task)
        tasks.append(get_proxie_list_task)
        print('任务添加成功')
        for i in range(5):
            test_proxie = Task(target=self.test_proxie)
            tasks.append(test_proxie)

        for task in tasks:
            task.setDaemon(True)
            task.start()
            print('开始')

        # 保证子线程必须运行
        time.sleep(2)

        # 设置主线程退出条件
        for queue in [self.proxie_queue]:
            queue.join()


if __name__ == '__main__':
    proxie = Test_Proxie()
    proxie.run()