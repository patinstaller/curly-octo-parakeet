import sqlite3 as sql
import json


def connect():
  return sql.connect("database.db", check_same_thread=False)

numbersss_check = list(range(0,37))


class user:

  def create():
    con = connect()
    db = con.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS 'users'
			(id INTEGER PRIMARY KEY AUTOINCREMENT,
			uid INTEGER,
			nickname TEXT,
			level INTEGER DEFAULT 1,
			xp INTEGER DEFAULT 0,
			balance INTEGER DEFAULT 0,
			reputation TEXT DEFAULT '0.0',
			sc_wins_day INTEGER DEFAULT 0,
			sc_wins_week INTEGER DEFAULT 0,
			game_wins INTEGER DEFAULT 0,
			game_overs INTEGER DEFAULT 0,
			last_bonus INTEGER DEFAULT 0,
			chat TEXT DEFAULT 'def',
			ref_owner INTEGER DEFAULT 0,
			ref_id TEXT,
			ref_link TEXT,
			ref_users INTEGER DEFAULT 0,
			ref_reset INTEGER DEFAULT 1,
			json TEXT DEFAULT "{}",
			promo_json TEXT DEFAULT "[]") 
			""")
    con.commit()
    con.close()

  def add(user_id, name):
    con = connect()
    db = con.cursor()
    db.execute(
      f"INSERT INTO 'users' (uid, nickname) VALUES ({user_id}, '{name}')")
    con.commit()
    con.close()

  def get(user_id=None, var=None, nickname=None):
    con = connect()
    db = con.cursor()
    if not nickname:
      if user_id:
        if var:
          db.execute(f"SELECT {var} FROM 'users' WHERE uid = {user_id}")
          val = db.fetchone()[0]
        else:
          db.execute(f"SELECT * FROM 'users' WHERE uid = {user_id}")
          val = db.fetchall()
      else:
        db.execute("SELECT * FROM 'users'")
        val = db.fetchall()
    else:
      db.execute(f"SELECT uid FROM 'users' WHERE nickname = '{nickname}'")
      val = db.fetchone()
    if var == "balance" and int(val) >= 100000000000000:
      user.update(user_id, 'balance', 100000000000000)
      val = 100000000000000
    con.commit()
    con.close()
    return val

  def update(user_id, var, val):
    con = connect()
    db = con.cursor()
    if str(type(val)) in ["<class 'dict'>", "<class 'list'>"]:
      val = json.dumps(val)
    if str(type(val)) == "<class 'int'>":
      db.execute(f"UPDATE 'users' SET {var} = {val} WHERE uid = {user_id}")
    else:
      db.execute(f"UPDATE 'users' SET {var} = '{val}' WHERE uid = {user_id}")
    con.commit()
    con.close()

  def check(user_id):
    con = connect()
    db = con.cursor()
    db.execute(f"SELECT id FROM 'users' WHERE uid = {user_id}")
    val = db.fetchone()
    con.commit()
    con.close()
    if val is None:
      return False
    else:
      return True

  def top(var, limit=None):
    con = connect()
    db = con.cursor()
    db.execute(
      f"SELECT nickname, uid, balance, {var} FROM 'users' WHERE uid != 498475943 AND uid != 644686917 AND uid != 693647474 and sc_wins_day > 0 ORDER BY {var} DESC"
    )
    val = db.fetchall()
    con.commit()
    con.close()
    return val

  def remove(user_id):
    con = connect()
    db = con.cursor()
    db.execute(f"DELETE FROM 'users' WHERE uid = {user_id}")
    con.commit()
    con.close()

  def cleartop():
    con = connect()
    db = con.cursor()
    db.execute("UPDATE 'users' SET sc_wins_day = 0")
    con.commit()
    con.close()

  def updcheck():
    con = connect()
    db = con.cursor()
    db.execute("SELECT uid, balance FROM 'users' WHERE balance >= 1")
    con.commit()
    val = db.fetchall()
    con.close()
    for i in val:
      print(i)
      user_id = i[0]
      balance = int(i[1])
      balance = int(balance)
      user.update(user_id, 'balance', balance)
    print("STOP")    

  class ref:

    def get(ref_id):
      con = connect()
      db = con.cursor()
      db.execute(f"SELECT uid FROM 'users' WHERE ref_id = '{ref_id}'")
      val = db.fetchone()[0]
      con.commit()
      con.close()
      return val

    def check(ref_id):
      con = connect()
      db = con.cursor()
      db.execute(f"SELECT id FROM 'users' WHERE ref_id = '{ref_id}'")
      val = db.fetchone()
      con.commit()
      con.close()
      if val is None:
        return False
      else:
        return True

    def clear():
      con = connect()
      db = con.cursor()
      db.execute("UPDATE 'users' SET ref_id = 'None'")
      con.commit()
      con.close()


class games:

  def create():
    con = connect()
    db = con.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS 'games'
			(id INTEGER PRIMARY KEY AUTOINCREMENT,
			uid INTEGER,
			json TEXT DEFAULT "{}")
			""")
    con.commit()
    con.close()

  def add(gameID, val):
    con = connect()
    db = con.cursor()
    db.execute(f"INSERT INTO 'games' (uid, json) VALUES ({gameID}, \"{val}\")")
    con.commit()
    con.close()

  def remove(gameID):
    con = connect()
    db = con.cursor()
    db.execute(f"DELETE FROM 'games' WHERE uid = {gameID}")
    con.commit()
    con.close()

  def bet(gameID, val):
    con = connect()
    db = con.cursor()
    val = json.dumps(val)
    db.execute(f"UPDATE 'games' SET json = '{val}' WHERE uid = {gameID}")
    con.commit()
    con.close()

  def getBets(gameID):
    con = connect()
    db = con.cursor()
    db.execute(f"SELECT json FROM 'games' WHERE uid = {gameID}")
    val = eval(db.fetchone()[0])
    con.commit()
    con.close()
    return val

  def check(gameID):
    con = connect()
    db = con.cursor()
    db.execute(f"SELECT id FROM 'games' WHERE uid = {gameID}")
    val = db.fetchone()
    con.commit()
    con.close()
    if val is None:
      return False
    else:
      return True

  def get():
    con = connect()
    db = con.cursor()
    db.execute(f"SELECT * FROM 'games'")
    val = db.fetchall()
    con.commit()
    con.close()
    return val

  class users:

    def get_num_bets(gameID, user_id):
      con = connect()
      db = con.cursor()
      db.execute(f"SELECT json FROM 'games' WHERE uid = {gameID}")
      val = eval(db.fetchone()[0])['bets']
      con.commit()
      con.close()
      num_sectors_count = 0
      for i in val:
        if i['user_id'] == user_id:
          if i['select'] in numbers:
            num_sectors_count += 1
      return num_sectors_count

