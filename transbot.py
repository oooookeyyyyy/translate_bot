from json import loads , dumps
from gtts import gTTS
import translators as ts
from telegram.inline.inlinequeryresultarticle import InlineQueryResultArticle
from telegram.ext import CommandHandler, Filters, InlineQueryHandler, MessageHandler, Updater, ConversationHandler, CallbackContext
from telegram.inline.inputtextmessagecontent import InputTextMessageContent
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update , InlineQueryResultVoice
from random import randint

updater = Updater("1600186727:AAEidfawzGdcCZWbjPZ_WbO-fxFpj1OPbHA")
dispatcher = updater.dispatcher
clients = loads(open('clients.json' , 'r').read())
users = loads(open('users.json' , 'r').read())
ADMIN = (768168527 , 1292941800)
LANGUAGE = 'en'
LANGUAGES = {'afrikaans': 'af','albanian': 'sq','amharic': 'am','arabic': 'ar','armenian': 'hy','azerbaijani': 'az',
    'basque': 'eu','belarusian': 'be','bengali': 'bn','bosnian': 'bs','bulgarian': 'bg','catalan': 'ca','cebuano': 'ceb',
    'chichewa': 'ny','chinese1': 'zh-cn','chinese2': 'zh-tw','corsican': 'co','croatian': 'hr',
    'czech': 'cs','danish': 'da','dutch': 'nl','english': 'en','esperanto': 'eo','estonian': 'et','filipino': 'tl',
    'finnish': 'fi','french': 'fr','frisian': 'fy','galician': 'gl','georgian': 'ka','german': 'de','greek': 'el',
    'gujarati': 'gu','haitian creole': 'ht','hausa': 'ha','hawaiian': 'haw','hebrew': 'iw','hebrew': 'he','hindi': 'hi',
    'hmong': 'hmn','hungarian': 'hu','icelandic': 'is','igbo': 'ig','indonesian': 'id','irish': 'ga','italian': 'it',
    'japanese': 'ja','javanese': 'jw','kannada': 'kn','kazakh': 'kk','khmer': 'km','korean': 'ko','kurdish': 'ku',
    'kyrgyz': 'ky','lao': 'lo','latin': 'la','latvian': 'lv','lithuanian': 'lt','luxembourgish': 'lb','macedonian': 'mk',
    'malagasy': 'mg','malay': 'ms','malayalam': 'ml','maltese': 'mt','maori': 'mi','marathi': 'mr','mongolian': 'mn',
    'myanmar': 'my','nepali': 'ne','norwegian': 'no','odia': 'or','pashto': 'ps','persian': 'fa','polish': 'pl',
    'portuguese': 'pt','punjabi': 'pa','romanian': 'ro','russian': 'ru','samoan': 'sm','scots gaelic': 'gd','serbian': 'sr',
    'sesotho': 'st','shona': 'sn','sindhi': 'sd','sinhala': 'si','slovak': 'sk','slovenian': 'sl','somali': 'so',
    'spanish': 'es','sundanese': 'su','swahili': 'sw','swedish': 'sv','tajik': 'tg','tamil': 'ta','telugu': 'te','thai': 'th',
    'turkish': 'tr','ukrainian': 'uk','urdu': 'ur','uyghur': 'ug','uzbek': 'uz','vietnamese': 'vi','welsh': 'cy','xhosa': 'xh',
    'yiddish': 'yi','yoruba': 'yo','zulu': 'zu'}
LANGUAGES2 = {'Afrikaans': 'af', 'Arabic': 'ar', 'Bengali': 'bn', 'Bosnian': 'bs', 'Catalan': 'ca', 'Czech': 'cs', 'Welsh': 'cy',
    'Danish': 'da', 'German': 'de', 'Greek': 'el', 'English': 'en', 'Esperanto': 'eo', 'Spanish': 'es', 'Estonian': 'et',
    'Finnish': 'fi', 'French': 'fr', 'Gujarati': 'gu', 'Hindi': 'hi','Croatian': 'hr', 'Hungarian': 'hu', 'Armenian': 'hy',
    'Indonesian': 'id', 'Icelandic': 'is','Italian': 'it', 'Japanese': 'ja', 'Javanese': 'jw', 'Khmer': 'km', 'Kannada': 'kn',
    'Korean': 'ko','Latin': 'la', 'Latvian': 'lv', 'Macedonian': 'mk', 'Malayalam': 'ml', 'Marathi': 'mr', 'Myanmar': 'my',
    'Nepali': 'ne', 'Dutch': 'nl', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt', 'Romanian': 'ro', 'Russian': 'ru',
    'Sinhala': 'si', 'Slovak': 'sk','Albanian': 'sq', 'Serbian': 'sr', 'Sundanese': 'su', 'Swedish': 'sv', 'Swahili': 'sw',
    'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 'Filipino': 'tl', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Urdu': 'ur',
    'Vietnamese': 'vi', 'Chinese1': 'zh-cn', 'Chinese2': 'zh-tw'}


def start(update : Update, context : CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id , text="Hi there ! your language sets on english\nyou can change it by using /language command",reply_markup=ReplyKeyboardRemove())
    clients[str(update.effective_chat.id)] = 'en'
    file = open('clients.json' , 'w')
    file.write(dumps(clients))
    file.close()
    users[str(update.effective_chat.id)] = update.message.from_user.username
    file = open('users.json' , 'w')
    file.write(dumps(users))
    file.close()


