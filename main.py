import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hola, soy un bot {client.user}!')
    elif message.content.startswith('$bottle'):
        await message.channel.send("Las botellas de plástico son un recurso que se tardan mucho en descomponerse. Te recomiendo evitar usarlas pero si no tienes de otra, puedes intentar lavar y reutilizar la botella.")
    elif message.content.startswith("$cardboard"):
        await message.channel.send("El cartón no se tarda mucho en descomponerse, pero igual puedes intentar hacer una manualidad para reutilizarlo siempre que puedas")
    elif message.content.startswith("$glass"):
        await message.channel.send("Una botella de vidrio se tarda mucho en descomponerse, lo mejor que puedes hacer es reutilizarla haciendo una maceta, o si te caben, almacenar cosas.")
    elif message.content.startswith("$aluminum"):
        await message.channel.send("Las latas de aluminio son otra cosa que se tarda en descomponerse en la naturaleza. Puedes intentar reutilizarlas para hacer masetas o un portalápices")

client.run("Coloca tu token aquí")