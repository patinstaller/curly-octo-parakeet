# --- Данный код является публичным и может использоваться третьими лицами в своих целях ---
# < Данный код не платный. Если вы его купили - лохи) >
# < Создатель: Иван Шаповалов >
# < Лицензия: MIT >
# < Описание: Бот (Wheel) для VK, написанный на vk_api и использующий асинхронность для подведения итогов. >
# < Тематика: Виртуальный азарт на виртуальную валюту >
#
# </ Ссылки на создателя:
# VK: https://vk.com/yprak
# />

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from random import randint, choice, choices, sample
from json import dump
from DataBase import user, games, promocodes, bonus, glob
from keyboards import *
from datetime import datetime
from hashlib import md5
from config import groupToken, groupId, adminIds
import time, asyncio, threading, string


class BotLongPoll(VkBotLongPoll):

  def listen(self):
    while True:
      try:
        for event in self.check():
          yield event
      except Exception as e:
        print(e)

vk_session = VkApi(token=groupToken)
lp = BotLongPoll(vk_session, groupId)
vk_session = vk_session.get_api()
botstart = int(time.time())


def randid():
  return randint(-2000000000, 2000000000)


def idsplit(text, tipe="default"):
  us_id = text.split(" ")[1]
  if tipe == "default":
    try:
      us_id = int(us_id)
    except:
      try:
        us_id = us_id.split("vk.com/")[1]
        us_id = vk.users.get(us_id)['id']
      except:
        try:
          us_id = text.split("@")[1]
          us_id = us_id.split("]")[0]
          us_id = vk.users.get(us_id)['id']
        except Exception as err:
          print(err)
          pass
  return us_id


def postidsplit(text):
  post_id = text.split(" ")[1]
  try:
    post_id = int(post_id)
  except:
    try:
      post_id = (text.split("_")[1]).split(" ")[0]
    except Exception as err:
      print(err)
      pass
  return post_id


def getrandkey(klen):
  return ''.join(sample(string.ascii_letters + string.digits, klen))


class vk:

  def send(message,
           peer_id=None,
           attachment=None,
           keyboard=None,
           peer_ids=None):
    if not peer_ids:
      vk_session.messages.send(peer_id=peer_id,
                               message=message,
                               attachment=attachment,
                               keyboard=keyboard,
                               random_id=randid())
    else:
      vk_session.messages.send(peer_ids=peer_ids,
                               message=message,
                               attachment=attachment,
                               keyboard=keyboard,
                               random_id=randid())

  class users:

    def get(user_id):
      return vk_session.users.get(user_ids=user_id)[0]

  class utils:

    def getShortLink(url):
      return vk_session.utils.get_short_link(url=url)


games.create()
user.create()
promocodes.create()
bonus.create()
glob.create()
if len(glob.get()) <= 0:
  glob.add()

numbers_one = list(range(1, 13))
numbers_two = list(range(13, 25))
numbers_three = list(range(25, 37))
numbers = list(range(0, 37))
strnumbers = list(map(str, numbers))

colors = ['черный', "красный"]
num_intervals = ['1-12', '13-24', '25-36']
ends = 60
ends_two = ends - 5

sectors = [{
  "number": 0,
  "color": "зеленый",
  "img": "photo-220673195_457239060"
}, {
  "number": 1,
  "color": "красный",
  "img": "photo-220673195_457239061"
}, {
  "number": 2,
  "color": "черный",
  "img": "photo-220673195_457239062"
}, {
  "number": 3,
  "color": "красный",
  "img": "photo-220673195_457239063"
}, {
  "number": 4,
  "color": "черный",
  "img": "photo-220673195_457239064"
}, {
  "number": 5,
  "color": "красный",
  "img": "photo-220673195_457239065"
}, {
  "number": 6,
  "color": "черный",
  "img": "photo-220673195_457239066"
}, {
  "number": 7,
  "color": "красный",
  "img": "photo-220673195_457239067"
}, {
  "number": 8,
  "color": "черный",
  "img": "photo-220673195_457239068"
}, {
  "number": 9,
  "color": "красный",
  "img": "photo-220673195_457239069"
}, {
  "number": 10,
  "color": "черный",
  "img": "photo-220673195_457239070"
}, {
  "number": 11,
  "color": "черный",
  "img": "photo-220673195_457239071"
}, {
  "number": 12,
  "color": "красный",
  "img": "photo-220673195_457239072"
}, {
  "number": 13,
  "color": "черный",
  "img": "photo-220673195_457239073"
}, {
  "number": 14,
  "color": "красный",
  "img": "photo-220673195_457239074"
}, {
  "number": 15,
  "color": "черный",
  "img": "photo-220673195_457239075"
}, {
  "number": 16,
  "color": "красный",
  "img": "photo-220673195_457239076"
}, {
  "number": 17,
  "color": "черный",
  "img": "photo-220673195_457239077"
}, {
  "number": 18,
  "color": "красный",
  "img": "photo-220673195_457239078"
}, {
  "number": 19,
  "color": "красный",
  "img": "photo-220673195_457239079"
}, {
  "number": 20,
  "color": "черный",
  "img": "photo-220673195_457239080"
}, {
  "number": 21,
  "color": "красный",
  "img": "photo-220673195_457239081"
}, {
  "number": 22,
  "color": "черный",
  "img": "photo-220673195_457239082"
}, {
  "number": 23,
  "color": "красный",
  "img": "photo-220673195_457239083"
}, {
  "number": 24,
  "color": "черный",
  "img": "photo-220673195_457239084"
}, {
  "number": 25,
  "color": "красный",
  "img": "photo-220673195_457239085"
}, {
  "number": 26,
  "color": "черный",
  "img": "photo-220673195_457239086"
}, {
  "number": 27,
  "color": "красный",
  "img": "photo-220673195_457239087"
}, {
  "number": 28,
  "color": "черный",
  "img": "photo-220673195_457239088"
}, {
  "number": 29,
  "color": "черный",
  "img": "photo-220673195_457239089"
}, {
  "number": 30,
  "color": "красный",
  "img": "photo-220673195_457239090"
}, {
  "number": 31,
  "color": "черный",
  "img": "photo-220673195_457239091"
}, {
  "number": 32,
  "color": "красный",
  "img": "photo-220673195_457239092"
}, {
  "number": 33,
  "color": "черный",
  "img": "photo-220673195_457239093"
}, {
  "number": 34,
  "color": "красный",
  "img": "photo-220673195_457239094"
}, {
  "number": 35,
  "color": "черный",
  "img": "photo-220673195_457239095"
}, {
  "number": 36,
  "color": "красный",
  "img": "photo-220673195_457239096"
}]

official_chats = [1, 2, 3, 4]
verify_chats = []
admin_ids = adminIds
per_click = 100
# 644686917

