import re

inp_count1 = int(input())
regex_list = []

for i in range(inp_count1):
    x = re.compile(input())
    regex_list.append(x)
inp_count2 = int(input())
str_list = []
for i in range(inp_count2):
    str_list.append(input())

for i in range(len(str_list)):

    for j in range(len(regex_list)):


        if re.match(regex_list[j], str_list[i]) is None and j == len(regex_list) - 1:
            print('NO, 0')
            break
        elif re.match(regex_list[j], str_list[i]) is not None:
            print('YES,', str(j + 1))
            break