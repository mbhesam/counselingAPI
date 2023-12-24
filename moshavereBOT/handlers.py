from telegram import ReplyKeyboardMarkup, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)

from .common import (
MOSHAVERE_FIELDS,
MESSAGE_START_INTRO
)

STATES = {
    'option_choosing': 1,
    'song_choosing': 2,
    'not_allowed': 3,
}


def show_non_shown_songs_keyboard_markup():
    non_shown_songs = list(get_non_shown_songs())
    keyboard = BASE_KEYBOARD.copy()
    keyboard.extend([[f'{song.persian_singer_name}, {song.persian_song_name}'] for song in non_shown_songs])
    keyboard_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return keyboard_markup


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_existance = chek_information(username=update.effective_user.username)
        keyboard = [MOSHAVERE_FIELDS]
        keyboard_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
        await update.message.reply_text(MESSAGE_START_INTRO, reply_markup=keyboard_markup,
                                        parse_mode=ParseMode.MARKDOWN)
        return STATES['option_choosing']


async def get_songs_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard_markup = show_non_shown_songs_keyboard_markup()
    await update.message.reply_text(MESSAGE_SONG_CHOOSING, reply_markup=keyboard_markup, parse_mode=ParseMode.MARKDOWN)
    return STATES['song_choosing']


async def song_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update_text = update.message.text
    persian_singer_name, persian_song_name = update_text.split(', ')
    song = get_song_by_name(persian_singer_name, persian_song_name)
    song_info = MESSAGE_SONG_INFO.format(
        english_singer_name=song.english_singer_name,
        english_song_name=song.english_song_name,
        persian_singer_name=song.persian_singer_name,
        persian_song_name=song.persian_song_name,
        publish_date=song.publish_date,
        category=song.category,
        genre=song.genre,
        composer=song.composer,
        writer=song.writer,
        arranger=song.arranger,
        musician=song.musician,
    )
    keyboard = []
    similar_singers = search_similar_singers(song.persian_singer_name)
    for similar_singer in similar_singers:
        singer_id = similar_singer['id']
        singer_name = similar_singer['name']
        keyboard.append(
            [InlineKeyboardButton(f'{BUTTON_YES} {singer_name}', callback_data=f'ADD,{song.song_code},{singer_id}')]
        )
    additional_buttons = [
        [InlineKeyboardButton(f'{MESSAGE_INLINE_SONG_SAME_ARTIST} {BUTTON_YES}',
                              callback_data=f'ADD,{song.song_code},-1')],
        [InlineKeyboardButton(BUTTON_NO, callback_data=f'REJECT,{song.song_code},-1')],
    ]
    keyboard.extend(additional_buttons)
    await update.message.reply_photo(song.cover_path, song_info)
    if song.song_128_path:
        await update.message.reply_audio(song.song_128_path)
    if song.song_320_path:
        await update.message.reply_audio(song.song_320_path)
    await update.message.reply_text(MESSAGE_SONG_SHOULD_ADD, reply_markup=InlineKeyboardMarkup(keyboard))


async def song_should_add_button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    action, song_code, singer_id = query.data.split(',')
    selected_choice = BUTTON_YES if action == 'ADD' else BUTTON_NO

    await query.answer()
    await query.edit_message_text(
        text=MESSAGE_SONG_SHOULD_ADD_REPLY.format(selected_choice=selected_choice),
        reply_markup=None,
    )

    song = get_song_by_song_code(song_code)

    if action == 'REJECT':
        message = MESSAGE_REPLY_SONG_REJECT
        reject_song(song)
    else:
        message = MESSAGE_REPLY_SONG_SHOULD_ADD_ACK
        accept_song(song)

    keyboard_markup = show_non_shown_songs_keyboard_markup()
    await update.effective_user.send_message(message, reply_markup=keyboard_markup)

    if action == 'ADD':
        if singer_id == '-1':
            singer_id = add_singer(
                song.persian_singer_name,
                song.english_singer_name,
                song.singer_image_path,
                song.singer_biography,
            )
        song_file = song.song_320_path or song.song_128_path
        add_song_result = add_song(
            song.persian_song_name,
            song.english_song_name,
            song.cover_path,
            song.cover_path,
            song_file,
            singer_id,
            song.lyrics,
            song.composer,
            song.writer,
            song.arranger,
            song.musician,
            song.publish_date,
        )
        if add_song_result:
            added_song(song)
            await update.effective_user.send_message(MESSAGE_SONG_ADDED)
        else:
            await update.effective_user.send_message(MESSAGE_SONG_ERRORED)


main_handler = ConversationHandler(
    entry_points=[CommandHandler('شروع', start_handler)],
    states={
        STATES['option_choosing']: [
            MessageHandler(filters.Regex(f'^{BUTTON_GET_SONGS}$'), get_songs_handler),
            MessageHandler(filters.TEXT & (~filters.COMMAND), start_handler),
        ],
        STATES['not_allowed']: [
            MessageHandler(filters.Regex(f'.*'), start_handler),
        ],
        STATES['song_choosing']: [
            MessageHandler(filters.Regex(BUTTON_HOME_PAGE), start_handler),
            CallbackQueryHandler(song_should_add_button_handler),
            MessageHandler(filters.TEXT & (~filters.COMMAND), song_handler),
        ],
    },
    fallbacks=[],
    name='main_conversation',
    persistent=True,
)
