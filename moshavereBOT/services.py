# import os
# import sys
#
# sys.path.append('../moshavereAPI/')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moshavereAPI.settings")
from users.models import Users
from coreAPI.models import Category, SubCategory, Advices
from .common import (
    NO_ADVICE,
    ADVICE_CHOICE_CASE
)
def chek_information(username):
    try:
        Users.objects.get(username=username)
        return True
    except Users.DoesNotExist:
        return False


def get_subcategory(category_name):
    try:
        subcategory_objects = SubCategory.objects.filter(category__name=category_name)
    except:
        subcategory_objects = None
    subcategories = []
    for subcategory in subcategory_objects:
        subcategories.append([subcategory.name])
    return subcategories

