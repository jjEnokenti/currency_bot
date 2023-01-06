
from config import Config
from aiogram import executor

from logger import create_logger
from parser import get_current_exchange_rate
from service.handlers import dp


def main():
    create_logger("user_messages")
    # get_current_exchange_rate(Config.URL)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
