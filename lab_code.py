import os

folder = "files"

files = os.listdir(folder)

for file in files:
    old_path = os.path.join(folder, file)
    new_name = "new_" + file
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)

print("Файлы успешно переименованы")