input_file = open("test.txt", "r")
lines = input_file.readlines()

count = 0
while count < len(lines): 
    lines[count] = lines[count].replace('\n', '')
    count += 1


others = [',', ';', ')', '(', '{', '}', '[', ']']
maths = ['+', '-', '*', '/', '%', '=']
logics = ['>', '<', '!', '||']
id_key = ['int', 'float', 'double', 'long']
keywords = ["auto", "break", "case", "char", "const", "continue", "default",
            "do", "double", "else", "enum", "extern", "float", "for", "goto",
            "if", "int", "long", "register", "return", "short", "signed",
            "sizeof", "static", "struct", "switch", "typedef", "union",
            "unsigned", "void", "volatile", "while"]

ident = []
ident_final = []
key = []
neumerics = []
math = []
logic = []
oth = []
i = 0

while i < len(lines):
    lines[i] = lines[i].split(" ")
    i += 1
   


for j in range (len(lines)):
    varr= lines[j]
    if varr[0] in keywords :
        key.append(varr[0])
        if varr[0] in id_key :
            ident.append(varr[1:])

def find_identifiers(iden_arr) :
    for i in range(len(iden_arr)) :
        item_arr = iden_arr[i]
        for j in range(len(item_arr)) :
            item = item_arr[j]
            item= item.replace(';','').replace(',','')
            ident_final.append(item)
        
            


with open('test.txt') as f:
    lines = f.read().replace(',',' ,').replace(';',' ;')  

for line in lines.split():

   
    c=len(line)

    if(line.isnumeric()):
        if line not in neumerics:
            neumerics.append(line)
   
    elif (line[c-2:c-3:-1] == '.') :
        if line not in neumerics:
            neumerics.append(line)
    elif line in others:
        if line not in oth:
            oth.append(line)
            
    elif line in maths:
        if line not in math:
            math.append(line)
    elif line in logics:
        if line not in logic:
            logic.append(line)


out = open('output.txt', 'w')
out.write(f"Keywords: ")
for i in key:
    if i != key[-1]:
        out.write(f"{i},")
    else:
        out.write(f"{i}")
out.write('\n')


find_identifiers(ident)

out.write(f"Identifiers: ")
for i in ident_final:
    if i != ident_final[-1]:
        out.write(f"{i},")
    else:
        out.write(f"{i}")
out.write('\n')

out.write(f"Math Operators: ")
for i in math:
    if i != math[-1]:
        out.write(f"{i},")
    else:
        out.write(f"{i}")
out.write('\n')

out.write(f"Logical Operators: ")
for i in logic:
    out.write(f"{i}")
out.write('\n')

out.write(f"Numerical Values: ")
for i in neumerics:
    if i != neumerics[-1]:
        out.write(f"{i},")
    else:
        out.write(f"{i}")
out.write('\n')

out.write(f"Others: ")
for i in oth:
    out.write(f"{i} ")

out.close()
input_file.close()