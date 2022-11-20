from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN # Файл конфига не выкладываю, там токен
import os
import pyautogui
from time import sleep
import subprocess
from cmd_bot import kb, ReplyKeyboardMarkup, ReplyKeyboardRemove


bot = Bot(TOKEN)
dp = Dispatcher(bot)
# ADMIN = #Сюды свой ТГ ID пропиши, чтобы доступ к боту был только у тебя


####################
# КОМАНДА СТАРТ
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    if message.chat.id == ADMIN:
        await message.answer(f"\n🔐<b><u>---WELCOME TO THE REMOTE PC---</u></b>🔐\n"
                             f"\nDear <b>{message.from_user.first_name},</b>"
                             f"\n👇Тыкай меню", parse_mode='html', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer('NOT FOR U!')

# КОМАНДА ХЕЛП
@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    if message.chat.id == ADMIN:
        await message.answer(f"\n<u>---INFO ABOUT CMD---</u>\n"
                             f"\n<b>/start</b> - Тупо ради кнопки"
                             f"\n<b>/cmd</b> - Открыть команды(кнопки)\n"
                             f"\n<b><i>Список cmd(buttons):</i></b>\n"
                             f"\n<code>screen</code> - Сделать скрин экрана и прислать"
                             f"\n<code>open google</code> - Открыть Chrome"
                             f"\n<code>close google</code> - Закрыть Chrome"
                             f"\n<code>lockPC</code> - Залочить ПК"
                             f"\n<code>sleepPC</code> - Погрузить ПК в сон"
                             f"\n<code>sound-10</code> - Убавить звук на 10"
                             f"\n<code>sound+10</code> - Прибавить звук на 10"
                             f"\n<b>closekey - Закрыть клавиатуру</b>",
                             parse_mode='html')
    else:
        await message.answer('NOT FOR U!')

@dp.message_handler(commands=['cmd'])
async def commands(message: types.Message):
    await message.answer(f"Выбери, что необходимо сделать:", reply_markup=kb)

@dp.message_handler(content_types=['text'])
async def filter_text(message: types.Message):
    if message.chat.id == ADMIN:

    # ЗАКРЫТЬ ГУГЛ ХРОМ
        if message.text.lower() in ['close google', 'close goo', 'closegoogle']:
            await message.answer("Закрываю Гугл. . .")
            sleep(2)
            subprocess.run("powershell get-process chrome | "
                           "ForEach-Object { $_.CloseMainWindow() | Out-Null}")

    # ОТКРЫТЬ ГУГЛ ХРОМ
        elif message.text.lower() in ['open google', 'open goo', 'opengoogle']:
            await message.answer("Открываю Гугл. . .")
            sleep(2)
            os.system("start chrome")

    # СДЕЛАТЬ СКРИНШОТ И ПРИСЛАТЬ
        elif message.text.lower() == 'screen':
                await message.answer("Сейчас пришлю скрин экрана. . .")
                sleep(2)
                screen = pyautogui.screenshot(r"T:\screenshots\screenshot.png")
                photo = open(r"T:\screenshots\screenshot.png", "rb")
                await bot.send_photo(message.chat.id, photo, "done")

    # ЗАБЛОКИРОВАТЬ ПК
        elif message.text.lower() in ['lock', 'lockpc', 'lock_pc']:
            await message.answer("Блокирую ПК. . .")
            sleep(2)
            os.system('Rundll32.exe user32.dll,LockWorkStation')


    # ПОГРУЖЕНИЕ ПК В СОН
        elif message.text.lower() in ['sleep', 'sleeppc']:
            await message.answer("Пугружение в сон. . .")
            sleep(2)
            os.system("shutdown /h")

    # УПРАВЛЕНИЕ ЗВУКОМ с помощью стронней прилки 'cmdtools' - ссылку оставлю
        elif message.text.lower() == 'sound+10':
            await message.answer("Прибавляю звук на 10")
            await message.delete()
            sleep(1)
            os.system(fr"powershell c:\cmdtools\nircmd.exe changesysvolume 6555.5")
        elif message.text.lower() == 'sound-10':
            await message.answer("Убавляю звук на 10")
            await message.delete()
            sleep(1)
            os.system(r"powershell c:\cmdtools\nircmd.exe changesysvolume -6555.5")

        elif message.text.lower() == 'closekeyb':
            await message.answer('Закрываю клавиатуру.', reply_markup=ReplyKeyboardRemove())
            await message.delete()

        else:
            await message.answer('---ERROR COMMAND---')
    else:
        await message.answer("ТЫ КТО ТАКОЙ? ПРОВАЛИВАЙ")

        
