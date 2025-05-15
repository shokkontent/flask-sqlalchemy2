import datetime
from data import db_session
from data.Jobs import Jobs
from data.users import User

db_session.global_init("db/blogs.db")
db_sess = db_session.create_session()

news = Jobs(team_leader="1", job="deployment of residential modules 1 and 2",
            work_size=15, collaborators='2, 3', start_date=0, is_finished=False)
db_sess.add(news)
db_sess.commit()

news = Jobs(team_leader="2", job="System unit",
            work_size=15, collaborators='4, 3', start_date=0, is_finished=False)
db_sess.add(news)
db_sess.commit()

news = Jobs(team_leader="3", job="scientist",
            work_size=25, collaborators='5', start_date=0, is_finished=False)
db_sess.add(news)
db_sess.commit()
'''user = db_sess.query(User).filter(User.id == 1).first()
news = News(title="Личная запись", content="Эта запись личная",
            is_private=True)
user.news.append(news)
db_sess.commit()

for news in user.news:
    print(news)

name_db = input()
global_init(name_db)
db_sess = create_session()

users = db_sess.query(User).all()
users = db_sess.query(User).all()
for user in users:
    if user.address == "module_1" and user.age < 21:
        user.address = "module_3"
db_sess.commit()'''