def language(update : Update, context : CallbackContext) :
    reply_keyboard = [['afrikaans','albanian','amharic', 'arabic'], ['armenian', 'azerbaijani', 'basque', 'belarusian'], 
    ['bengali', 'bosnian', 'bulgarian', 'catalan'], ['cebuano', 'chichewa', 'chinese1', 'chinese2' ], 
    ['corsican', 'croatian', 'czech', 'danish'], ['corsican', 'croatian', 'czech', 'danish'], 
    ['dutch', 'english', 'esperanto', 'estonian'], ['filipino', 'finnish', 'french', 'frisian'],
    ['galician', 'georgian', 'german', 'greek'], ['gujarati', 'haitian creole', 'hausa', 'hawaiian'],
    ['hebrew', 'hebrew', 'hindi', 'hmong'], ['hungarian', 'icelandic', 'igbo', 'indonesian'],
    ['irish', 'italian', 'japanese', 'javanese'], ['kannada', 'kazakh', 'khmer', 'korean'],
    ['kurdish', 'kyrgyz', 'lao', 'latin'], ['latvian', 'lithuanian', 'luxembourgish', 'macedonian'],
    ['malagasy', 'malay', 'malayalam', 'maltese'], ['maori', 'marathi', 'mongolian', 'myanmar'],
    ['nepali', 'norwegian', 'odia', 'pashto'], ['persian', 'polish', 'portuguese', 'punjabi'], 
    ['romanian', 'russian', 'samoan', 'scots gaelic'], ['serbian', 'sesotho', 'shona', 'sindhi'],
    ['sinhala', 'slovak', 'slovenian', 'somali'], ['spanish', 'sundanese', 'swahili', 'swedish'],
    ['tajik', 'tamil', 'telugu', 'thai'], ['turkish', 'ukrainian', 'urdu', 'uyghur'], 
    ['uzbek', 'vietnamese', 'welsh', 'xhosa'], ['yiddish', 'yoruba', 'zulu']]
    context.bot.send_message(chat_id=update.effective_chat.id , text = 'choose from this languages :' , reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return 1


def change(update : Update, context : CallbackContext) :
    global LANGUAGE
    if update.message.text in LANGUAGES.keys() :
        LANGUAGE = LANGUAGES.get(update.message.text)
        context.bot.send_message(chat_id=update.effective_chat.id, text='ok ... now send /done to end the language change operation \nor reselect language ')
    else :
        context.bot.send_message(chat_id=update.effective_chat.id, text='ERROR :) \nselect a correct language !')


def done(update : Update, context : CallbackContext) :
    global LANGUAGE
    clients[str(update.effective_chat.id)] = LANGUAGE
    file = open('clients.json' , 'w')
    file.write(dumps(clients))
    file.close()
    context.bot.send_message(chat_id=update.effective_chat.id, text='language sets on '+clients.get(str(update.effective_chat.id)) ,reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def translate(update : Update, context : CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=ts.google(update.message.text , to_language=clients.get(str(update.effective_chat.id))))


def speech(update : Update, context : CallbackContext):
    if update.message.reply_to_message :
        if clients.get(str(update.effective_chat.id)) in LANGUAGES2.values() :
            name = str(randint(0,1000))
            gTTS(text=update.message.reply_to_message.text , lang=clients.get(str(update.effective_chat.id)) , lang_check=False ).save(name)
            context.bot.send_audio(chat_id=update.effective_chat.id , audio=open(name , 'rb'))
        else :
            context.bot.send_message(chat_id=update.effective_chat.id , text= clients.get(str(update.effective_chat.id))+' is not supported for speech')
    else :
        context.bot.send_message(chat_id=update.effective_chat.id , text= 'must use by replying a message')


def ad(update : Update, context : CallbackContext):
    if update.effective_chat.id in ADMIN :
        context.bot.send_message(chat_id=update.effective_chat.id , text='users : '+str(len(users)))
        for user in users :
            context.bot.forward_message(chat_id=user , from_chat_id=update.effective_chat.id , message_id=update.message.reply_to_message.message_id)


def inline_translate(update : Update, context : CallbackContext):
    global LANGUAGE
    query = update.inline_query.query
    LANGUAGE = clients.get(str(update.inline_query.from_user.id))
    if not query:
        return
    name = str(randint(0,1000))
    results = [ InlineQueryResultArticle(id=1,title='text',input_message_content=InputTextMessageContent(query+' : '+ts.google(query , to_language=LANGUAGE))) ,
				InlineQueryResultVoice(id=2,voice_url=name,title='speech',caption=query)]
    gTTS(text=query,lang=clients.get(str(update.inline_query.from_user.id)),lang_check=False).save(name)
    context.bot.answer_inline_query(update.inline_query.id, results)


dispatcher.add_handler(CommandHandler('start' , start))
dispatcher.add_handler(ConversationHandler(
    entry_points=[CommandHandler('language', language)],
    states={1: [MessageHandler(Filters.text & (~Filters.command), change)]},
    fallbacks=[CommandHandler('done' , done)]))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), translate))
dispatcher.add_handler(CommandHandler('speech' , speech))
dispatcher.add_handler(CommandHandler('ad' , ad))
dispatcher.add_handler(InlineQueryHandler(inline_translate))
updater.start_polling()
updater.idle()