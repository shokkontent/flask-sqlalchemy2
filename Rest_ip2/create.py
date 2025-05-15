import datetime

from data import db_session
from data.users import User


db_session.global_init('db/blogs.db')
db_sess = db_session.create_session()

'''user = User()
user.surname = "Scbfott"
user.name = "Ridbfley"
user.age = "21"
user.position = "captabfdin"
user.speciality = "researbdfch enbdfineer"
user.address = "mbdfodule_3"
user.email = "scobdtt_chbdief@marsbd.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()'''

user = User()
user.surname = "Scgfott"
user.name = "Ringdley"
user.age = "22"
user.position = "captabfin"
user.speciality = "resebfbarch bgenginbfeer"
user.address = "module_2"
user.email = "scottvfdvfdchief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = User()
user.surname = "Scotsst"
user.name = "Ridgfley"
user.age = "25"
user.position = "captbfin"
user.speciality = "researbfch engineer"
user.address = "module_3"
user.email = "scobftt_bfchiefbgf@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()


'''user = db_sess.query(User).filter(User.id == 1).first()
print(user)
user.name = "Пользователь 1"
user.created_date = datetime.datetime.now()
db_sess.commit()
users = db_sess.query(User).all()
for user in users:
    if user.address == "module_1":
        print(user)'''