emoji_top = ["🥇", "🥈", "🥉", "🏅", "🏅", "🏅", "🏅", "🏅", "🏅", "🏅"]
today_prize = 500000
today_wins = [35, 24, 12, 8, 6, 5, 4, 3, 2, 1]

week_wins = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def top_start(p, u, n, v, d=True):
  threading.Thread(target=top_start2, args=(
    p,
    u,
    n,
    v,
    d,
  )).start()


def top_start2(p, u, n, v, d=True):
  asyncio.run(top(
    p,
    u,
    n,
    v,
    d,
  ))


async def top(peer_id, user_id, name, var, day=True):
  if day:
    top = user.top(var)
    text = ""
    text2 = ""
    num = 0
    for a, i in enumerate(top):
      if a <= 9:
        num += 1
        winprize = int(today_prize / 100 * today_wins[a])
        text += f"{emoji_top[a]} {a+1}. {i[0]} - {formarter(i[3])} SC (Приз: {formarter(winprize)} SC)\n"
      else:
        break
    if num < 2:
      text2 = "\n\n(Для подведения итогов необходимо как минимум 2 игрока в топе)"
    vk.send(
      peer_id=peer_id,
      message=
      f"🔥 Ежедневный рейтинг игроков на {formarter(today_prize)} SC:\n\n{text}\n\n{name}, вы выиграли: {formarter(user.get(user_id, 'sc_wins_day'))} SC{text2}"
    )
  else:
    top = user.top(var)
    text = ""
    for a, i in enumerate(top):
      if a <= 9:
        text += f"{emoji_top[a]} {a+1}. {i[0]} - {formarter(i[3])} SC (Приз: {formarter(week_wins[a])} SC)\n"
      else:
        break
    vk.send(
      peer_id=peer_id,
      message=
      f"🔥 Еженедельный рейтинг игроков на XXXкк SC:\n\n{text}\n\n{name}, вы выиграли: {formarter(user.get(user_id, 'sc_wins_week'))} SC"
    )


async def check_wins():
  while True:
    data = games.get()
    now_h = int(datetime.now().strftime("%H")) + 3
    now = f"{now_h}:{datetime.now().strftime('%M')}:{datetime.now().strftime('%S')}"
    last_time = glob.get()[0][1]
    if now == "24:00:00":
      top = user.top('sc_wins_day')
      if len(top) >= 2:
        text = f"🔥 Итоги ежедневного топа на {formarter(today_prize)} SC:\n\n"
        for a, i in enumerate(top):
          if a <= 9:
            winprize = int(today_prize / 100 * today_wins[a])
            text += f"{emoji_top[a]} {a+1}. {i[0]} - {formarter(i[3])} SC (Приз: {formarter(winprize)} SC)\n"
            user_id = i[1]
            user.update(user_id, 'balance',
                        user.get(user_id, 'balance') + winprize)
          else:
            break
        user.cleartop()
      else:
        text = "❌ Итоги ежедневного рейтинга не подведены, т.к. в топе меньше 2-ух игроков. Топ не обнулен, играем дальше!"
      vk.send(peer_ids=[2000000001, 2000000004], message=text)

    if len(data) > 0:
      for i in data:
        start = int(eval(data[0][2])['start_time'])
        now = int(time.time())
        check = now - start
        if check >= ends:
          peer_id = int(data[0][1])
          vk.send(peer_id=peer_id, message="Подводим итоги...")
          bets = games.getBets(peer_id)
          win_elem = bets['win']
          md5h = bets['md5hash']
          checkhash = bets['checkhash']
          win_color = win_elem['color']
          win_num = win_elem['number']
          win_img = win_elem['img']
          bets = bets['bets']
          win = ""
          if win_num != 0:
            if win_num in numbers_one:
              win_interval = '1-12'
            elif win_num in numbers_two:
              win_interval = "13-24"
            else:
              win_interval = '25-36'
            if win_color == 'черный':
              win = f"{win_num} {win_color}🖤"
            else:
              win = f"{win_num} {win_color}❤️"
            wincheck = f"{win_num} {win_interval} {win_color}"
          else:
            win = "0"
            wincheck = "0"
          text = ""
          for i in bets:
            select = i['select']
            select = str(select)
            x = 0
            if select != "0" and str(win_num) != "0":
              if select == win_color:
                x = 2
              elif select == str(win_num):
                x = 36
              elif select == win_interval:
                x = 3
              else:
                x = 0
            elif select == "0" and str(win_num) == "0":
              x = 36
            else:
              x = 0
            if x:
              prize = int(i['value'] * x)
              user.update(i['user_id'], 'balance',
                          user.get(i['user_id'], 'balance') + prize)
              user.update(i['user_id'], 'game_wins',
                          user.get(i['user_id'], 'game_wins') + 1)
              user.update(i['user_id'], 'sc_wins_day',
                          user.get(i['user_id'], 'sc_wins_day') + prize)
              user.update(i['user_id'], 'sc_wins_week',
                          user.get(i['user_id'], 'sc_wins_week') + prize)
              user.update(i['user_id'], 'xp', user.get(i['user_id'], 'xp') + 1)
              text += f"{i['name']} - {formarter(i['value'])} SC на {select}✅ (Приз: {formarter(prize)} SC x{x})\n"
            else:
              user.update(i['user_id'], 'game_overs',
                          user.get(i['user_id'], 'game_overs') + 1)
              text += f"{i['name']} - {formarter(i['value'])} SC на {select}❌\n"
          vk.send(
            peer_id=peer_id,
            message=
            f"Итоги текущего раунда:\nВыпало: <<{win}>>\n\n{text}\n\nMD5: {md5h}\nПроверка честности: {checkhash}",
            attachment=win_img,
            keyboard=getkeyboard("end", data=f"{checkhash}%%%{md5h}"))
          games.remove(peer_id)
    await asyncio.sleep(1)


