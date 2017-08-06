import getpass
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


def password_is_weak(password):
    return any((
              password.isalnum(),
              password.isalpha(),
              password.isspace(),
              len(password) < 6,
              password in TOP_10_COMMON_PASSWORDS,
              ))


def isdigit_in_password(password):
    return any((char.isdigit() for char in password))


def isalpha_in_password(password):
    return any((char.isalpha() for char in password))


def isupper_in_password(password):
    return any((char.isupper() for char in password))


def islower_in_password(password):
    return any((char.islower() for char in password))


def isspecial_in_password(password):
    return any((char in string.punctuation for char in password))


def islong_password(password):
    return len(password) > 10


def calculate_password_strength(password):
    return 4 + sum((
                    isdigit_in_password(password),
                    isalpha_in_password(password),
                    isupper_in_password(password),
                    islower_in_password(password),
                    isspecial_in_password(password),
                    islong_password(password),
                    ))


def get_password_strength(password):
    if password_is_weak(password):
        return 1
    return calculate_password_strength(password)


if __name__ == '__main__':
    print('Enter password to check its strength:')
    password = getpass.getpass()
    password_strength = get_password_strength(password)
    print('password_strength is {}'.format(password_strength))
