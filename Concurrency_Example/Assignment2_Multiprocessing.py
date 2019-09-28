import multiprocessing as mp
import os
import shutil


def worker():
    src = "State_CSVs"
    dest = "States_Copied_Multiprocessing"
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)


jobs = []
for i in range(mp.cpu_count()):
    p = mp.Process(target=worker)
    jobs.append(p)
    p.start()
