from vkbottle import Bot, Message
import time

@bot.on.message_handler(text='you command', lower=True)
async def speed_ans(ans: Message):
    timer = time.time()
    await ans('you message')
    await ans(f'you message{(time.time()-timer)} sec.')
