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
    if any((
              password.isalnum(),
              password.isalpha(),
              password.isspace(),
              len(password) < 6,
              password in TOP_10_COMMON_PASSWORDS,
              )):
        return True


def isdigit_in_password(password):
    if any((char.isdigit() for char in password)):
        return True


def isalpha_in_password(password):
    if any((char.isalpha() for char in password)):
        return True


def isupper_in_password(password):
    if any((char.isupper() for char in password)):
        return True


def islower_in_password(password):
    if any((char.islower() for char in password)):
        return True


def isspecial_in_password(password):
    if any((char in string.punctuation for char in password)):
        return True


def calculate_password_strength(password):
    pswd_strn = 4
    if len(password) > 10:
        pswd_strn += 1
    if isdigit_in_password(password):
        pswd_strn += 1
    if isalpha_in_password(password):
        pswd_strn += 1
    if isupper_in_password(password):
        pswd_strn += 1
    if islower_in_password(password):
        pswd_strn += 1
    if isspecial_in_password(password):
        pswd_strn += 1
    return pswd_strn


def get_password_strength(password):
    if not password:
        return None
    if password_is_weak(password):
        return 1
    return calculate_password_strength(password)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        password = sys.argv[1]
        password_strength = get_password_strength(password)
        print('password_strength is {}'.format(password_strength))
    else:
        print('\nEnter: python3 password_strength.py "here is a password"\n')
