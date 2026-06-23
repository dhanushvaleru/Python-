def print_upper(ch):
    if ch > 'Z':
        return
    print(ch, end=" ")
    print_upper(chr(ord(ch)+1))
print_upper('A')