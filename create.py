import datetime

from data import db_session
from data.users import User


db_session.global_init("db/blogs.db")
db_sess = db_session.create_session()

user = User()
user.name = "Пользователь 1"
user.about = "биография пользователя 1"
user.email = "email@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.name = "Пользователь 2"
user.about = "биография пользователя 2"
user.email = "email2@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.name = "Пользователь 3"
user.about = "биография пользователя 3"
user.email = "email3@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

'''user = db_sess.query(User).filter(User.id == 1).first()
print(user)
user.name = "Пользователь 1"
user.created_date = datetime.datetime.now()
db_sess.commit()'''