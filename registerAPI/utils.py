from melipayamak import Api
from moshavereAPI.settings import MELI_PAYAMAK_USERNAME, MELI_PAYAMAK_PASSWORD, MELI_PAYAMAK_MESSAGE, MELI_PAYAMAK_PATTERN_NUMBER

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

def send_sms(phone_number):
    api = Api(MELI_PAYAMAK_USERNAME, MELI_PAYAMAK_PASSWORD)
    sms_rest = api.sms()
    sms_rest.send_by_base_number(MELI_PAYAMAK_MESSAGE, phone_number, MELI_PAYAMAK_PATTERN_NUMBER)