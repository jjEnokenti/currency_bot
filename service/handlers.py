import logging
from aiogram import Bot, Dispatcher, types

from config import Config
from parser import get_current_exchange_rate
from service.utils import DataHandler
from implemented import user_service

bot = Bot(token=Config.TOKEN)
dp = Dispatcher(bot=bot)

data_handler = DataHandler()
logger = logging.getLogger("user_messages")


@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    logger.info(data_handler.log_message(message))

    is_exist_into_db = user_service. \
        get_one_by_id(message.from_user.id)

    if not is_exist_into_db:
        try:
            data = data_handler.form_data(message)
            new_user = user_service.create(data)
            await message.answer(f"Привет {new_user.first_name}👋\nЧтобы узнать команды нажми /help")
        except Exception as e:
            logger.error(e)
    else:
        await message.answer(f"Привет еще раз {is_exist_into_db.first_name}👋\nЧтобы узнать команды нажми /help")


@dp.message_handler(commands=["help", "refresh", "show"])
async def hello_bot(message: types.Message):
    logger.info(data_handler.log_message(message))
    is_exist_into_db = user_service. \
        get_one_by_id(message.from_user.id)
    if not is_exist_into_db:
        try:
            data = data_handler.form_data(message)
            user_service.create(data)
        except Exception as e:
            logger.error(e)

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


@dp.message_handler()
async def other_message(message: types.Message):
    logger.info(data_handler.log_message(message))

    await message.reply("Я вас не понимаю\nНажмите /help, что бы посмотреть доступные команды.🐒")
