import threading


class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__(self, name="threddy" + num)
        self.num = num

    def run(self):
        print("Thread ", self.num),


thread1 = MyThread("1")
thread2 = MyThread("2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
