from common import ADVICE_CHOICE_CASE


def create_message_to_send(messages):
    list_result = []
    for index, advice in enumerate(messages):
        list_result.append(ADVICE_CHOICE_CASE + f" {advice}")
    final_result = "\n".join(list_result)
    return final_result