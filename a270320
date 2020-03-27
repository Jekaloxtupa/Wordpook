@bot.on.message_handler(text='/скорость', lower=True)
async def speed_ans(ans: Message):
    timer = time.time()
    await ans('🕛 | Тест скорости начался...')
    await ans(f'🕥 | Скорость ответа составила {(time.time()-timer)} сек.')
