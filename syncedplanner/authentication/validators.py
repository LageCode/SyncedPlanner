from django.core import validators


PSWD_MIN_LENGTH = 8
PSWD_MAX_LENGTH = 32

PSWD_VALIDATORS = {
    'min_length': validators.MinLengthValidator(
        limit_value=PSWD_MIN_LENGTH,
        message=f'Password must contain at least {PSWD_MIN_LENGTH} characters.'
    ),
    'max_length': validators.MaxLengthValidator(
        limit_value=PSWD_MAX_LENGTH,
        message=f'Password must not exceed {PSWD_MAX_LENGTH} characters.'
    ),
    'has_lower_letter': validators.RegexValidator(
        regex=r'^(?=.*[a-z])',
        message=f'Password must contain at least one lowercase letter.'
    ),
    'has_upper_letter': validators.RegexValidator(
        regex=r'^(?=.*[A-Z])',
        message=f'Password must contain at least one uppercase letter.'
    ),
    'has_digit': validators.RegexValidator(
        regex=r'^(?=.*\d)',
        message=f'Password must contain at least one digit.'
    ),
    'has_symbol': validators.RegexValidator(
        regex=r'^(?=.*[!@#$%&])',
        message=f'Password must contain at least one symbol.'
    ),
    'allowed_char_only': validators.RegexValidator(
        regex=r'^[a-zA-Z\d]+$',
        message=f'Username must only contain lowercase and uppercase letters and digits.'
    )
}
