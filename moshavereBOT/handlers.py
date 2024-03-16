from moshavereBOT.services import get_question_answers, check_information, get_question_prefix, \
    get_questions_name, get_question_text, get_next_question_id, get_state_id, set_state_id, is_this_end, \
    get_first_question_id
from telegram import ReplyKeyboardMarkup, Update
from telegram.constants import ParseMode
from moshavereBOT.common import (
    BUTTON_HOME_PAGE,
    BASE_KEYBOARD,
    MESSAGE_NOT_PERMITTED_USER,
    START_BUTTON,
    )
from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters, ContextTypes,
)

from moshavereBOT.utils import link_generator

STATES = {
    'option_choosing': -1,
}
questions = get_questions_name()
for index, name in enumerate(questions):
    STATES[name] = index

STATES['end'] = len(questions)
STATES['not_allowed'] = len(questions) + 1

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_question_id = get_first_question_id()
    user_existence = check_information(username=update.effective_user.username)
    if not user_existence:
        await update.message.reply_text(MESSAGE_NOT_PERMITTED_USER)
        link = link_generator(f"/users/registerinformation/telegram/{update.effective_user.username}")
        await update.message.reply_text(link)
        return STATES['not_allowed']
    try:
        await update.message.reply_text(get_question_prefix(question_id=first_question_id))
    except ValueError:
        pass
    question_text = get_question_text(question_id=first_question_id)
    question_name: str = get_questions_name(question_id=first_question_id)[0]
    answers_choices = get_question_answers(question_id=first_question_id)
    keyboard = BASE_KEYBOARD.copy()
    keyboard.extend([[f'{field}'] for field in answers_choices])
    keyboard_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(question_text, reply_markup=keyboard_markup, parse_mode=ParseMode.MARKDOWN)
    set_state_id(user_name=update.effective_user.username, state_id=first_question_id)
    return STATES[question_name]


async def switch_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = update.message.text
    state_id = get_state_id(user_name=update.effective_user.username)
    try:
        next_question_id = get_next_question_id(answer=answer, self_question_id=state_id)
        try:
            await update.message.reply_text(get_question_prefix(question_id=next_question_id))
        except ValueError:
            pass
        question_text = get_question_text(question_id=next_question_id)
        if is_this_end(id=next_question_id):
            keyboard = BASE_KEYBOARD.copy()
            keyboard_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
            await update.message.reply_text(question_text, reply_markup=keyboard_markup)
            set_state_id(user_name=update.effective_user.username, state_id=get_first_question_id())
            return STATES['end']
        question_name: str = get_questions_name(question_id=next_question_id)[0]
        answers_choices = get_question_answers(question_id=next_question_id)
        keyboard = BASE_KEYBOARD.copy()
        keyboard.extend([[f'{field}'] for field in answers_choices])
        keyboard_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        await update.message.reply_text(question_text, reply_markup=keyboard_markup, parse_mode=ParseMode.MARKDOWN)
        set_state_id(user_name=update.effective_user.username, state_id=next_question_id)
        return STATES[question_name]
    except ValueError:
        return STATES['not_allowed']


state_definition = {}
for index, name in enumerate(questions):
    state_definition[STATES[name]] = [
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
            MessageHandler(filters.TEXT & (~filters.COMMAND), switch_handler),
            MessageHandler(filters.Regex(START_BUTTON), start_handler),
        ]
state_definition[STATES['end']] = [
    MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
    MessageHandler(filters.Regex(START_BUTTON), start_handler),
]
state_definition[STATES['not_allowed']] = [
    MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
    MessageHandler(filters.Regex(START_BUTTON), start_handler),
]

main_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_handler)],
    states=state_definition,
    fallbacks=[],
    name='main_conversation',
    persistent=True,
)
