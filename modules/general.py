# Base import
import discord
from discord.ext import commands
import utility.discordembed as dmbd
import configparser
import json


# Module specific import
import random
from random import choice
from random import choice as randchoice

class General:
    """General commands."""

    def __init__(self, bot):
        self.bot = bot

# Say good night to user
    @commands.command(pass_context=True)
    async def gn(self, ctx, user : discord.Member=None):
    	msg = "Good Night" + "\n" + ":fist: :sweat_drops:"
    	author = user
    	em = dmbd.newembed(author, msg)
    	await self.bot.delete_message(ctx.message)
    	await self.bot.say(embed=em)

# Pierre Feuille Ciseaux
    @commands.command(pass_context = True)
    async def pfc(self, ctx, playerChoice):
    	rps = ["pierre", "feuille", "ciseaux"]
    	botChoice = random.choice(rps)
    	playerChoice = playerChoice.lower()
    	author = ctx.message.author
    	if botChoice == playerChoice:
    		msg = "Tu as dit " + playerChoice + " et j'ai dit " + botChoice + "\n" + "Égalité"
    	elif botChoice == "pierre" and playerChoice == "feuille":
    		msg = "Tu as dit :page_facing_up: et j'ai dit :moyai:." + "\n" + "Tu as gagné! J'ai perdu!"
    	elif botChoice == "pierre" and playerChoice == "ciseaux":
    		msg = "Tu as dit :scissors: et j'ai dit :moyai:." + "\n" + "J'ai gagné! Tu as perdu! haha"
    	elif botChoice == "feuille" and playerChoice == "pierre":
    		msg = "Tu as dit :moyai: et j'ai dit :page_facing_up:." + "\n" + "J'ai gagné! Tu as perdu! haha"
    	elif botChoice == "feuille" and playerChoice == "ciseaux":
    		msg = "Tu as dit :scissors: et j'ai dit :page_facing_up:." + "\n" + "Tu as gagné! J'ai perdu!"
    	elif botChoice == "ciseaux" and playerChoice == "feuille":
    		msg = "Tu as dit :page_facing_up: et j'ai dit :scissors:." + "\n" + "J'ai gagné! Tu as perdu! haha"
    	elif botChoice == "ciseaux" and playerChoice == "pierre":
    		msg = "Tu as dit :moyai: et j'ai dit :scissors:." + "\n" + "Tu as gagné! J'ai perdu!"
    	em = dmbd.newembed(author, msg)
    	await self.bot.delete_message(ctx.message)
    	await self.bot.say(embed=em)

# Lance un Dé
    @commands.command(pass_context = True)
    async def roll(self, ctx):
    	rolled = random.randint(1,6)
    	rolled = str(rolled)
    	msg = "Vous avez lancé un Dé !" + "\n" + "Il affiche " + rolled
    	author = ctx.message.author
    	em = dmbd.newembed(author, msg)
    	await self.bot.delete_message(ctx.message)
    	await self.bot.say(embed=em)

# Poop ou Face
    @commands.command(pass_context = True, aliases=['pof', 'toss'])
    async def PoF(self, ctx):
    	coin = [":poop:", ":full_moon_with_face: "]
    	msg = "C'est "
    	author = ctx.message.author
    	em = dmbd.newembed(author, msg + randchoice(coin))
    	await self.bot.delete_message(ctx.message)
    	await self.bot.say(embed=em)

# 8Ball
    @commands.command(pass_context=True, aliases=['8ball'])
    async def ball(self, ctx):
        """ Demandez à 8Ball """
        answers = ['Essaye plus tard', 'Essaye encore', "Pas d'avis",
				    'C\'est ton destin', 'Le sort en est jeté', 'Une chance sur deux',
				    'Repose ta question', 'D\'après moi oui', 'C\'est certain', 'Oui absolument',
				    'Tu peux compter dessus', 'Sans aucun doute', 'Très probable',
				    'Oui', 'C\'est bien parti', ':smirk:',
				    'C\'est non', 'Peu probable', 'Faut pas rêver',
				    'N\'y compte pas', 'Impossible']

        author = ctx.message.author
        em = dmbd.newembed(author, random.choice(answers))
        await self.bot.say(embed=em)

