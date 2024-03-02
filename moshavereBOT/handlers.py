from moshavereBOT.services import get_question_answers, chek_information, get_question_prefix, get_questions_name, get_question_text
from telegram import ReplyKeyboardMarkup, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode
import telegram.ext
from time import sleep
from moshavereBOT.utils import link_generator
from moshavereBOT.common import (
    MESSAGE_HEALTH_SUB_FIELD,
    MESSAGE_CHOICE_NOT_PERMITTED,
    MOSHAVERE_FIELDS,
    MESSAGE_START_INTRO,
    MESSAGE_NOT_PERMITTED_USER,
    MESSAGE_FIELD_CHOOSE,
    HEALTH_FIELDS,
    MESSAGE_HEALTH_FIELDS_CHOOSE,
    BUTTON_HOME_PAGE,
    BASE_KEYBOARD,
    MESSAGE_LINK_GENERATED
    )
from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    )
#
# STATES = {
#     'option_choosing': 1,
#     'song_choosing': 2,
#     'not_allowed': 3,
#     'health_step_1': 4,
#     'health_counseling_step_1': 5,
#     'health_advices_step_1': 6,
#     'choice_not_permitted': 7,
# }
STATES = {
    'option_choosing': 1,
}
questions = get_questions_name()
for index,question_id in enumerate(questions):
    STATES[question_id] = index + 2

STATES['not_allow'] = len(questions) + 1
#
# async def start_handler(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
#     user_existance = chek_information(username=update.effective_user.username)
#     if user_existance:
#         await update.message.reply_text(MESSAGE_START_INTRO)
#         keyboard = BASE_KEYBOARD.copy()
#         keyboard.extend([[f'{field}'] for field in MOSHAVERE_FIELDS])
#         keyboard_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
#         await update.message.reply_text(MESSAGE_FIELD_CHOOSE, reply_markup=keyboard_markup,
#                                         parse_mode=ParseMode.MARKDOWN)
#         return STATES['option_choosing']
#     else:
#         await update.message.reply_text(MESSAGE_NOT_PERMITTED_USER)
#         return STATES['not_allowed']


async def start_handler(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    user_existance = chek_information(username=update.effective_user.username)
    if user_existance:
        try:
            await update.message.reply_text(get_question_prefix(question_id=0))
        except ValueError:
            pass
        state_question = get_question_text(question_id=0)
        await update.message.reply_text(state_question)
        answers_choices = get_question_answers(question_id=0)
        keyboard = BASE_KEYBOARD.copy()
        keyboard.extend([[f'{field}'] for field in answers_choices])
        keyboard_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)


    else:
        return STATES['not_allow']


async def get_option_handler(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    choice = update.message.text
    if choice == MOSHAVERE_FIELDS[0]:
        keyboard = BASE_KEYBOARD.copy()
        keyboard.extend([[f'{field}'] for field in HEALTH_FIELDS])
        keyboard_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
        await update.message.reply_text(MESSAGE_HEALTH_FIELDS_CHOOSE, reply_markup=keyboard_markup,
                                        parse_mode=ParseMode.MARKDOWN_V2)
        return STATES['health_step_1']
    elif choice == MOSHAVERE_FIELDS[1]:
        return STATES['psychological_disorders_step_1']
    else:
        await update.message.reply_text(MESSAGE_CHOICE_NOT_PERMITTED)
        return STATES['option_choosing']


async def get_health_field(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    health_choice = update.message.text
    if health_choice == HEALTH_FIELDS[0]:
        return STATES['health_counseling_step_1']
    elif health_choice == HEALTH_FIELDS[1]:
        keyboard = BASE_KEYBOARD.copy()
        keyboard.extend(get_subcategory(category_name='طب_و_سلامت'))
        keyboard_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
        await update.message.reply_text(MESSAGE_HEALTH_SUB_FIELD, reply_markup=keyboard_markup,
                                        parse_mode=ParseMode.MARKDOWN_V2)
        return STATES['health_advices_step_1']
    else:
        await update.message.reply_text(MESSAGE_CHOICE_NOT_PERMITTED)
        return STATES['health_step_1']


async def get_health_advice_subcategory_field(update: Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    subcategory_name = update.message.text
    category = "طب_و_سلامت"
    link = link_generator(path=f'/core/advices/{category}/{subcategory_name}')
    await update.message.reply_text(MESSAGE_LINK_GENERATED)
    await update.message.reply_text(f'{link}')
    sleep(10)
    return STATES['option_choosing']

main_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start_handler)],
    states={
        STATES['option_choosing']: [
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
            MessageHandler(filters.TEXT & (~filters.COMMAND), get_option_handler),
        ],
        STATES['not_allowed']: [
            MessageHandler(filters.Regex(f'.*'), start_handler),
        ],
        STATES['health_step_1']: [
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
            MessageHandler(filters.TEXT & (~filters.COMMAND), get_health_field),
        ],
        STATES['health_counseling_step_1']: [
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
        ],
        STATES['health_advices_step_1']: [
            MessageHandler(filters.TEXT & (~filters.COMMAND), get_health_advice_subcategory_field),
        ],
        STATES['choice_not_permitted']: [
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
        ]
    },
    fallbacks=[],
    name='main_conversation',
    persistent=True,
)