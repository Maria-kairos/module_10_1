import time
from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    time_start1 = datetime.now()
    for i in range(word_count):
        with open(file_name, 'a', encoding='UTF-8') as file:
            file.write(f'Какое-то слово № {i + 1}' + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
    time_end1 = datetime.now()
    time_res1 = time_end1 - time_start1

time_start1 = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(time_res1)

time_start2 = datetime.now()

ww1 = Thread(target=write_words, args=(10, 'example5.txt'))
ww2 = Thread(target=write_words, args=(30, 'example6.txt'))
ww3 = Thread(target=write_words, args=(200, 'example7.txt'))
ww4 = Thread(target=write_words, args=(100, 'example8.txt'))

ww1.start()
ww2.start()
ww3.start()
ww4.start()

ww1.join()
ww2.join()
ww3.join()
ww4.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(time_res2)