from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from random import randint

bot = Bot(token='5664115796:AAHIfzzVlzqGiiB9ECSj_ajQv2CCA-XQxp8')
dp = Dispatcher(bot)

keyboard1 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add("الصف الأول").add("💋 Youtube")


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("مرحبا 👋\n يرجى اختيار الصف.", reply_markup=keyboard1)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == "الصف الأول":
        await message.reply("Hi! How are you?")
    elif message.text == '💋 Youtube':
        await message.reply("https://youtube.com/gunthersuper")
    else:
        await message.reply(f"Your message is: {message.text}")


executor.start_polling(dp)