async def main():
  try:
    await asyncio.sleep(1)
    for event in lp.listen():
      if event.type == VkBotEventType.WALL_REPOST:
        obj = event.obj
        post_id = obj['copy_history'][0]['id']
        user_id = obj['owner_id']
        name = f"[id{user_id}|{vk.users.get(user_id)['first_name']}]"
        post_data = bonus.get(post_id)
        if len(post_data) > 0:
          post_data = post_data[0]
          start_time = post_data[3]
          end_time = post_data[4]
          userss = eval(post_data[5])
          now = int(time.time())
          check = now - start_time
          if check < end_time:
            if not user_id in userss:
              mbonus = post_data[2]
              users = eval(post_data[5])
              user.update(user_id, 'balance',
                          user.get(user_id, 'balance') + mbonus)
              users.append(user_id)
              bonus.update(post_id, users)
              vk.send(
                peer_id=user_id,
                message=
                f"{name}, за репост записи вы получаете: {formarter(mbonus)} SC"
              )
            else:
              vk.send(
                peer_id=user_id,
                message=f"{name}, вы уже получили награду за данный пост!")
          else:
            bonus.remove(post_id)
            vk.send(
              peer_id=user_id,
              message=
              f"{name}, акция завершилась или пост не участвовал в акции!")
        else:
          vk.send(
            peer_id=user_id,
            message=f"{name}, акция завершилась или пост не участвовал в акции!"
          )

      elif event.type == VkBotEventType.MESSAGE_NEW:
        message = event.obj.message
        user_id = message['from_id']
        if not "-" in str(user_id):
          peer_id = message['peer_id']
          def_text = message['text']
          text = message['text'].lower()
          name = f"[id{user_id}|{vk.users.get(user_id)['first_name']}]"
          try:
            ref = message['ref']
          except:
            ref = None
          try:
            payload = eval(message['payload'])
          except:
            payload = {}

          if "[club" in text:
            text = text.split("] ")[1]
          if user.check(user_id):
            name = user.get(user_id, 'nickname')
            if not "[id" in name:
              name = f"[id{user_id}|{name}]"

            if text == "бонус":
              btime = user.get(user_id, 'last_bonus')
              now = int(time.time())
              check = now - btime
              if check >= 86400:
                user.update(user_id, 'last_bonus', now)
                mbonus = randint(777, 4444)
                user.update(user_id, 'balance',
                            user.get(user_id, 'balance') + mbonus)
                vk.send(
                  peer_id=peer_id,
                  message=f"{name}, вы получили бонус {formarter(mbonus)} SC")
              else:
                check = btime - now
                chtime = time.gmtime(check)
                chtime = time.strftime("%H час. %M мин. %S сек.", chtime)
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"{name}, забрать следующий бонус вы сможете через: {chtime}"
                )

            elif text.startswith("промо "):
              try:
                promocode = def_text.split(" ")[1]
                data = promocodes.get(promocode)
                if len(data) > 0:
                  data = data[0]
                  activations = data[3]
                  if activations >= 1:
                    users_activated = eval(data[5])
                    if not user_id in users_activated:
                      amount = data[4]
                      owner = data[1]
                      user.update(
                        owner, 'reputation',
                        str(float(user.get(owner, 'reputation')) + 0.1))
                      user.update(user_id, 'balance',
                                  user.get(user_id, 'balance') + amount)
                      users_activated.append(
                        user_id) if not user_id in admin_ids else None
                      activations -= 1
                      promocodes.update(promocode, activations,
                                        users_activated)
                      vk.send(
                        peer_id=peer_id,
                        message=
                        f"{name}, вы активировали промокод и получили {formarter(amount)} SC"
                      )
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=
                        f"{name}, вы уже активировали указанный промокод!")
                  else:
                    promocodes.remove(promocode)
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"{name}, у данного промокода закончились активации!")
                else:
                  vk.send(
                    peer_id=peer_id,
                    message=f"{name}, указанного промокода не существует!")
              except Exception as err:
                print(err)
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"{name}, для активации промокода введите: Промо [Промокод]")

            elif text in ['рейтинг', "топы", "топ"]:
              vk.send(peer_id=peer_id,
                      message=f"{name}, какой рейтинг вы хотите увидеть?",
                      keyboard=getkeyboard('top'))

            elif text.startswith("топ дня") or text.startswith("🔥 ежедневный"):
              top_start(peer_id, user_id, name, 'sc_wins_day', True)

            elif text.startswith("топ недели") or text.startswith(
                "🔥 топ недели"):
              top_start(peer_id, user_id, name, 'sc_wins_week', False)

            elif peer_id > 2000000000 and not peer_id in [
                2000000002, 2000000003
            ]:
              if text == "банк":
                if games.check(peer_id):
                  bets = games.getBets(peer_id)
                  start = int(bets['start_time'])
                  now = int(time.time())
                  checkss = now - start
                  if checkss <= ends_two:
                    check = ends - (int(time.time()) - start)
                    text = ""
                    num = 0
                    for a, i in enumerate(bets['bets']):
                      if a <= 11:
                        text += f"{i['name']} - {formarter(i['value'])} SC на {i['select']}\n"
                      else:
                        num = (a + 1) - 12

                    if num >= 1:
                      if num == 1:
                        stavk = "ставка"
                      elif num in [2, 3, 4]:
                        stavk = "ставки"
                      else:
                        stavk = "ставок"
                      text += f"\nНе показано: {num} {stavk}"
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"Список ставок:\n\n{text}\n\nMD5: {bets['md5hash']}\n\nИтоги через: {check} сек."
                    )
                  else:
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"{name}, до конца раунда осталось менее 5-и секунд. Ставки не принимаются!"
                    )
                else:
                  vk.send(peer_id=peer_id,
                          message="Игра будет начата после первой ставки.")

              elif text.startswith("!клав"):
                vk.send(peer_id=peer_id,
                        message="< Клавиатура была обновлена! >",
                        keyboard=getkeyboard())

              elif text.startswith("!прав"):
                if not peer_id in [2000000006]:
                  vk.send(
                    peer_id=peer_id,
                    message=
                    "🔥 Для данной беседы актуальны правила №-1\nhttps://vk.com/topic-220673195_49340597"
                  )
                else:
                  vk.send(
                    peer_id=peer_id,
                    message=
                    "🔥 Для данной беседы актуальны правила №-2\nhttps://vk.com/topic-220673195_49340597"
                  )

              elif text == "1-12":
                balance = user.get(user_id, 'balance')
                data = {
                  'min': int(balance / 100),
                  'med': int(balance / 2),
                  'max': balance
                }
                vk.send(peer_id=peer_id,
                        message=f"{name}, укажите ставку на промежуток 1-12:",
                        keyboard=getkeyboard("go1-12", data))

              elif text == "13-24":
                balance = user.get(user_id, 'balance')
                data = {
                  'min': int(balance / 100),
                  'med': int(balance / 2),
                  'max': balance
                }
                vk.send(peer_id=peer_id,
                        message=f"{name}, укажите ставку на промежуток 13-24:",
                        keyboard=getkeyboard("go13-24", data))

              elif text == "25-36":
                balance = user.get(user_id, 'balance')
                data = {
                  'min': int(balance / 100),
                  'med': int(balance / 2),
                  'max': balance
                }
                vk.send(peer_id=peer_id,
                        message=f"{name}, укажите ставку на промежуток 25-36:",
                        keyboard=getkeyboard("go25-36", data))

              elif text == "черный":
                balance = user.get(user_id, 'balance')
                data = {
                  'min': int(balance / 100),
                  'med': int(balance / 2),
                  'max': balance
                }
                vk.send(peer_id=peer_id,
                        message=f"{name}, укажите ставку на черный цвет:",
                        keyboard=getkeyboard("goblack", data))

              elif text == "красный":
                balance = user.get(user_id, 'balance')
                data = {
                  'min': int(balance / 100),
                  'med': int(balance / 2),
                  'max': balance
                }
                vk.send(peer_id=peer_id,
                        message=f"{name}, укажите ставку на красный цвет:",
                        keyboard=getkeyboard("gored", data))

              elif text.startswith("ставка ") or text.startswith(
                  "с ") or "sector" in payload:
                try:
                  check = False
                  if payload:
                    if "sector" in payload:
                      val = payload['amount']
                      sel = payload['sector']
                  else:
                    val = int(text.split(" ")[1])
                    sel = text.split(" ")[2]
                    if sel in [
                        'black', "чёрный", "черн", "чёрн", "черное", "чёрное"
                    ]:
                      sel = "черный"
                    elif sel in ["red", "красн", "крас", "красное"]:
                      sel = 'красный'
                    elif sel in [
                        'green', 'зелёный', "зеленый", "зелен", "зелён",
                        "зеленое", "зелёное"
                    ]:
                      sel = "0"
                  balance = user.get(user_id, 'balance')
                  if sel in num_intervals or sel in colors:
                    check = True
                  try:
                    sel = int(sel)
                  except:
                    pass
                  if sel in numbers:
                    check = True
                    sel = str(sel)
                  if val >= 10:
                    if balance >= val:
                      if check:
                        if not games.check(peer_id):
                          win = choice(sectors)
                          checkhash = f"{win['number']}/{getrandkey(randint(15,22))}"
                          md5h = md5(checkhash.encode())
                          md5h = md5h.hexdigest()
                          games.add(
                            peer_id, {
                              'bets': [],
                              'start_time': str(int(time.time())),
                              'md5hash': md5h,
                              'checkhash': checkhash,
                              'win': win
                            })
                        bets = games.getBets(peer_id)
                        start = int(bets['start_time'])
                        now = int(time.time())
                        check = now - start
                        stav = False
                        num_sectors_count = 0

                        if check < ends_two:
                          for a, i in enumerate(bets['bets']):
                            if user_id == i['user_id']:
                              selects = i['select']
                              if selects in strnumbers:
                                num_sectors_count += 1
                              if sel == selects:
                                balance -= val
                                user.update(user_id, 'balance', balance)
                                bets['bets'][a][
                                  'value'] = bets['bets'][a]['value'] + val
                                games.bet(peer_id, bets)
                                vk.send(
                                  peer_id=peer_id,
                                  message=
                                  f'{name}, вы успешно сделали ставку: {formarter(val)} SC на "{sel}"'
                                )
                                stav = True
                                break
                              elif sel in colors and selects in colors:
                                if sel != selects:
                                  vk.send(
                                    peer_id=peer_id,
                                    message=
                                    f"{name}, ставить ставку на два цвета нельзя!"
                                  )
                                  stav = True
                                break
                              elif sel in num_intervals and selects in num_intervals:
                                if sel != num_intervals:
                                  vk.send(
                                    peer_id=peer_id,
                                    message=
                                    f"{name}, ставить ставку на несколько промежутков нельзя!"
                                  )
                                  stav = True
                                break
                              elif sel in strnumbers and selects in strnumbers:
                                if num_sectors_count >= 6:
                                  vk.send(
                                    peer_id=peer_id,
                                    message=
                                    f"{name}, нельзя поставить ставку на более чем 6 чисел!"
                                  )
                                  stav = True
                          if not stav:
                            balance -= val
                            user.update(user_id, 'balance', balance)
                            bets = games.getBets(peer_id)
                            bets['bets'].append({
                              'user_id': user_id,
                              'name': name,
                              'value': val,
                              'select': sel
                            })
                            games.bet(peer_id, bets)
                            vk.send(
                              peer_id=peer_id,
                              message=
                              f'{name}, вы успешно сделали ставку: {formarter(val)} SC на "{sel}"'
                            )
                        else:
                          vk.send(
                            peer_id=peer_id,
                            message=
                            f"{name}, до конца раунда осталось менее 5-и секунд. Ставки не принимаются!"
                          )
                      else:
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"{name}, укажите ставку правильно: Ставка [Сумма] [Сектор]",
                          keyboard=getkeyboard("err_sel"))
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=f"{name}, у вас недостаточно SC для ставки!")
                  else:
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"{name}, сумма ставки не может быть меньше 10 SC!")
                except Exception as err:
                  print(err)
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"{name}, укажите ставку правильно: Ставка [Сумма] [Сектор]",
                    keyboard=getkeyboard("err_sel"))
                  pass

              elif text.startswith('бал'):
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"{name}, ваш баланс: {formarter(user.get(user_id, 'balance'))} SC"
                )

              elif text in [
                  'чек', "проверка", "чекни", "стат", "статистика", "статус",
                  "стата"
              ]:
                chatid = peer_id - 2000000000
                if chatid in official_chats:
                  text = "👑 Данная беседа является официальной"
                elif chatid in verify_chats:
                  text = "✔️ Данная беседа подтверждена администрацией"
                else:
                  text = "⭕ Данная беседа не подтверждена"

                text = f"""{text}
    🆔 ID беседы: {chatid} ({peer_id})
    
    💠 Версия: 1.72Release
    ✔️ Скорость работы: (~99.{randint(7,9)}%)
    ⌛ Прошло с момента запуска: {int(time.time()) - botstart} сек.
                """
                vk.send(peer_id=peer_id,
                        message=text,
                        keyboard=getkeyboard("stat"))

              elif text == "update log":
                if payload['command'] == "update_log":
                  vk.send(peer_id=peer_id,
                          message="""Last Update::

    1.7-1.8Release | От 04.06.2023:
    ➕ Добавлено:
    - Бесплатное изменение никнейма
    - Кликер Start Coin

    📝 Изменено & Исправлено:
    - Отныне раунд будет длиться 60сек.
    - Система ставок через кнопки
    - Повышены ежедневный бонус и награды реферальной системы
    - Разные ошибки в коде, замедляющие работу бота
    """)

              elif text.startswith("выдать ") and user_id == admin_ids[0]:
                try:
                  us_id = idsplit(text)
                  amount = int(text.split(" ")[2])
                  if amount >= 1:
                    if user.check(us_id):
                      user.update(us_id, 'balance',
                                  user.get(us_id, 'balance') + amount)
                      try:
                        vk.send(
                          peer_id=us_id,
                          message=f"Вам было выдано {formarter(amount)} SC")
                      except:
                        pass
                      vk.send(
                        peer_id=peer_id,
                        message=
                        f"[id{user_id}|Вы] успешно выдали [id{us_id}|Пользователю] - {formarter(amount)} SC"
                      )
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=f"[id{us_id}|Пользователь] не зарегистрирован!"
                      )
                  else:
                    vk.send(peer_id=peer_id, message="Укажите сумму от 1 SC")
                except:
                  pass

              elif text.startswith("обнулить ") and user_id == admin_ids[0]:
                try:
                  us_id = idsplit(text)
                  if user.check(us_id):
                    user.update(us_id, 'balance', 0)
                    try:
                      vk.send(peer_id=us_id,
                              message="Ваш баланс был обнулен администрацией!")
                    except:
                      pass
                    vk.send(
                      peer_id=peer_id,
                      message=f"Баланс [id{us_id}|Пользователя] был обнулен!")
                  else:
                    vk.send(
                      peer_id=peer_id,
                      message=f"[id{us_id}|Пользователь] не зарегистрирован!")
                except:
                  pass

              elif text.startswith("перевод ") or text.startswith("передать "):
                try:
                  us_id = idsplit(text)
                  amount = int(text.split(" ")[2])
                  if amount >= 100:
                    if us_id != user_id:
                      if user.check(us_id):
                        nameus = f"[id{us_id}|{vk.users.get(us_id)['first_name']}]"
                        if amount < 10000:
                          commision = 2
                        elif amount >= 10000 and amount <= 150000:
                          commision = 5
                        elif amount > 150000 and amount <= 850000:
                          commision = 8
                        elif amount > 850000 and amount <= 1500000:
                          commision = 12
                        elif amount > 1500000 and amount <= 3000000:
                          commision = 20
                        else:
                          commision = 25
                        coast = amount + (amount / 100 * commision)
                        user.update(
                          user_id, 'json', {
                            'confirm_transaction': 1,
                            'info': {
                              'us_id': us_id,
                              'amount': amount,
                              'coast': coast
                            }
                          })
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"""{name}, вы уверены, что хотите совершить перевод?

      Получатель: {nameus} (ID: {us_id})
      Сумма: {formarter(amount)} SC
      Спишется с учетом комиссии {commision}%: {formarter(coast)}""",
                          keyboard=getkeyboard("transaction_next"))
                      else:
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"{name}, указанный пользователь не зарегистрирован в системе"
                        )
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=f"{name}, нельяз переводить самому себе!")
                  else:
                    vk.send(
                      peer_id=peer_id,
                      message=f"{name}, минимальная сумма для перевода 100 SC!"
                    )
                except:
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"{name}, для перевод введите: передать [VK ID] [Сумма]")

              elif "секторы" in text:
                vk.send(peer_id=peer_id,
                        message=f"""{name}, список секторов:
    - Цвета: черный, красный, зеленый (0)
    - Промежутки: 1-12, 13-24, 25-36
    - Числа: от 0 до 36""")

              elif text.startswith("реф"):
                vk.send(
                  peer_id=peer_id,
                  message=f"{name}, реф. система работает только в ЛС с ботом")

              elif text.startswith("создать промо"):
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"{name}, создавать промокоды можно только в ЛС с ботом")

              elif text.startswith("проф"):
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"{name}, просматривать профиль можно только в ЛС с ботом")

              elif text == "продолжить":
                if payload:
                  if payload['command'] == "confirm_transaction_next":
                    data = eval(user.get(user_id, 'json'))
                    if "confirm_transaction" in data:
                      data = data['info']
                      balance = user.get(user_id, 'balance')
                      us_id = data['us_id']
                      amount = data['amount']
                      coast = data['coast']
                      if balance >= coast:
                        balance -= coast
                        user.update(user_id, 'balance', balance)
                        user.update(us_id, 'balance',
                                    user.get(us_id, 'balance') + amount)
                        user.update(user_id, 'json', {})
                        nameus = f"[id{us_id}|{vk.users.get(us_id)['first_name']}]"
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"{name}, вы успешно перевели {formarter(amount)} SC игроку - {nameus}"
                        )
                        try:
                          vk.send(
                            peer_id=us_id,
                            message=
                            f"{nameus}, игрок {name} перевел вам {formarter(amount)} SC"
                          )
                        except:
                          pass
                      else:
                        vk.send(
                          peer_id=peer_id,
                          message=f"{name}, у вас недостаточно SC для перевода!"
                        )

            elif peer_id == 2000000002:
              vk.send(
                peer_id=peer_id,
                message=
                f"{name}, данная беседа создана исключительно для доставки уведомлений от бота"
              )

            elif peer_id == 2000000003:
              if user_id in admin_ids:
                if text in ['команды', "помощь", "меню"]:
                  vk.send(peer_id=peer_id,
                          message=f"""{name}, доступные команды в вашей беседе:
    +реп - добавить запись в базу
    !реп - посмотреть информацию о посте из базы
    -реп - досрочно удалить запись из базы

    В данное беседе не работает большинство команд, т.к. она является <<Административной>>"""
                          )

                elif text.startswith("выдать") or text.startswith("обнулить"):
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"{name}, указанная админ-команда не доступна в данной беседе!"
                  )

                elif text == "+реп":
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"""{name}, чтобы добавить пост в базу введите: +реп [ID поста / Ссылка] [Бонус] [Сек. до окончания]

    Подробней:
    ID Поста - Скопировать ссылку на пост с акцией, число после _ (Нижнего подчеркивания) - это и будет ID
    Бонус - Награда за репост записи
    Сек. до окончания - Сколько секунд будет длиться раздача (Как только пройденное время достигает указанного числа, пост удаляется из базы)"""
                  )

                elif text == "-реп":
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"""{name}, чтобы удалить пост из базы введите: -реп [ID поста]"""
                  )

                elif text == "!реп":
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"{name}, чтобы увидеть данные о посте из базы введите: !реп [ID поста]"
                  )

                elif text.startswith("!реп"):
                  try:
                    post_id = postidsplit(text)
                    post_data = bonus.get(post_id)
                    text = ""
                    if len(post_data) > 0:
                      post_data = post_data[0]
                      check = int(time.time()) - post_data[3]
                      if check < post_data[4]:
                        for i in eval(post_data[5]):
                          text += f"{i}, "
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"""{name}, информацию о посте https://vk.com/wall-220673195_{post_id} из базы:

    Base ID: {post_data[0]}
    Награда: {formarter(post_data[2])}
    Акция продлится еще: {post_data[4] - check} сек.
    ID Пользователей, получивших награду:

    {text}""")
                      else:
                        bonus.remove(post_id)
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"{name}, акция завершилась и была удалена из базы!")
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=f"{name}, поста с указанным ID нет в базе!")
                  except Exception as err:
                    print(err)
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"{name}, чтобы увидеть данные о посте из базы введите: !реп [ID поста]"
                    )

                elif text.startswith("+реп "):
                  try:
                    post_id = postidsplit(text)
                    mbonus = int(text.split(" ")[2])
                    sec = int(text.split(" ")[3])
                    if mbonus >= 10 and sec >= 3600:
                      bonus.add(post_id, mbonus, int(time.time()), sec)
                      vk.send(
                        peer_id=peer_id,
                        message=
                        f"""{name}, запись https://vk.com/wall-220673195_{post_id} была добавлена в базу:

    Автор: {name}
    Награда за репост: {formarter(mbonus)} SC
    Акция продлится еще: {sec} сек.""")
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=
                        f"{name}, минимальная награда: 10 SC | Минимальное число сек.: 3600 (1 час)"
                      )
                  except Exception as err:
                    print(err)
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"""{name}, чтобы добавить пост в базу введите: +реп [ID поста / Ссылка] [Бонус] [Сек. до окончания]

    Подробней:
    ID Поста - Скопировать ссылку на пост с акцией, число после _ (Нижнего подчеркивания) - это и будет ID
    Бонус - Награда за репост записи
    Сек. до окончания - Сколько секунд будет длиться раздача (Как только пройденное время достигает указанного числа, пост удаляется из базы)"""
                    )

                elif text.startswith("-реп "):
                  try:
                    post_id = postidsplit(text)
                    comment = None
                    if "\\n" in text:
                      comment = text.split(f"{post_id}\n")[1]
                    if len(bonus.get(post_id)) > 0:
                      bonus.remove(post_id)
                      if comment:
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"""{name}, запись https://vk.com/wall-220673195_{post_id} была удалена из базы.
    Комментарий: {comment}""")
                      else:
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"{name}, запись https://vk.com/wall-220673195_{post_id} была удалена из базы"
                        )
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=f"{name}, записи с таким ID в базе не найдено!"
                      )
                  except:
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"""{name}, чтобы удалить пост из базы введите: -реп [ID поста / Ссылка]"""
                    )

            else:
              if text in [
                  'начать', "start", 'меню', 'команды', "помощь", "ком",
                  "назад"
              ] or text.startswith("!клав"):
                vk.send(peer_id=peer_id,
                        message=f"{name}, ваша клавиатура:",
                        keyboard=getkeyboard("menu"))

              elif text in ['беседы', "чаты", "играть"]:
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"{name}, скорее начни поднимать Start Coin! Заходи в одну из бесед и играйся!",
                  keyboard=getkeyboard("chats"))

              elif text.startswith("реф"):
                ref_id = user.get(user_id, 'ref_id')
                if not ref_id or ref_id == "None":
                  for i in range(10):
                    ref_id = getrandkey(randint(5, 12))
                    if not user.ref.check(ref_id):
                      user.update(user_id, 'ref_id', ref_id)
                      ref_link = vk.utils.getShortLink(
                        f"https://mainrep.pagstart.repl.co/startwheel/vkme?refid={ref_id}"
                      )['short_url']
                      user.update(user_id, 'ref_link', ref_link)
                      break
                ref_link = user.get(user_id, 'ref_link')
                ref_users = user.get(user_id, 'ref_users')
                if user.get(user_id, 'ref_reset') == 1:
                  vk.send(peer_id=peer_id,
                          message=f"""{name}, реферальная система:

    Ваш ref_Id: {ref_id}
    По вашей ссылке перешло {ref_users} чел.

    - За каждого пользователя вы получаете 3000 SC
    - Каждый пользователь, которого вы пригласили, получает 1500 SC

    Ваша короткая ссылка: {ref_link}

    ❕ Вы можете изменить ref_Id на другой случайный ID, но только 1 раз!
    """,
                          keyboard=getkeyboard("changerefid"))
                else:
                  vk.send(peer_id=peer_id,
                          message=f"""{name}, реферальная система:

    Ваш ref_Id: {ref_id}
    По вашей ссылке перешло: {ref_users} чел.

    - За каждого пользователя вы получаете 3000 SC
    - Каждый пользователь, которого вы пригласили, получает 1500 SC

    Ваша короткая ссылка: {ref_link}
    """)

              elif text == "❕ изменить ref_id":
                if user.get(user_id, 'ref_reset') == 1:
                  user.update(user_id, 'ref_reset', 0)
                  for i in range(10):
                    ref_id = getrandkey(randint(5, 12))
                    if not user.ref.check(ref_id):
                      user.update(user_id, 'ref_id', ref_id)
                      ref_link = vk.utils.getShortLink(
                        f"https://vk.com/write-220673195?ref={ref_id}"
                      )['short_url']
                      user.update(user_id, 'ref_link', ref_link)
                      break
                  vk.send(peer_id=peer_id,
                          message=f"{name}, ваш новый ref_Id: {ref_id}")
                else:
                  vk.send(peer_id=peer_id,
                          message=f"{name}, вы уже меняли свой ref_Id!")

              elif text.startswith("обнулить") or text.startswith(
                  "выдать") and user_id in admin_ids:
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"{name}, данная админ-команда работает только в беседах с ботом "
                )

              elif text == "сбт":
                vk.send(peer_id=peer_id,
                        message=f"""{name}, Система Быстрых Транзакций (BETA)
    Для генерации ссылки БТ введите: сбт [ID получателя] [Сумма]

    Подробнее про СБТ - https://vk.com/@startwheel-system-fast-transactions
    Проблемы с транзакциями? Не пришли средства? Обманули? - Обращайтесь в [startwheel_help|Тех. поддержку]"""
                        )

              elif text.startswith("сбт "):
                try:
                  user_id = idsplit(text)
                  amount = int(text.split(" ")[2])
                  sid = getrandkey(randint(5, 25))
                  if amount >= 1:

                    json = {
                      "transaction": {
                        "user_id": user_id,
                        "amount": amount,
                        "id": sid
                      }
                    }

                    link = "".join(str(json).split(" "))
                    link = f"https://mainrep.pagstart.repl.co/startwheel/sbt?payment={link}"
                    surl = vk.utils.getShortLink(link)['short_url']
                    vk.send(
                      peer_id=peer_id,
                      message=f"""{name}, ваша ссылка для Быстрой Транзакции:

    {surl}""")
                  else:
                    vk.send(peer_id=peer_id,
                            message=f"{name}, укажите сумму минимум от 1 SC!")
                except Exception as err:
                  print(err)
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"{name}, для генерации ссылки БТ введите: сбт [ID получателя] [Сумма]"
                  )
                  pass

              elif text == "подтвердить":
                try:
                  if str(ref).startswith("{'transaction':{"):
                    ref = eval(ref)['transaction']
                    us_id = int(ref['user_id'])
                    amount = int(ref['amount'])
                    sid = ref['id']
                    balance = user.get(user_id, 'balance')
                    if user_id != us_id:
                      if balance >= amount:
                        balance -= amount
                        nameus = f"[id{us_id}|{vk.users.get(us_id)['first_name']}]"
                        user.update(user_id, 'balance', balance)
                        user.update(us_id, 'balance',
                                    user.get(us_id, 'balance') + amount)
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"[СБТ / Успешно: \nㅤПеревод [id{us_id}|{sid}] на сумму {amount} SC]"
                        )
                        vk.send(
                          peer_id=us_id,
                          message=
                          f"[СБТ / Перевод #{sid}: \nㅤИгрок {name} перевел вам {amount} SC]"
                        )
                        vk.send(
                          peer_id=2000000002,
                          message=
                          f"[СБТ / Перевод #{sid}: \nㅤИгрок {name} перевел {nameus} - {amount} SC]"
                        )
                      else:
                        vk.send(
                          peer_id=peer_id,
                          message=
                          "[СБТ / Ошибка: \nㅤУ вас недостаточно SC для перевода]"
                        )
                        vk.send(
                          peer_id=us_id,
                          message=
                          f"[СБТ / Ошибка: \nㅤПеревод #{sid} отменен || У игрока недостаточно SC]"
                        )
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=
                        "[СБТ / Ошибка: \nㅤНельзя подтвердить свою же транзакцию]"
                      )
                except Exception as err:
                  print(err)
                  pass

              elif text == "промокоды":
                data = 1 if user.get(
                  user_id, 'level') >= 3 or user_id in admin_ids else 0
                vk.send(peer_id=peer_id,
                        message=f"{name}, меню промокодов:",
                        keyboard=getkeyboard("promocodes", data))

              elif text == "мои промокоды":
                promos = promocodes.getvkid(user_id)
                text = ""
                next_text = ""
                next_text2 = ""
                next_text3 = ""
                for a, i in enumerate(promos):
                  if a <= 9:
                    text += f"{i[0]}. {i[2]}\nㅤ- Осталось активаций: {i[3]}\nㅤ- Награда: {formarter(i[4])}\n\n"
                  elif a > 9 and a <= 19:
                    next_text += f"{i[0]}. {i[2]}\nㅤ- Осталось активаций: {i[3]}\nㅤ- Награда: {formarter(i[4])}\n\n"
                  elif a > 19 and a <= 29:
                    next_text2 += f"{i[0]}. {i[2]}\nㅤ- Осталось активаций: {i[3]}\nㅤ- Награда: {formarter(i[4])}\n\n"
                  else:
                    break
                data = [text, next_text, next_text2]
                user.update(user_id, 'promo_json', data)
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"{name}, ваши последние 30 активных промокодов (1/3):\n\n{text}",
                  keyboard=getkeyboard("next", num=0))

              elif text == "▶️":
                if payload:
                  if 'page' in payload:
                    num = payload['page']
                    text = eval(user.get(user_id, 'promo_json'))[num]
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"{name}, ваши последние 30 активных промокодов ({num+1}/3):\n\n{text}",
                      keyboard=getkeyboard("next", num=num))

              elif text == "◀️":
                if payload:
                  if 'page' in payload:
                    num = payload['page']
                    text = eval(user.get(user_id, 'promo_json'))[num]
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"{name}, ваши последние 30 активных промокодов ({num+1}/3):\n\n{text}",
                      keyboard=getkeyboard("next", num=num))

              elif text in ['промо', "активировать"]:
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"{name}, для активации промокода введите: Промо [Промокод]")

              elif text in ["создать промо", "создать"]:
                if user.get(user_id, 'level') >= 3 or user_id in admin_ids:
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"{name}, для создания промокода введите (Все данные указывать без пробелов): Создать промо [Промокод] [Кол-во активаций > 1] [Сумма > 100]"
                  )
                else:
                  vk.send(
                    peer_id=peer_id,
                    message=f"{name}, создавать промокоды можно с 3-го уровня")

              elif text.startswith("создать промо "):
                try:
                  promo = def_text.split(" ")[2]
                  activations = int(text.split(" ")[3])
                  amount = int(text.split(" ")[4])
                  if user.get(user_id, 'level') >= 3 or user_id in admin_ids:
                    if len(promo) >= 3 and len(promo) <= 15:
                      checker = promocodes.get(promo)
                      if len(checker) <= 0:
                        if activations >= 1 and amount >= 100:
                          if amount <= 1000:
                            commision = 3
                          elif amount > 1000 and amount <= 50000:
                            commision = 7
                          elif amount > 50000 and amount <= 250000:
                            commision = 10
                          elif amount > 250000 and amount <= 1000000:
                            commision = 15
                          else:
                            commision = 25
                          comka = int(amount / 100) * commision
                          price = amount * activations + comka
                          user.update(
                            user_id, 'json', {
                              'create_promo_verify': 1,
                              'promocode': {
                                'promo': promo,
                                'activations': activations,
                                'amount': amount,
                                'price': price
                              }
                            })
                          vk.send(
                            peer_id=peer_id,
                            message=
                            f"""{name}, вы уверены, что хотите создать промокод?
      Промо: {promo}
      Кол-во активаций: {activations}
      Сумма после активации: {formarter(amount)} SC

      Стоимость промокода с учетом комиссии {commision}%: {price} SC
      Для продолжения нажмите кнопку <<Продолжить>>""",
                            keyboard=getkeyboard("create_promo"))
                        else:
                          vk.send(
                            peer_id=peer_id,
                            message=
                            f"{name}, для создания промокода введите (Все данные указывать без пробелов): Создать промо [Промокод] [Кол-во активаций > 1] [Сумма > 100]"
                          )
                      else:
                        vk.send(
                          peer_id=peer_id,
                          message=f'{name}, указанный промокод уже существует!'
                        )
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=
                        f"{name}, минимальная длина промокода: 3 символа | Максимальная: 15 символов"
                      )
                  else:
                    vk.send(
                      peer_id=peer_id,
                      message=f"{name}, создавать промокоды можно с 3-го уровня"
                    )
                except Exception as err:
                  print(err)
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"{name}, для создания промокода введите (Все данные указывать без пробелов): Создать промо [Промокод] [Кол-во активаций > 1] [Сумма > 100]"
                  )

              elif text.startswith("!ник "):
                try:
                  new_nick = def_text.split("ик ")[1]
                  if len(new_nick) >= 5 and len(new_nick) <= 15:
                    check = user.get(nickname=new_nick)
                    if not check:
                      user.update(user_id, 'nickname', new_nick)
                      vk.send(
                        peer_id=peer_id,
                        message=
                        f"{name}, ваш никнейм был изменен на: [id{user_id}|{new_nick}]!"
                      )
                    else:
                      vk.send(
                        peer_id=peer_id,
                        message=
                        f"{name}, пользователь с таким никнеймом уже существует!"
                      )
                  else:
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"{name}, максимальная длина никнейма: 15 символов. Минимальная: 5."
                    )
                except Exception as err:
                  print(err)
                  vk.send(
                    peer_id=peer_id,
                    message=
                    f"{name}, для смены никнейма введите: !Ник [Новый никнейм]"
                  )

              elif text == "продолжить":
                if payload:
                  if payload['command'] == "create_promo_next":
                    data = eval(user.get(user_id, 'json'))
                    if 'create_promo_verify' in data:
                      data = data['promocode']
                      balance = user.get(user_id, 'balance')
                      amount = data['amount']
                      price = data['price']
                      if balance >= price:
                        balance -= price
                        user.update(user_id, 'json', {})
                        user.update(user_id, 'balance', balance)
                        if not user_id in admin_ids:
                          promocodes.add(data['promo'], user_id,
                                         data['activations'], amount,
                                         [user_id])
                        else:
                          promocodes.add(data['promo'], user_id,
                                         data['activations'], amount, [])
                        vk.send(peer_id=peer_id,
                                message=f"""{name}, промокод успешно создан!
    Промокод: {data['promo']}
    Кол-во активаций: {data['activations']}
    Награда: {formarter(amount)} SC

    Для активации введите: Промо {data['promo']}""")
                      else:
                        vk.send(
                          peer_id=peer_id,
                          message=
                          f"{name}, у вас недостаточно SC для создания промокода!"
                        )

              elif text.startswith("проф"):
                xp = user.get(user_id, 'xp')
                level = user.get(user_id, 'level')
                text = ""
                if level == 1:
                  limitxp = 10
                  text = f"({xp}/{limitxp})"
                  if xp >= limitxp:
                    level += 1
                    xp = 0
                    user.update(user_id, 'level', level)
                    user.update(user_id, 'xp', 0)
                    text = f"({xp}/20)"
                elif level == 2:
                  limitxp = 20
                  text = f"({xp}/{limitxp})"
                  if xp >= limitxp:
                    level += 1
                    xp = 0
                    user.update(user_id, 'level', level)
                    user.update(user_id, 'xp', 0)
                    text = f"({xp}/35)"
                elif level == 3:
                  limitxp = 35
                  text = f"({xp}/{limitxp})"
                  if xp >= limitxp:
                    level += 1
                    xp = 0
                    user.update(user_id, 'level', level)
                    user.update(user_id, 'xp', 0)
                    text = f"({xp}/50)\n✨ Репутация: {user.get(user_id, 'reputation')}"
                elif level == 4:
                  limitxp = 50
                  text = f"({xp}/{limitxp})"
                  if xp >= limitxp:
                    level += 1
                    xp = 0
                    user.update(user_id, 'level', level)
                    user.update(user_id, 'xp', 0)
                    text = f"({xp}/20)\n✨ Репутация: {user.get(user_id, 'reputation')}"
                elif level == 5:
                  text = "(Максимальный)\n✨ Репутация: {user.get(user_id, 'reputation')}"
                vk.send(peer_id=peer_id,
                        message=f"""{name}, ваш профиль:

    🆔 Игровой ID: {user.get(user_id, 'id')}
    📶 Уровень: {user.get(user_id, 'level')} {text}
    💰 Баланс: {formarter(user.get(user_id, 'balance'))} SC
    👥 Вы пригласили: {user.get(user_id, 'ref_users')} чел.

    😎 Побед: {user.get(user_id, 'game_wins')}
    😓 Поражений: {user.get(user_id, 'game_overs')}""")

              elif text.startswith("мерч"):
                vk.send(
                  peer_id=peer_id,
                  message=f"""{name}, мерчанты находятся в разработке.""")

              elif text.startswith("!чек ") and user_id == admin_ids[0]:
                try:
                  peerid = text.split(" ")[1]
                  data = games.getBets(peerid)
                  if data:
                    vk.send(
                      peer_id=peer_id,
                      message=
                      f"Выпадет: {data['win']['number']} {data['win']['color']}"
                    )
                  else:
                    vk.send(peer_id=peer_id,
                            message=f"{name}, в данной беседе нет игры!")
                except Exception as err:
                  print(err)
                  pass

              elif text == "кликер":
                vk.send(peer_id=peer_id,
                        message="< Меню кликера >",
                        keyboard=getkeyboard("clicker"))

              elif text == "клик":
                balance = user.get(user_id, 'balance')
                forclick = randint(10, per_click)
                balance += forclick
                user.update(user_id, 'balance', balance)
                vk.send(
                  peer_id=peer_id,
                  message=
                  f"💠 +{formarter(forclick)} SC\n{name}, ваш баланс: {formarter(balance)} SC"
                )

          else:
            user.add(user_id, name)
            if ref and not ref.startswith("{'transaction':{"):
              owner_id = user.ref.get(ref)
              ownername = f"[id{owner_id}|{vk.users.get(owner_id)['first_name']}]"
              user.update(owner_id, 'ref_users',
                          user.get(owner_id, 'ref_users') + 1)
              user.update(owner_id, 'balance',
                          user.get(owner_id, 'balance') + 3000)
              user.update(user_id, 'balance', 1500)
              user.update(user_id, 'ref_owner', owner_id)
              vk.send(
                peer_id=peer_id,
                message=
                f'{name}, добро пожаловать в наше виртуальное казино Start Wheel на игровую валюту Start Coin! Вас пригласил: {ownername}, за что вы получаете 1500 SC!'
              )
              try:
                vk.send(
                  peer_id=owner_id,
                  message=
                  f'{ownername}, пользователь {name} зарегистрировался по вашей ссылке! Вы получаете: 3000 SC!'
                )
              except:
                pass
              vk.send(
                peer_id=2000000002,
                message=
                f"[Реф / Приглашение: \nㅤПользователь {name} зарегистрировался по ссылке {ownername}]"
              )
            else:
              vk.send(
                peer_id=peer_id,
                message=
                f"{name}, добро пожаловать в наше виртуальное казино Start Wheel на игровую валюту Start Coin!"
              )
  except Exception as err:
    print(err)
    pass


def firsttar():
  asyncio.run(main())


def secondtar():
  asyncio.run(check_wins())


def thirdtar():
  asyncio.run(check_top())


thread1 = threading.Thread(target=firsttar)
thread1.start()

thread2 = threading.Thread(target=secondtar)
thread2.start()
