import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('NTEyNjkyNTcwODMzMjg5MjQ2.W-24Kg.Ty_mIDV0cSPw7ykRKkAWS33-PUw')