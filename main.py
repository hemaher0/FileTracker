import os
import shutil
import threading
import time
import keyboard

keep_going = True
def key_capture_thread():
    global keep_going
    a = keyboard.read_key()
    if a== "esc":
        print("The process is finished.")
        keep_going = False



def compare(filepath, currentfilepath):
    r = 1
    fatime = os.path.getatime(filepath)
    catime = os.path.getatime(currentfilepath)
    fsize = os.path.getsize(filepath)
    csize = os.path.getsize(filepath)
    if fatime != catime:
        r = 0
    if fsize != csize:
        r = 0
    return r

def copy():
    shutil.copy2(file_name + ext, file_name + count + ext)
    shutil.move(file_name + count + ext, file_name)
    print(file_name + count, "is copied.")
    copied_file_ck3.insert(0, file_name + count)


root_dir = "C:/Users/Administrator/Documents/Paradox Interactive/Crusader Kings III/save games"
os.chdir(root_dir)
# 초기 파일 검사
tmp_file_list = os.listdir(root_dir)
tmp_current_file_ck3 = [file for file in tmp_file_list if file.endswith(".ck3")]
print(tmp_current_file_ck3)
file_index = int(input("File number : "))
file_name = tmp_current_file_ck3[file_index].split(".")[0]
file_dir = "./" + file_name
ext = ".ck3"

if os.path.isdir(file_name):
    print("The folder", file_name, "is detected.")
else:
    os.makedirs(file_name, exist_ok=True)
    print("The folder", file_name, "is created.")

file_list = os.listdir(file_dir)
copied_file_ck3 = [file for file in file_list if file.endswith(ext)]
threading.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()
while keep_going:
    count = str(len(copied_file_ck3))
    if not copied_file_ck3:
        copy()
    else:
        if compare(file_name + '/' + copied_file_ck3[-1], file_name + ext) == 0:
            copy()
    time.sleep(300)
