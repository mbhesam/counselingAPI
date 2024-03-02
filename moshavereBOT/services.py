# import os
# import sys
#
# sys.path.append('../moshavereAPI/')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moshavereAPI.settings")
from users.models import Users
from coreAPI.models import Questions, Answers
from moshavereBOT.common import (
    NO_ADVICE,
    ADVICE_CHOICE_CASE
)


def chek_information(username) -> bool:
    try:
        Users.objects.get(username=username)
        return True
    except Users.DoesNotExist:
        return False


# def get_subcategory(category_name):
#     try:
#         subcategory_objects = SubCategory.objects.filter(category__name=category_name)
#     except:
#         subcategory_objects = None
#     subcategories = []
#     for subcategory in subcategory_objects:
#         subcategories.append([subcategory.name])
#     return subcategories


def get_questions_name(question_id="all") -> list:
    question_names = []
    if question_id == "all":
        question_objs = Questions.objects.all()
    else:
        question_objs = Questions.objects.filter(id=question_id)
    for question_object in question_objs:
        question_names.append(question_object.name)
    
    return question_names


def get_question_text(question_id) -> str:
    return Questions.objects.get(id=question_id).original_question


def get_question_prefix(question_id) -> str:
    prefix = Questions.objects.get(id=question_id).prefix_question
    if prefix is None:
        raise ValueError()
    return prefix


def get_question_answers(question_id) -> list:
    answers = [answer for answer in Questions.objects.get(id=question_id).self_answers.all()]

