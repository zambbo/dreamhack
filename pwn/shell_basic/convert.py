
string = '/home/shell_basic/flag_name_is_loooooong'

b32 = False
splitter = 8
if b32:
    splitter = 4

def main():
    tokens = [*string]
    print(len(string))

    print(tokens)
    tokens = [format(ord(token),'02x') for token in tokens]
    print(tokens)

    t_list = []
    for idx in range(len(tokens)-1, -1, -1):
        t_list.append(tokens[idx])

        if idx % splitter == 0:
            t_str = "".join(t_list)
            print(f"0x{t_str}")
            t_list = []

    if len(t_list) != 0:
        t_str = "".join(t_list)
        print(f"0x{t_str}")        

    



if __name__ == '__main__':
    main()