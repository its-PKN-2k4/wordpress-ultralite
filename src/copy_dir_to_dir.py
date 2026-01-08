import shutil
import os

def copy_dir_to_dir(src, dest):
    files = os.listdir(src)
    if not files:
        raise Exception("Nothing to copy from source")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

    for fname in files:
        if not os.path.isfile(os.path.join(src, fname)):
            copy_dir_to_dir(os.path.join(src, fname), os.path.join(dest, fname))
        else:
            shutil.copy(os.path.join(src, fname), dest)