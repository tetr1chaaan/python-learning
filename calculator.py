ans = int(input("Enter the number:"))
while True:
    op = input("Choose the operation:")
    if op == 'NO':
            break
    val = input("Enter the number:")
    if val == 'NO':
        break
    x = int(val)
    if op == '+':
        ans = ans + x
    elif op == '-':
        ans = ans - x
    elif op == '*':
        ans = ans * x
    else:
        if x == 0:
            print("You can't divide to 0 please choose other operation and num")
            continue
        else:
            ans = ans // x
print(ans)