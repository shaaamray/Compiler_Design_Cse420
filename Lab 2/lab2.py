fr = open('input.txt', 'r')

data = fr.read().splitlines()
n = int(data[0])
data = data[1:]

pos = 1
for i in data:
    end = i[-4:]
    if '@' in i and end == '.com' and '@gmail' in i:
        print("Email,",pos)

    if end == '.com' and '@' not in i and 'www' in i[0:4] and i[0] not in '1234567890':
        print("Web,",pos)

    pos += 1


fr.close()