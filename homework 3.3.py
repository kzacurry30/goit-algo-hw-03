import re


def normalize_phone(phone_number):

    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())


    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    elif cleaned_number.startswith('+') and not cleaned_number.startswith('+38'):

        cleaned_number = '+38' + cleaned_number.lstrip('+')

    return cleaned_number



print(normalize_phone("    +38(050)123-32-34"))  # +380501233234
print(normalize_phone("     0503451234"))  # +380503451234
print(normalize_phone("(050)8889900"))  # +380508889900
print(normalize_phone("38050-111-22-22"))  # +380501112222
print(normalize_phone("38050 111 22 11   "))  # +380501112211
