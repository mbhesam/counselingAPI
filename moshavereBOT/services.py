from users.models import Users
from coreAPI.models import Category, SubCategory, Advices
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
        subcategories.append(subcategory.name)
    return subcategories


def get_advices(category_name, subcategory_name):
    try:
        advices_objects = Advices.objects.filter(category__name=category_name, subcategory__name=subcategory_name)
    except:
        advices_objects = None
    advices = []
    for advice in advices_objects:
        advices.append(advice.content)
    return advices