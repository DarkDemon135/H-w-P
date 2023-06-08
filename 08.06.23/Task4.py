import os
import shutil
dir_path = r'C:\Users\User\Python\Other'
remove_dir = 'Files'
path = os.path.join(dir_path, remove_dir)
print(f'Содержимое директории {os.path.basename(dir_path)} до удаления каталога \
{remove_dir}: {os.listdir(dir_path)}\n')
shutil.rmtree(path)
print(f'Содержимое директории {os.path.basename(dir_path)} после удаления \
{remove_dir}: {os.listdir(dir_path)}\n')