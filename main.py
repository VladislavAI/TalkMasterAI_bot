import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '6118285335:AAEmnSBIPml24muQ4H9nVCDYAIBmRsRG44I'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"]
    )
    await message.answer(response['choices'][0]['text'])

bot.polling(none_stop=True, interval=0)
executor.start_polling(dp, skip_updates=True)
