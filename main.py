import discord
from currency_converter import convert_currency
from command import com_list
import qoute_jokes
from Reaction import react,lottary
from Key import token
import guess_game
from search_item import search_here
intents=discord.Intents.all()
client = discord.Client(intents=intents)

from weather import weather_details
@client.event
async def on_ready():
    print("Bot is ready!")
    print(client.user.name)

@client.event
async def on_message(message):


    if message.content.startswith("jtb hello"):

        await message.channel.send("Hello!")
    elif message.content.startswith("jtb"):
        # print(message.attachments)

        act_com = message.content[4:]
        print(act_com)


        if act_com.lower() in ["how are you?","how are you"]:
            await message.channel.send("I am good what about you?")

        elif act_com.lower() in ["i am fine", "i am also good"]:
            await message.add_reaction(react.happy_react())
            await message.channel.send("Great")

        elif act_com.lower() in ["i am sad", "i am not good","i am unhappy"]:
            await message.add_reaction(react.sad_react())
            await message.channel.send(f"Aww {message.author.mention} so sorry about that, can I share an inspiring quote for you?")

        elif act_com.lower() in ["yes","inspire"]:
            quote = qoute_jokes.get_qoute()
            await message.channel.send(quote)
        elif act_com.lower()=="no":
            await message.channel.send("Okay, let me know if you need anything else")

        elif act_com.lower()=="react":
            await react.ract_all(message)
        elif act_com[0:9].lower()=="ftw among":
            str=act_com
            str=str[10:]
            names=str.split(" ")
            w_name=lottary.who_is_winnner(names)
            await message.channel.send(f'Hurray winner is {w_name}\nCongratulation {w_name}')
        elif act_com=="jokes":
            await message.channel.send(qoute_jokes.get_jokes())

        elif act_com[:6]=="wtoday":
            city=act_com[7:]
            await message.channel.send(weather_details.get_weather(city))


    # -------------------------------------------------------------------------#
        elif act_com[:2].lower()=='lg': #jtb lg is for playing guess game with bot pact_com=>playing actual command
            print("here")
            pact_com=act_com[3:]
            if pact_com.lower() in ["play","start","begin"]:
                await message.channel.send("Ok then guess a number between 1 to 10")
            # elif type(pact_com) is not int :
            #     await message.channel.send("No sech command")
            elif pact_com:
                try:
                    val=int(pact_com)
                    result=guess_game.guess_right(val)
                    if result.lower()=="you won!!!":
                        await message.add_reaction(react.happy_react())
                    else:
                        await message.add_reaction(react.sad_react())
                    await message.channel.send(f'{message.author.mention} {result}')
                except:
                    await message.channel.send("Please enter a valid number or command for guess game")
        elif act_com[:2].lower()=='cc':
            fcurr=act_com[3:6]
            lcurr=act_com[10:13]
            amount = act_com[14:]
            try:
                amount=int(amount)
                await message.channel.send(convert_currency.converter(fcurr,lcurr,amount))
            except:
                await message.channel.send("Enter valid command")
    # wiki search pages --------------------------------------------------------#
        elif act_com[:3].lower()=='src':
            await message.channel.send("I am trying to answer you question.Please wait a while\n\n\n\n\n")
            src_itm=act_com[4:]
            items=search_here.search(src_itm)
            await message.channel.send(items[0])
            await message.channel.send(items[1])


    # command list get
        elif act_com=="help":
            await message.channel.send(com_list.commands())

client.run(token)



