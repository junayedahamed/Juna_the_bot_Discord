def sad_react():
       return '😢'


def happy_react():
    return '😍'

async def ract_all(message):
    await message.add_reaction('👍')
    await message.add_reaction('👎')
    await message.add_reaction('❤️')
    await message.add_reaction('🤣')
    await message.add_reaction('😢')
    await message.add_reaction('😡')