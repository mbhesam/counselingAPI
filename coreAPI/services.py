from coreAPI.models import Category, SubCategory, Advices
from moshavereBOT.common import (
    NO_ADVICE,
    ADVICE_CHOICE_CASE
)

def get_advices(category_name, subcategory_name):
    try:
        advices_objects = Advices.objects.filter(category__name=category_name, subcategory__name=subcategory_name)
    except:
        advices_objects = [NO_ADVICE]
    advices = []
    for advice in advices_objects:
        advices.append(ADVICE_CHOICE_CASE + advice.content)
    return advices
