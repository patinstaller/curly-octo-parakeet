from vk_api.keyboard import VkKeyboard

primary = "primary"
positive = "positive"
negative = "negative"

def formarter(var):
  if var >= 10000:
    var = '{:,}'.format(var).replace(',', ' ')
  return var


def getkeyboard(key="chat", data=None, num=None):
  if key == "chat":
    keyboards = VkKeyboard(one_time=False)
    keyboards.add_button("Банк", color=positive)
    keyboards.add_button("Баланс", color=primary)
    keyboards.add_line()
    keyboards.add_button("1-12")
    keyboards.add_button("13-24")
    keyboards.add_button("25-36")
    keyboards.add_line()
    keyboards.add_button("Черный")
    keyboards.add_button("Красный")
    keyboards.add_line()
    keyboards.add_button("Рейтинг", color=negative)
    keyboards.add_button("Бонус", color=positive)
  elif key == "go1-12":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button(f"{formarter(data['min'])}", payload={"amount": data['min'], "sector": '1-12'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['med'])}", payload={"amount": data['med'], "sector": '1-12'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['max'])}", payload={"amount": data['max'], "sector": '1-12'})
  elif key == "go13-24":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button(f"{formarter(data['min'])}", payload={"amount": data['min'], "sector": '13-24'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['med'])}", payload={"amount": data['med'], "sector": '13-24'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['max'])}", payload={"amount": data['max'], "sector": '13-24'})
  elif key == "go25-36":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button(f"{formarter(data['min'])}", payload={"amount": data['min'], "sector": '25-36'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['med'])}", payload={"amount": data['med'], "sector": '25-36'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['max'])}", payload={"amount": data['max'], "sector": '25-36'})
  elif key == "goblack":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button(f"{formarter(data['min'])}", payload={"amount": data['min'], "sector": 'черный'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['med'])}", payload={"amount": data['med'], "sector": 'черный'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['max'])}", payload={"amount": data['max'], "sector": 'черный'})
  elif key == "gored":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button(f"{formarter(data['min'])}", payload={"amount": data['min'], "sector": 'красный'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['med'])}", payload={"amount": data['med'], "sector": 'красный'})
    keyboards.add_line()
    keyboards.add_button(f"{formarter(data['max'])}", payload={"amount": data['max'], "sector": 'красный'})
  elif key == "chats":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_openlink_button(
      "Start Wheel | #1",
      "https://vk.me/join/uNxcC4LPNshOLbs7A5ypccIzFP7Rkd7LTbc=")
    keyboards.add_openlink_button(
      "Start Wheel | #2",
      "https://vk.me/join/x8G_ZqWY1iDgrukf9YHdWjoSCWRXXLjFsuI=")
    keyboards.add_line()
    keyboards.add_openlink_button(
      "Start Wheel | Общение",
      "https://vk.me/join/9gMS3MtoRewaiXo_te1pIQAqUFUHv2RUXZ8=")
  elif key == "clicker":
    keyboards = VkKeyboard(one_time=False)
    keyboards.add_button("Клик")
    keyboards.add_line()
    keyboards.add_button("Назад", color=negative)
  elif key == "menu":
    keyboards = VkKeyboard(one_time=False)
    keyboards.add_button("Беседы", color=positive)
    keyboards.add_line()
    keyboards.add_button("Профиль", color=primary)
    keyboards.add_button("Бонус", color=positive)
    keyboards.add_button("Кликер")
    keyboards.add_line()
    keyboards.add_button("Рефералка")
    keyboards.add_button("Промокоды")
    keyboards.add_line()
    keyboards.add_button("Рейтинг", color=negative)
  elif key == "promocodes":
    keyboards = VkKeyboard(one_time=False)
    if data == 1:
      keyboards.add_button("Создать", color=positive)
    else:
      keyboards.add_button("Создать", color=negative)
    keyboards.add_button("Активировать")
    keyboards.add_line()
    keyboards.add_button("Мои промокоды")
    keyboards.add_line()
    keyboards.add_button("Назад", color=primary)
  elif key == "next":
    keyboards = VkKeyboard(inline=True)
    if num == 0:
      keyboards.add_button("▶️", payload={"page": 1})
    elif num == 1:
      keyboards.add_button("◀️", payload={"page": 0})
      keyboards.add_button("▶️", payload={"page": 2})
    elif num == 2:
      keyboards.add_button("◀️", payload={"page": 1})
  elif key == "err_sel":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button("❔ Какие секторы есть?")
  elif key == "changerefid":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button("❕ Изменить ref_Id", color=negative)
  elif key == "create_promo":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button("Продолжить",
                         color=negative,
                         payload={"command": "create_promo_next"})
  elif key == "transaction_next":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button("Продолжить",
                         color=negative,
                         payload={"command": "confirm_transaction_next"})
  elif key == "stat":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button("Update Log", payload={"command": "update_log"})
  elif key == "top":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_button("🔥 Ежедневный")
  elif key == "end":
    keyboards = VkKeyboard(inline=True)
    keyboards.add_openlink_button("Проверка честности", f"https://mainrep.pagstart.repl.co/startwheel/md5?text={data}")
  return keyboards.get_keyboard()
