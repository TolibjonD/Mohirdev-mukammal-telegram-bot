from aiogram import Bot, Dispatcher, types, executor
import wikipedia

wikipedia.set_lang("uz")

API_TOKEN = "6257596500:AAEzW4xP8sBRtCcQfQRcsFb10AaRuDp3ECY"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start", "help"])
async def get_welcome(msg: types.Message):
    await msg.answer(
        "Assalou aleykum wikipedia botga xush kelibsiz .\nMuallif: @TolibjonDev"
    )


@dp.message_handler()
async def get_wiki_data(msg: types.Message):
    res = wikipedia.summary(msg.text)
    await msg.answer(res)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
