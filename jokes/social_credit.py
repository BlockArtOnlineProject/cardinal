import disnake
import random
from disnake import ApplicationCommandInteraction as Aci
from disnake.ext import commands
import os

import config_manager as cfg

name = "socialcredit"
des = "Tín dụng xã hội. Ngoan thì sống."

banned = [
    "Thiên An Môn", "xe tăng", "biểu tình", "dân chủ", "Hồng Kông", "Biển Đông", "Đảo Điếu Ngư",
    "Vịt", "winnie the pooh", "tham nhũng", "Tân Cương", "Tây Tạng", "Giang Trạch Dân", "hai con",
    "diệt chủng", "John Cena"
                  "Tiannmen", "tank man", "protest", "democracy", "Hong Kong", "South China Sea", "Sogakukan",
    "ducks", "winnie the pooh", "coruption", "Xinjiang", "Tibet", "Zhiang Zemin", "John Cena",
    "two children", "genocide"
]


class SocialCredit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        img_path = os.path.join("jokes", "social_credit", f"rem-{random.randint(0, 4)}.png")
        content = message.content
        if cfg.read("social-credit-channel-ids").__contains__(message.channel.id):
            for entry in banned:
                if entry.upper() in content.upper():
                    await message.reply(file=disnake.File(img_path))

    @commands.slash_command(name=name, description=des)
    async def social_credit(self, interaction: Aci, member: disnake.Member):
        img_path = os.path.join("jokes", "social_credit", f"rem-{random.randint(0, 4)}.png")
        await interaction.response.send_message(f"{member.mention}, 哦艾弗伊艾哦哦艾弗伊艾哦哦艾弗伊艾哦!", file=disnake.File(img_path))


def setup(bot: commands.Bot):
    bot.add_cog(SocialCredit(bot))
