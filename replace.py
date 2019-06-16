import os

path = os.chdir('/home/edgar757/Documents/Python/python-tutorial/dummy-files/')

for file in os.listdir(path):
    file_name, file_ext = os.path.splitext(file)
    f_num, f_dummy, f_file = file_name.split('-')
    f_dummy = f_dummy.strip()
    new_name = '{}-{}{}{}'.format(f_num, f_dummy, f_file, file_ext)
    os.replace(file, new_name)
    print('{}{}'.format(file_name, file_ext))



















# os.mkdir('dummy-files/')
# os.chdir('dummy-files/')

# file_name = 'dummy-file'
# file_ext = 'txt'

# for file_num in range(0,10):
#     with open('{} - {}.{}'.format(file_num, file_name, file_ext), 'w') as f:
#         f.write('Hello')   


