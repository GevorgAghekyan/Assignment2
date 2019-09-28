import os
import shutil


def worker():
    src = "State_CSVs"
    dest = "States_Copied_Normally"
    src_files = os.listdir(src)
    for index, file_name in enumerate(src_files):
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)


worker()




