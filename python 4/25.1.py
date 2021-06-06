import random
import string


def generate_password(m):
    def generate_symbol(prev=None):
        return random.choice(list(
            set(string.ascii_letters + string.digits)
            - {'l', 'I', '1', 'o', 'O', '0', prev}
        ))

    password = generate_symbol()
    for i in range(1, m):
        password += generate_symbol(password[i - 1])
    return password


def main(n, m):
    return [generate_password(m) for _ in range(n)]


print('Случайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15), sep='\n')
