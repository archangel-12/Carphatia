import discord, wikipedia
from discord import Option

bot = discord.bot()

@bot.event
async def on_ready():
    print(f"Skyfall connect {bot.user}.")

testing = ['your guilds id']

@bot.slash_command(guild_ids=testing, name = 'summary', description='Returns a Wikipedia summary')
async def summary(ctx, search: Option(str, description="what kind of article you want me to summarize?", required = True)):
    await ctx.channel.trigger_typing()
    try: #tries to get a summary
        thesummary = wikipedia.summary(search, chars = 1950)
        try:
            await ctx.respond(thesummary)
        except:
            await ctx.send(thesummary)
    except:
        searchsummary = str(wikipedia.search(search, suggestion = True)).replace('(', '').replace(')', '').replace("'", "").replace('[', '').replace(']', '')
        try:
            await ctx.respond(f"I can't seem to find a summary for that.. Did you mean: {searchsummary}")
        except:
            await ctx.send(f"I can't seem to find a summary for that.. Did you mean: {searchsummary}")

@bot.slash_command(guild_ids = testing, name = 'search', description = "Search Wikipedia")
async def search(ctx, search: Option(str, description="What do you want to search for?", required = True)):
    await ctx.channel.trigger_typing() #shows that the bot is typing 
    searchsearch = str(wikipedia.search(search, suggestion = True)).replace('(', '').replace(')', '').replace("'", "").replace('[', '').replace(']', '')
    try:
        await ctx.respond(searchsearch)
    except:
        await ctx.send(searchsearch)

@bot.slash_command(guild_ids = testing, name = "url", description = "Get a URL to a page on Wikipedia")
async def url(ctx, search: Option(str, description="What do you want to get a URL for?", required = True)):
    await ctx.channel.trigger_typing()
    try:
        urlsummary = wikipedia.summary(search, auto_suggest = False)
        search = search.lower().replace(' ', '_').replace('  ', '_')
        try:
            await ctx.respond(f'https://en.wikipedia.org/wiki/{search}')
        except:
            await ctx.send(f'https://en.wikipedia.org/wiki/{search}')
    except:
        urlsearch = str(wikipedia.search(search, suggestion = True)).replace('(', '').replace(')', '').replace("'", "").replace('[', '').replace(']', '') 
        try:
            await ctx.respond(f"I can't find what you're talking about, did you mean: {urlsearch}")
        except:
            await ctx.send(f"I can't find what you're talking about, did you mean: {urlsearch}")

@bot.slash_command(guild_ids = testing, name = "random", description= "Returns a random Wikipedia article")
async def random(ctx):
    await ctx.channel.trigger_typing()
    randomtitle = wikipedia.random() #returns a title 
    randomsummary = wikipedia.summary(randomtitle, chars = 1950)
    link = randomtitle.replace(' ', '_')
    try:
        await ctx.respond(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")
    except:
        await ctx.send(f"**{randomtitle}** \n\n{randomsummary}\n\nhttps://en.wikipedia.org/wiki/{link}")

bot.run('token')