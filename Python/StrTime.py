import time

start_time = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime())
print("今天是",start_time)
tt = time.time() + 10*60*60*24

start_time = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(tt))
print("10天后是",start_time)
