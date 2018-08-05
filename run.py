import multiprocessing
import subprocess
import time

#runs multiple scripts

WORKERS = 6

def worker():
    subprocess.call("main.py", shell=True)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(WORKERS):
        time.sleep(1.5)
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()