# Choose
    @commands.command(pass_context=True, description='Demandez au Bot d\'en choisir un')
    async def choose(self, ctx, *choices: str):
        """Choisit entre plusieurs choix."""
        author = ctx.message.author
        em = dmbd.newembed(author, 'Je choisis ' + random.choice(choices))
        await self.bot.say(embed=em)

# Random Face
    @commands.command(pass_context=True, name='face')
    async def face(self, ctx):
        """ Random face """
        faceanswers = ["( .-. )", "( .o.)", "( `·´ )", "( ° ͜ ʖ °)", "( ͡° ͜ʖ ͡°)", "( ⚆ _ ⚆ )", "( ︶︿︶)", "( ﾟヮﾟ)", "(\\/)(°,,,°)(\\/)", "(¬_¬)", "(¬º-°)¬", "(¬‿¬)", "(°ロ°)☝", "(´・ω・)っ", "(ó ì_í)", "(ʘᗩʘ')", "(ʘ‿ʘ)", "(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄", "(͡° ͜ʖ ͡°)", "ᕦ( ͡° ͜ʖ ͡°)ᕤ", "(ಠ_ಠ)", "(ಠ‿ಠ)", "(ಠ⌣ಠ)", "(ಥ_ಥ)", "(ಥ﹏ಥ)", "(ง ͠° ͟ل͜ ͡°)ง", "(ง ͡ʘ ͜ʖ ͡ʘ)ง", "(ง •̀_•́)ง", "(ง'̀-'́)ง", "(ง°ل͜°)ง", "(ง⌐□ل͜□)ง", "(ღ˘⌣˘ღ)", "(ᵔᴥᵔ)", "(•ω•)", "(•◡•)/", "(⊙ω⊙)", "(⌐■_■)", "(─‿‿─)", "(╯°□°）╯", "(◕‿◕)", "(☞ﾟ∀ﾟ)☞", "(❍ᴥ❍ʋ)", "(っ◕‿◕)っ", "(づ｡◕‿‿◕｡)づ", "(ノಠ益ಠ)ノ", "(ノ・∀・)ノ", "(；一_一)", "(｀◔ ω ◔´)", "(｡◕‿‿◕｡)", "(ﾉ◕ヮ◕)ﾉ", "=^.^=", "t(-.-t)", "| (• ◡•)|", "~(˘▾˘~)", "¬_¬", "¯(°_o)/¯", "¯\\_(ツ)_/¯", "°Д°", "ɳ༼ຈل͜ຈ༽ɲ", "ʅʕ•ᴥ•ʔʃ", "ʕ´•ᴥ•`ʔ", "ʕ•ᴥ•ʔ", "ʕ◉.◉ʔ", "ʕㅇ호ㅇʔ", "ʕ；•`ᴥ•´ʔ", "ʘ‿ʘ", "͡° ͜ʖ ͡°", "ζ༼Ɵ͆ل͜Ɵ͆༽ᶘ", "Ѱζ༼ᴼل͜ᴼ༽ᶘѰ", "ب_ب", "٩◔̯◔۶", "ಠ_ಠ", "ಠoಠ", "ಠ~ಠ", "ಠ‿ಠ", "ಠ⌣ಠ", "ಠ╭╮ಠ", "ರ_ರ", "ง ͠° ل͜ °)ง", "๏̯͡๏﴿", "༼ ºººººل͟ººººº ༽", "༼ ºل͟º ༽", "༼ ºل͟º༼", "༼ ºل͟º༽", "༼ ͡■ل͜ ͡■༽", "༼ つ ◕_◕ ༽つ", "༼ʘ̚ل͜ʘ̚༽", "ლ(´ڡ`ლ)", "ლ(́◉◞౪◟◉‵ლ)", "ლ(ಠ益ಠლ)", "ᄽὁȍ ̪őὀᄿ", "ᔑ•ﺪ͟͠•ᔐ", "ᕕ( ᐛ )ᕗ", "ᕙ(⇀‸↼‶)ᕗ", "ᕙ༼ຈل͜ຈ༽ᕗ", "ᶘ ᵒᴥᵒᶅ", "(ﾉಥ益ಥ）ﾉ", "≧☉_☉≦", "⊙▃⊙", "⊙﹏⊙", "┌( ಠ_ಠ)┘", "╚(ಠ_ಠ)=┐", "◉_◉", "◔ ⌣ ◔", "◔̯◔", "◕‿↼", "◕‿◕", "☉_☉", "☜(⌒▽⌒)☞", "☼.☼", "♥‿♥", "⚆ _ ⚆", "✌(-‿-)✌", "〆(・∀・＠)", "ノ( º _ ºノ)", "ノ( ゜-゜ノ)", "ヽ( ͝° ͜ʖ͡°)ﾉ", "ヽ(`Д´)ﾉ", "ヽ༼° ͟ل͜ ͡°༽ﾉ", "ヽ༼ʘ̚ل͜ʘ̚༽ﾉ", "ヽ༼ຈل͜ຈ༽ง", "ヽ༼ຈل͜ຈ༽ﾉ", "ヽ༼Ὸل͜ຈ༽ﾉ", "ヾ(⌐■_■)ノ", "꒰･◡･๑꒱", "﴾͡๏̯͡๏﴿", "｡◕‿◕｡", "ʕノ◔ϖ◔ʔノ", "(ノಠ益ಠ)ノ彡┻━┻", "(╯°□°）╯︵ ┻━┻", "꒰•̥̥̥̥̥̥̥ ﹏ •̥̥̥̥̥̥̥̥๑꒱", "ಠ_ರೃ", "(ू˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ू)", "(ꈨຶꎁꈨຶ)۶”", "(ꐦ°᷄д°᷅)", "(۶ૈ ۜ ᵒ̌▱๋ᵒ̌ )۶ૈ=͟͟͞͞ ⌨", "₍˄·͈༝·͈˄₎◞ ̑̑ෆ⃛", "(*ﾟ⚙͠ ∀ ⚙͠)ﾉ❣", "٩꒰･ัε･ั ꒱۶", "ヘ（。□°）ヘ", "˓˓(ृ　 ु ॑꒳’)ु(ृ’꒳ ॑ ृ　)ु˒˒˒", "꒰✘Д✘◍꒱", "૮( ᵒ̌ૢཪᵒ̌ૢ )ა", "“ψ(｀∇´)ψ", "ಠﭛಠ", "(๑>ᴗ<๑)", "(۶ꈨຶꎁꈨຶ )۶ʸᵉᵃʰᵎ", "٩(•̤̀ᵕ•̤́๑)ᵒᵏᵎᵎᵎᵎ", "(oT-T)尸", "(✌ﾟ∀ﾟ)☞", "ಥ‿ಥ", "ॱ॰⋆(˶ॢ‾᷄﹃‾᷅˵ॢ)", "┬┴┬┴┤  (ಠ├┬┴┬┴", "( ˘ ³˘)♥", "Σ (੭ु ຶਊ ຶ)੭ु⁾⁾", "(⑅ ॣ•͈ᴗ•͈ ॣ)", "ヾ(´￢｀)ﾉ", "(•̀o•́)ง", "(๑•॒̀ ູ॒•́๑)", "⚈้̤͡ ˌ̫̮ ⚈้̤͡", "=͟͟͞͞ =͟͟͞͞ ﾍ( ´Д`)ﾉ", "(((╹д╹;)))", "•̀.̫•́✧", "(ᵒ̤̑ ₀̑ ᵒ̤̑)", "\\_(ʘ_ʘ)_/", "乙(ツ)乙", "乙(のっの)乙", "ヾ(¯∇￣๑)", "\\_(ʘ_ʘ)_/", "༼;´༎ຶ ۝ ༎ຶ༽", "(▀̿Ĺ̯▀̿ ̿)", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)", "┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴", "┬┴┬┴┤(･_├┬┴┬┴", "(͡ ͡° ͜ つ ͡͡°)", "( ͡°╭͜ʖ╮͡° )", "(• ε •)", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]", "| (• ◡•)| (❍ᴥ❍ʋ)", "(◕‿◕✿)", "(╯°□°)╯︵ ʞooqǝɔɐɟ", "(☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)", "(づ￣ ³￣)づ", "(;´༎ຶД༎ຶ`)", "♪~ ᕕ(ᐛ)ᕗ", "༼ つ  ͡° ͜ʖ ͡° ༽つ", "༼ つ ಥ_ಥ ༽つ", "ಥ_ಥ", "( ͡ᵔ ͜ʖ ͡ᵔ )", "ヾ(⌐■_■)ノ♪", "~(˘▾˘~)", "\\ (•◡•) /", "(~˘▾˘)~", "(._.) ( l: ) ( .-. ) ( :l ) (._.)", "༼ ºل͟º ༼ ºل͟º ༼ ºل͟º ༽ ºل͟º ༽ ºل͟º ༽", "┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻", "ᕦ(ò_óˇ)ᕤ", "(•_•) ( •_•)>⌐■-■ (⌐■_■)", "(☞ຈل͜ຈ)☞", "˙ ͜ʟ˙", "☜(˚▽˚)☞", "(｡◕‿◕｡)", "（╯°□°）╯︵( .o.)", "(っ˘ڡ˘ς)", "┬──┬ ノ( ゜-゜ノ)", "ಠ⌣ಠ", "( ಠ ͜ʖರೃ)", "ƪ(˘⌣˘)ʃ", "¯\\(°_o)/¯", "ლ,ᔑ•ﺪ͟͠•ᔐ.ლ", "(´・ω・`)", "(´・ω・)っ由", "(° ͡ ͜ ͡ʖ ͡ °)", "Ƹ̵̡Ӝ̵̨̄Ʒ", "ಠ_ಥ", "ಠ‿↼", "(>ლ)", "(▰˘◡˘▰)", "(✿´‿`)", "◔ ⌣ ◔", "｡゜(｀Д´)゜｡", "┬─┬ノ( º _ ºノ)", "(ó ì_í)=óò=(ì_í ò)", "(/) (°,,°) (/)", "┬─┬ ︵ /(.□. ）", "^̮^", "(>人<)", "(~_^)", "(･.◤)", ">_>", "(^̮^)", "=U", "(｡╹ω╹｡)", "ლ(╹◡╹ლ)", "(●´⌓`●)", "（[∂]ω[∂]）", "U^ｴ^U", "(〒ó〒)", "(T^T)", "(íoì)", "(#•v•#)", "(•^u^•)", "!(^3^)!", "\\(°°\\”)", "(°o°:)", "(° o°)!", "(oﾛo)!!", "(òロó)", "(ò皿ó)", "(￣･_______･￣)", "ヾ(๑╹◡╹)ﾉ'", "(ლ╹◡╹)ლ", "（◞‸◟）", "(✿◖◡◗)", "(　´･‿･｀)", "(*｀益´*)がう", "(ヾﾉ'д'o)ﾅｨﾅｨ", "❤(◕‿◕✿)", "(◡‿◡*)❤", "(o'ω'o)", "(｡･ˇ_ˇ･｡)ﾑｩ…", "♬♩♫♪☻(●´∀｀●）☺♪♫♩♬", "(✿ฺ◕ฺ‿◕ฺ）ｳﾌｯ♥", "(つД⊂)ｴｰﾝ", "(つД・)ﾁﾗ", "(*´ω｀*)", "(✪‿✪)ノ", "╲(｡◕‿◕｡)╱", "ლ(^o^ლ)"]

        author = ctx.message.author
        em = dmbd.newembed(author, random.choice(faceanswers))
        await self.bot.say(embed=em)

def setup(bot):
    """Setup General.py"""
    bot.add_cog(General(bot))