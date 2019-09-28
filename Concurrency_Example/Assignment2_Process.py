from concurrent.futures import ProcessPoolExecutor
import os
import shutil


def worker():
    src = "State_CSVs"
    dest = "States_Copied_Processes"
    src_files = os.listdir(src)
    for index, file_name in enumerate(src_files):
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            with ProcessPoolExecutor(max_workers=5) as e:
                e.submit(shutil.copy(full_file_name, dest))


worker()




