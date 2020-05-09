# Wordpook
version 2.1

# Text reverse

from vkbottle import Bot, Message

bot = Bot("token")

@bot.on.message_handler(text="command <text>", lower=True)
async def message_reverse(ans: Message, text)
  await ans(text[::-1]
  
# финиш бум)
