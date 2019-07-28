from threading import*
def Display():
    print('1This code executing by Thread: ',current_thread().getName())
    print('1This code executing by Thread: ',current_thread().getName())

print('This code executing by Thread: ',current_thread().getName())
Thread(target=Display).start()
print('This code executing by Thread: ',current_thread().getName())

# print('This code executing by Thread: ',current_thread().getName())

