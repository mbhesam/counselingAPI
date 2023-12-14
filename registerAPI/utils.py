def revalidate_phone(phone_obj):
    phone_number = phone_obj["phone_number"]
    if phone_number.startswith("0") == False :
        return "WRONG_NUMBER"
    elif len(phone_number) != 11:
        return "CHAR_COUNT"
    else:
        return phone_number
def is_mobile(phone_number):
    return phone_number.startswith("09")