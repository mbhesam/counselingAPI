from users.models import Users
from coreAPI.models import Questions, Answers
from moshavereAPI.settings import redis_client


def check_information(username) -> bool:
    try:
        Users.objects.get(username=username)
        return True
    except Users.DoesNotExist:
        return False


def get_questions_name(question_id="all") -> list:
    question_names = []
    if question_id == "all":
        question_objs = Questions.objects.all()
    else:
        question_objs = Questions.objects.filter(id=question_id)
    for question_object in question_objs:
        question_names.append(question_object.name)

    return question_names


def get_question_prefix(question_id) -> str:
    prefix = Questions.objects.get(id=question_id).prefix_question
    if prefix is None:
        raise ValueError()
    return prefix


def get_question_text(question_id) -> str:
    return Questions.objects.get(id=question_id).original_question


def get_question_answers(question_id) -> list:
    answers = [answer for answer in Questions.objects.get(id=question_id).self_answers.all()]
    return answers


def get_next_question_id(answer, self_question_id) -> int:
    return Answers.objects.get(original_answer=answer, self_question_id=self_question_id).id


def get_state_id(user_name) -> int:
    return redis_client.get(user_name)


def set_state_id(user_name, state_id):
    redis_client.set(user_name, state_id)
