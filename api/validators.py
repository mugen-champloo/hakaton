from django.core.exceptions import ValidationError

def validate_password(password:str):
    if len(password) < 8:
        raise ValidationError("Пароль должен содержать как минимум 8 символов.")
    if password.isalpha() == True:
        raise ValidationError("Пароль должен содержать числа.")
    if password.isnumeric() == True:
        raise ValidationError("Пароль должен содержать буквы.")

def validate_phone_number(phone_number):
    if len(phone_number) < 10:
        raise ValidationError("Убедитесь в правилности номера телефона")