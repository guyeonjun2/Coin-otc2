import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} 로그인 완료")

@bot.command()
async def 재고입고(ctx, 금액: str):
    cleaned = 금액.replace(",", "")

    if not cleaned.isdigit():
        return await ctx.send("❌ 숫자만 입력해주세요.\n예: !재고입고 1000000")

    amount = int(cleaned)
    formatted = format(amount, ",") + "원"

    embed = discord.Embed(
        title="🪙 레제 코인대행 | 재고 입고",
        description="재고가 입고되었습니다!",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="💰 입고 금액",
        value=f"**{formatted}**",
        inline=False
    )

    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1476912108074434581/1477106440106676295/REZE_COIN_OTC.gif?ex=69a38e12&is=69a23c92&hm=8f75d18ba2cd903e18a33c87a9bec674494095ce1dd3b89258714e657605e33b&"
    )

    embed.set_footer(text="REZE OTC | 신속한 대행")

    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))
