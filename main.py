import logging, asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import API_TOKEN
from game.roles import ROLE_DESC
from game.modes import get_modes, assign_roles
from game.storage import (
    new_game, add_player, set_phase, set_role,
    get_players, get_game
)
from keyboards.inline import vote_keyboard

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message):
    chat = msg.chat.id
    modes = ", ".join(get_modes())
    await msg.reply(f"ربات Mafia Vahid آماده‌ست!\nحالت‌های بازی: {modes}\nبرای ساخت بازی /create <حالت>")

@dp.message_handler(lambda m: m.text.startswith('/create '))
async def cmd_create(msg: types.Message):
    chat, mode = msg.chat.id, msg.text.split(maxsplit=1)[1]
    if mode not in get_modes():
        return await msg.reply("حالت نامعتبر است.")
    new_game(chat, mode)
    await msg.reply(f"بازی ایجاد شد. حالت `{mode}` انتخاب شد.\nبرای پیوستن /join")

@dp.message_handler(commands=['join'])
async def cmd_join(msg: types.Message):
    chat, user = msg.chat.id, msg.from_user.full_name
    game = get_game(chat)
    if not game or game[1] != 'waiting':
        return await msg.reply("اول /create بزن.")
    add_player(chat, user)
    players = [u for u,_ in get_players(chat)]
    await msg.reply(f"{user} به بازی پیوست. تعداد: {len(players)}")

@dp.message_handler(commands=['play'])
async def cmd_play(msg: types.Message):
    chat = msg.chat.id
    game = get_game(chat)
    if not game or game[1] != 'waiting':
        return await msg.reply("نمی‌توان بازی را شروع کرد.")
    players = [u for u,_ in get_players(chat)]
    if len(players) < 4:
        return await msg.reply("حداقل ۴ نفر لازم است.")
    mode = game[0]
    roles = assign_roles(players, mode)
    for user, role in roles.items():
        set_role(chat, user, role)
        await bot.send_message(msg.chat.id, f"{user}: **{role}**\n{ROLE_DESC[role]}", parse_mode=types.ParseMode.MARKDOWN)
    set_phase(chat, 'night')
    await msg.reply("فاز شب آغاز شد. منتظر اکشن‌ها...")

@dp.callback_query_handler(lambda c: c.data.startswith('vote:'))
async def on_vote(call: types.CallbackQuery):
    target = call.data.split(':')[1]
    # مثال ساده: ثبت رأی در مموری (قابل توسعه)
    await call.answer(f"رأی شما برای {target} ثبت شد!")

@dp.message_handler(commands=['day'])
async def cmd_day(msg: types.Message):
    chat = msg.chat.id
    # نمونه‌ی ساده اعلام پایان شب و شروع روز
    set_phase(chat, 'day')
    names = [u for u,_ in get_players(chat)]
    kb = vote_keyboard(names)
    await msg.reply("فاز روز: برای اعدام رأی بدهید.", reply_markup=kb)

@dp.message_handler()
async def fallback(msg: types.Message):
    await msg.reply("دستور نامعتبر. از /create, /join, /play, /day استفاده کن.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)