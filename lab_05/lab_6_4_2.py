import random
import os
from glob import glob
from threading import Thread
from queue import Queue
import time

extensions = [
    "txt", "log", "h", "xml"
]

def create_dirs():
    for i in range(10):
        os.mkdir(f"./dir{i+1}")

def task_creation():
    create_dirs()
    dir_files_count = []
    for i in range(10):
        dir_files_count.append(random.randint(1, 25))

    for i in dir_files_count:
        print(i)

    for i in range(len(dir_files_count)):
        cnt = 0
        for j in range(dir_files_count[i]):
            fileName = f'./dir{i + 1}/File{cnt}.{extensions[random.randint(0, len(extensions) - 1)]}'
            cnt += 1
            with open(fileName, 'w') as newBornFile:
                if fileName.find(".txt") != -1:
                    if random.randint(1, 100) > 50:
                        newBornFile.write("asdf")


def print_matrix(mtx):
    for row in mtx:
        for el in row:
            print(el, end=' ')
        print()


def separate_files_for_threads(file_cnt, thread_count, file_list):
    files_for_threads = []
    cur_files = []
    cur_files_cnt = 0
    file_per_thread = int(file_cnt / thread_count)
    for i in file_list:
        if cur_files_cnt < file_per_thread:
            cur_files.append(i)
            cur_files_cnt += 1
        else:
            files_for_threads.append(cur_files.copy())
            cur_files.clear()
            cur_files.append(i)
            cur_files_cnt = 1
    if cur_files_cnt > 0:
        files_for_threads.append(cur_files)
    return files_for_threads

def find_keyword_in_files(files_list, keyword, q):
    keyword_cnt = 0
    for filename in files_list:
        with open(filename, "r") as file:
            text = file.read()
            keyword_cnt += text.split().count(keyword)
    q.put(keyword_cnt)

def find_all_txt_files():
    file_list = []
    for filename in glob('./**/*.txt', recursive=True):
        file_list.append(filename)
    return file_list

def run_thread_version(files_for_threads, keyword, thread_count):
    keyword_cnt = 0
    q = Queue(thread_count)
    start = time.time()
    for i in range(thread_count):
        cur_thread = Thread(target=find_keyword_in_files, args=(files_for_threads[i], keyword, q))
        thread_list.append(cur_thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
    thread_list.clear()

    for i in q.queue:
        keyword_cnt += i
    q.queue.clear()
    end = time.time()

    #print(keyword_cnt)

    return end - start

def run_non_thread_version(file_list):
    keyword_cnt = 0
    start = time.time()
    for filename in file_list:
        with open(filename, "r") as file:
            text = file.read()
            keyword_cnt += text.split().count(keyword)
    end = time.time()
    #print(keyword_cnt)
    return end - start


if __name__ == '__main__':
    file_list = find_all_txt_files()
    file_cnt = len(file_list)
    N = 1000
    keyword = "asdf"
    keyword_cnt = 0
    thread_count = 8

    files_for_threads = separate_files_for_threads(file_cnt, thread_count, file_list)
    thread_list = []
    elapsed_thread_time = 0
    elapsed_time = 0

    run_non_thread_version(file_list)

    for tries in range(N):
        elapsed_thread_time += run_thread_version(files_for_threads=files_for_threads, keyword=keyword, thread_count=thread_count)
        elapsed_time += run_non_thread_version(file_list)

    print(f"Program with {thread_count} threads runs in {elapsed_thread_time / N} seconds as average time")
    print(f"Program without threads runs in {elapsed_time / N} seconds as average time")

    print(keyword_cnt)
