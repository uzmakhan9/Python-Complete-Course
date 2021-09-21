SECURE = (('s', '$'),('and', '&'),('a', '@'),('o', '0'),('i', '1'),('I', '|'))

def securePassword(password):
    for a,b in SECURE:
        password=password.replace(a,b)
    return password

if __name__=="__main__":
    inp=input("Enter your password\n")
    password=securePassword(inp)
    print(f"Your secure password is {password}")