class promocodes:

  def create():
    con = connect()
    db = con.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS 'promocodes'
			(id INTEGER PRIMARY KEY AUTOINCREMENT,
			owner INTEGER,
			promocode TEXT,
			activations INTEGER,
			content INTEGER,
			users_activated TEXT DEFAULT "[]")
			""")
    con.commit()
    con.close()

  def add(promo, user_id, acti, content, users):
    con = connect()
    db = con.cursor()
    users = json.dumps(users)
    db.execute(
      f"INSERT INTO 'promocodes' (promocode, owner, activations, content, users_activated) VALUES ('{promo}', {user_id}, {acti}, {content}, '{users}')"
    )
    con.commit()
    con.close()

  def update(promo, activations, users_activated):
    con = connect()
    db = con.cursor()
    users_activated = json.dumps(users_activated)
    db.execute(
      f"UPDATE 'promocodes' SET activations = {activations}, users_activated = '{users_activated}' WHERE promocode = '{promo}'"
    )
    con.commit()
    con.close()

  def remove(promo):
    con = connect()
    db = con.cursor()
    db.execute(f"DELETE FROM 'promocodes' WHERE promocode = '{promo}'")
    con.commit()
    con.close()

  def get(promo):
    con = connect()
    db = con.cursor()
    db.execute(f"SELECT * FROM 'promocodes' WHERE promocode = '{promo}'")
    val = db.fetchall()
    con.commit()
    con.close()
    return val

  def getvkid(user_id):
    con = connect()
    db = con.cursor()
    db.execute(f"SELECT * FROM 'promocodes' WHERE owner = {user_id}")
    val = db.fetchall()
    con.commit()
    con.close()
    return val


class bonus:

  def create():
    con = connect()
    db = con.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS 'bonuses'
			(id INTEGER PRIMARY KEY AUTOINCREMENT,
			post_id INTEGER,
			bonus INTEGER,
			start_time INTEGER,
			end_time INTEGER,
			users_reposted TEXT DEFAULT "[]")""")
    con.commit()
    con.close()

  def add(post_id, bonus, st, et):
    con = connect()
    db = con.cursor()
    db.execute(
      f"INSERT INTO 'bonuses' (post_id, bonus, start_time, end_time) VALUES ({post_id}, {bonus}, {st}, {et})"
    )
    con.commit()
    con.close()

  def update(post_id, ur):
    con = connect()
    db = con.cursor()
    ur = json.dumps(ur)
    db.execute(
      f"UPDATE 'bonuses' SET users_reposted = '{ur}' WHERE post_id = {post_id}"
    )
    con.commit()
    con.close()

  def get(post_id):
    con = connect()
    db = con.cursor()
    db.execute(f"SELECT * FROM 'bonuses' WHERE post_id = {post_id}")
    val = db.fetchall()
    con.commit()
    con.close()
    return val

  def remove(post_id):
    con = connect()
    db = con.cursor()
    db.execute(f"DELETE FROM 'bonuses' WHERE post_id = {post_id}")
    con.commit()
    con.close()


class glob:

  def create():
    con = connect()
    db = con.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS 'globals'
			(id INTEGER PRIMARY KEY,
			last_top_day TEXT DEFAULT 0,
			last_top_week TEXT DEFAULT 0)""")
    con.commit()
    con.close()

  def add():
    con = connect()
    db = con.cursor()
    db.execute("INSERT INTO 'globals' (id) VALUES (1)")
    con.commit()
    con.close()

  def addVar(name):
    con = connect()
    db = con.cursor()
    db.execute(f"ALTER TABLE 'globals' ADD COLUMN {name} 'TEXT'")
    con.commit()
    con.close()

  def update(var, val):
    con = connect()
    db = con.cursor()
    db.execute(f"UPDATE 'globals' SET {var} = '{val}' WHERE id = 1")
    con.commit()
    con.close()

  def get(var=None):
    con = connect()
    db = con.cursor()
    if not var:
      db.execute("SELECT * FROM 'globals' WHERE id = 1")
      val = db.fetchall()
    else:
      db.execute(f"SELECT {var} FROM 'globals' WHERE id = 1")
      val = db.fetchone()[0]
    con.commit()
    con.close()
    return val

  def remove():
    con = connect()
    db = con.cursor()
    db.execute(f"DELETE FROM 'globals' WHERE id = 1")
    con.commit()
    con.close()