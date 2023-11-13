import logging
import threading
import time
from multiprocessing import Process

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%H:%M:%S:%MS')
logger = logging.getLogger(__name__)
names = ['America', 'Europe', 'Africa']

# 同期的な関数
def sync_func(name):
    time.sleep(2)
    logger.debug(f'Synchronous task completed: {name}')

# 非同期的な関数
def async_func(name):
    threading.Thread(target=sync_func, args=(name,)).start()

if __name__ == "__main__":
    # 並行性のデモ
    for name in names:
        async_func(name)
        logger.debug(f'Asynchronous task started: {name}')

    # 並列性のデモ
    processList = []
    for name in names:
        proc = Process(target=sync_func, args=(name,))
        processList.append(proc)
        proc.start()

    for proc in processList:
        proc.join()

    logger.debug('All tasks completed')
