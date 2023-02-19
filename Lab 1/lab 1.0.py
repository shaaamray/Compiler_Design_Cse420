with open('input.txt') as input_test:
    lines = input_test.read().replace(',', ' ,').replace(';', ' ;')
input_test.close()

keywords = ["auto", "break", "case", "char", "const", "continue", "default",
            "do", "double", "else", "enum", "extern", "float", "for", "goto",
            "if", "int", "long", "register", "return", "short", "signed",
            "sizeof", "static", "struct", "switch", "typedef", "union",
            "unsigned", "void", "volatile", "while"]
oth = [',', ';', ')', '(', '{', '}', '[', ']']
maths = ['+', '-', '*', '/', '%', '=']
logics = ['>', '<', '!', '||']
id_key = ['int', 'float', 'double', 'long']

numerics = []
others = []
math_ops = []
logical_ops = []
identifiers = []
key = []

for i in lines.split():

    if i.isnumeric():
        if i not in numerics:
            numerics.append(i)
    elif i in oth:
        if i not in others:
            others.append(i)
    elif i in maths:
        if i not in math_ops:
            math_ops.append(i)
    elif i in logics:
        if i not in logical_ops:
            logical_ops.append(i)
    elif i in keywords:
        if i not in key:
            key.append(i)
    else:
        if i not in identifiers:
            identifiers.append(i)


output_text = open('output.txt', 'w')
output_text.write(f"Keywords: ")
output_text.write(", ".join(key))
output_text.write(f"\n")
output_text.write(f"Identifiers: ")
output_text.write(", ".join(identifiers))
output_text.write(f"\n")
output_text.write(f"Math Operators:")
output_text.write(", ".join(math_ops))
output_text.write(f"\n")
output_text.write(f"Logical Operators: ")
output_text.write(", ".join(logical_ops))
output_text.write(f"\n")
output_text.write(f"Numerical Values: ")
output_text.write(", ".join(numerics))
output_text.write(f"\n")
output_text.write(f"Others: ")
output_text.write(" ".join(others))

output_text.close()
input_test.close()
