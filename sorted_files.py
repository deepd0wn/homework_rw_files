files = ('1.txt', '2.txt', '3.txt')
len_file = {}
data = {}

for file in files:
    try:
        with open(file, 'r', encoding='UTF-8') as f:
            len_file[file] = len(f.readlines())

    except FileNotFoundError:
        print(f"File {file} Not Found")

    with open(file, 'r', encoding='UTF-8') as f:
        data[file] = f.read()

with open('result.txt', 'a', encoding='UTF-8') as f:
    sorted_dict = dict(sorted(len_file.items(), key=lambda item: item[1]))

    for file_name, num_str in sorted_dict.items():
        f.write(file_name + '\n' + str(num_str) + '\n' + data[file_name] + '\n')

