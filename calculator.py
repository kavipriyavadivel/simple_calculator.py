def sum(no1, no2, op):
    if op == '+':
        return no1 + no2
    elif op == '-':
        return no1 - no2
    elif op == '*':
        return no1 * no2
    else:
        return no1 / no2
def nxt_sum(n1,n2):
    print("Choose the Operation...")
    print("     +")
    print("     -")
    print("     *")
    print("     /")
    operation = input("Your operation is: ")
    res = sum(n1, n2, operation)
    print(res)
    game = input("Do you want to end game(y or n): ")
    if game == 'n':
        n2 = int(input("Enter another number: "))
        nxt_sum(res, n2)
    elif game == 'y':
        exit()
no1 = int(input("Enter the first number: "))
no2 = int(input("Enter the second number: "))
end = False
while not end:
    print("Choose the Operation...")
    print("     +")
    print("     -")
    print("     *")
    print("     /")
    operation = input("Your operation is: ")
    result = sum(no1, no2, operation)
    print(result)
    end_game = input("Do you want to end(y or n)").lower()
    if end_game == 'y':
        end = True
    elif end_game == 'n':
        no = int(input("Enter another number: "))
        nxt_sum(result, no)
