from z3 import *

with open("text_out.txt", "rb") as f:
    encoded_ptr = f.read()
with open("text_in.txt", "rb") as f:
    input_text = f.read()
print("plain: ", input_text)
print("encoded: ", encoded_ptr)
print("size: ", len(input_text))

set_param('verbose', 10)

input_size = len(input_text)

table = [BitVec(f't[{i}]', 8) for i in range(64)]

#table_constraints = [And(0 <= table[i], table[i] < 256) for i in range(64)]

solver = Solver()
#solver.add(table_constraints)

cs = 0
itc = 0
while (input_size - itc) > 2:
    solver.add(encoded_ptr[cs] == table[input_text[itc] >> 2])
    solver.add(encoded_ptr[cs+1] == table[(input_text[itc+1] >> 4) | (16*input_text[itc]) & 0x30])
    solver.add(encoded_ptr[cs+2] == table[(input_text[itc+2] >> 6) | (4*input_text[itc+1]) & 0x3c])
    solver.add(encoded_ptr[cs+3] == table[input_text[itc+2] & 0x3F])
    itc += 3
    cs += 4

if input_size != itc:
    solver.add(encoded_ptr[cs] == table[input_text[itc] >> 2])
    if (input_size - itc) == 1:
        solver.add(encoded_ptr[cs+1] == table[(16 * input_text[itc]) & 0x30])
        solver.add(encoded_ptr[cs+2] == 61)
    else:
        solver.add(encoded_ptr[cs+1] == table[(input_text[itc+1] >> 4) | (16 * input_text[itc]) & 0x30])
        solver.add(encoded_ptr[cs+2] == table[(4 * input_text[itc+1]) & 0x3C])
    solver.add(encoded_ptr[cs+3] == 61)


print(solver.assertions())

if solver.check() == sat:
    model = solver.model()
    reconstructed_table = [model.eval(table[i], model_completion=True).as_long() for i in range(64)]
    print("Reconstructed Table: ", reconstructed_table)
    table = bytearray(reconstructed_table)

    print(table)
    with open('table.new', 'wb') as f:
        f.write(table)
else:
    print("No solution")

'''
def encode(input_text: bytes, input_size: int):
    encoded_size = ((4 * input_size // 3 + 4) // 0x48) + 4*input_size//3 + 4 + 1
    if encoded_size < input_size:
        return b""
    encoded_ptr = bytearray(encoded_size)
    cs = 0
    itc = 0
    while (input_size - itc) > 2:
        encoded_ptr[cs] = table[input_text[itc] >> 2]
        encoded_ptr[cs+1] = table[(input_text[itc+1] >> 4) | (16*input_text[itc]) & 0x30]
        encoded_ptr[cs+2] = table[(input_text[itc+2] >> 6) | (4*input_text[itc+1]) & 0x3c]
        encoded_ptr[cs+3] = table[input_text[itc+2] & 0x3F]
        itc += 3
        cs += 4

    if input_size != itc:
        encoded_ptr[cs] = table[input_text[itc] >> 2]
        if (input_size - itc) == 1:
            encoded_ptr[cs+1] = table[(16 * input_text[itc]) & 0x30]
            encoded_ptr[cs+2] = 61
        else:
            encoded_ptr[cs+1] = table[(input_text[itc+1] >> 4) | (16 * input_text[itc]) & 0x30]
            encoded_ptr[cs+2] = table[(4 * input_text[itc+1]) & 0x3C]
        encoded_ptr[cs+3] = 61

    return encoded_ptr

with open("text_in.txt", "rb") as f:
    a = f.read()

print(encode(a, len(a)))
'''    
