files = ('1.txt', '2.txt', '3.txt')

len_file = {}
for file in files:    
    with open(file, 'r', encoding='UTF-8') as f:
        len_file[file] = len(f.readlines())

with open('result.txt', 'a', encoding='UTF-8') as f:
    sorted_dict = dict(sorted(len_file.items(), key=lambda item: item[1]))
    for key, value in sorted_dict.items():
        f.write(key + '\n')
        f.write(str(value) + '\n')