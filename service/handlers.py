import logging

from aiogram import Bot, Dispatcher, types

from config import Config
from parser import get_current_exchange_rate
from service.utils import DataHandler


bot = Bot(token=Config.TOKEN)
dp = Dispatcher(bot=bot)

data_handler = DataHandler()
logger = logging.getLogger("user_messages")


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    logger.info(data_handler.log_message(message))

    is_exist = data_handler.is_user_existent(message)

    if not is_exist:
        await message.answer(f"Привет {message.from_user.first_name}👋\nЧтобы узнать команды нажми /help")
    else:
        await message.answer(f"Привет еще раз {message.from_user.first_name}👋\nЧтобы узнать команды нажми /help")


@dp.message_handler(commands=["help", "refresh", "show"])
async def hello_bot(message: types.Message):
    logger.info(data_handler.log_message(message))

    data_handler.is_user_existent(message)

    if message.text.lower() == "/help":

        await message.answer(f"Команды:\n/help - все команды\n"
                             f"/show - посмотреть стоимость\n"
                             f"/refresh - обновить базу")

    elif message.text.lower() == "/refresh":

        await message.answer("База обновляется, пожалуйста подождите...🥶")

        get_current_exchange_rate(Config.URL)
        answer_message = data_handler.form_answer()

        await message.reply('\n'.join(answer_message))
    elif message.text.lower() == "/show":
        answer = data_handler.form_answer()

        await message.reply('\n'.join(answer))


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo(message: types.Message):
    data_handler.is_user_existent(message)
    photo = message.photo[-1].file_id
    await message.reply_photo(photo=photo)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def send_photo(message: types.Message):
    data_handler.is_user_existent(message)
    video = message.video.file_id
    await message.reply_video(video=video)


@dp.message_handler()
async def other_message(message: types.Message):
    logger.info(data_handler.log_message(message))
    data_handler.is_user_existent(message)
    await message.reply("Я вас не понимаю\nНажмите /help, что бы посмотреть доступные команды.🐒")
