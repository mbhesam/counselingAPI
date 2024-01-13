from handlers import (
    start_handler,
    get_option_handler,
    get_health_field
)

from common import (
    BUTTON_HOME_PAGE,
    BUTTON_GET_MOSHAVERE_FIELDS,
    BUTTON_GET_HEALTH_FIELDS
)

from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)

STATES = {
    'option_choosing': 1,
    'song_choosing': 2,
    'not_allowed': 3,
}

main_handler = ConversationHandler(
    entry_points=[CommandHandler('شروع', start_handler)],
    states={
        STATES['option_choosing']: [
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
            MessageHandler(filters.Regex(f'^{BUTTON_GET_MOSHAVERE_FIELDS}$'), get_option_handler),
        ],
        STATES['not_allowed']: [
            MessageHandler(filters.Regex(f'.*'), start_handler),
        ],
        STATES['health_step_1']: [
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
            MessageHandler(filters.Regex(f'^{BUTTON_GET_HEALTH_FIELDS}$'), get_health_field),
        ],
        STATES['health_counseling_step_1']: [

        ],
        STATES['health_advices_step_1']: [
            CallbackQueryHandler(get_health_advice_field),
        ],
        STATES['choice_not_permitted']: [
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),

        ]
    },
    fallbacks=[],
    name='main_conversation',
    persistent=True,
)
