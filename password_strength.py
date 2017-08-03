import sys
import string


TOP_10_COMMON_PASSWORDS = (
                            'Password1',
                            'Welcome1',
                            'P@ssword',
                            'Summer1!',
                            'password',
                            'Fa$hion1',
                            'Hello123',
                            'Welcome123',
                            'P@ssword1',
                           )


def get_password_strength(password):
    if not password:
        return None
    pswd_strn = 4
    if any((
              password.isalnum(),
              password.isalpha(),
              password.isspace(),
              len(password) < 6,
              password in TOP_10_COMMON_PASSWORDS,
              )):
        return 1
    if len(password) > 10:
        pswd_strn += 1
    if any((char.isdigit() for char in password)):
        pswd_strn += 1
    if any((char.isalpha() for char in password)):
        pswd_strn += 1
    if any((char.isupper() for char in password)):
        pswd_strn += 1
    if any((char.islower() for char in password)):
        pswd_strn += 1
    if any((char in string.punctuation for char in password)):
        pswd_strn += 1
    return pswd_strn


if __name__ == '__main__':
    if len(sys.argv) > 1:
        password = sys.argv[1]
        password_strength = get_password_strength(password)
        print('password_strength is {}'.format(password_strength))
    else:
        print('\nEnter: python3 password_strength.py "here is a password"\n')
