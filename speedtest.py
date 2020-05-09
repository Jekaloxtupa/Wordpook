from vkbottle import Bot, Message
import time

@bot.on.message_handler(text='you command', lower=True)
async def speed_ans(ans: Message):
    timer = time.time()
    await ans('start')
    await ans(f'finish{(time.time()-timer)} sec.')
