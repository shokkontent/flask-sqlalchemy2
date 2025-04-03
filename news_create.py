import datetime
from data import db_session
from data.news import News
from data.users import User

db_session.global_init("db/blogs.db")
db_sess = db_session.create_session()

news = News(title="Первая новость", content="Привет блог!",
            user_id=1, is_private=False)
db_sess.add(news)
db_sess.commit()

news = News(title="Вторая новость", content="Привет блог!",
            user_id=2, is_private=True)
db_sess.add(news)
db_sess.commit()

news = News(title="Третья новость", content="Привет блог!",
            user_id=3, is_private=False)
db_sess.add(news)
db_sess.commit()
'''user = db_sess.query(User).filter(User.id == 1).first()
news = News(title="Личная запись", content="Эта запись личная",
            is_private=True)
user.news.append(news)
db_sess.commit()
for news in user.news:
    print(news)'''

