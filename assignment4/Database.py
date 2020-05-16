import sqlite3
from sqlite3 import Error
import time


class Database:
    def __init__(self):
        self.conn = self.connect("temporary.db")
        self.curs = self.conn.cursor()

    @property
    def conn(self):
        return self._conn

    @conn.setter
    def conn(self, value):
        self._conn = value

    @property
    def curs(self):
        return self._curs

    @curs.setter
    def curs(self, value):
        self._curs = value

    def connect(self, db_address):  # connect to database
        print("connecting to db...")

        try:
            connection = sqlite3.connect(db_address)
            print("connected to sqlite @ " + str(db_address))
        except Error as err:
            raise Exception("ERROR connecting to DB: " + str(err))  # return error if can't connect

        return connection

    def check_article_input(self, author, title, body):  # check if the article input is valid
        if type(author) == str:  # check if author is valid
            if 100 > len(author) > 0:
                author_is_valid = True
            else:
                author_is_valid = False
        else:
            author_is_valid = False

        if type(title) == str:  # check if title is valid
            if 50 > len(title) > 0:
                title_is_valid = True
            else:
                title_is_valid = False
        else:
            title_is_valid = False

        if type(body) == str:  # check if article body is valid
            if 1000 > len(body) > 0:
                body_is_valid = True
            else:
                body_is_valid = False
        else:
            body_is_valid = False

        if author_is_valid and title_is_valid and body_is_valid:  # return the final validity result
            return True
        else:
            return False

    def check_comment_input(self, email, body):  # check if the comment input is valid
        if type(email) == str:  # check if email is valid
            if 50 > len(email) > 0:
                email_is_valid = True
            else:
                email_is_valid = False
        else:
            email_is_valid = False

        if type(body) == str:  # check if comment body is valid
            if 100 > len(body) > 0:
                body_is_valid = True
            else:
                body_is_valid = False
        else:
            body_is_valid = False

        if email_is_valid and body_is_valid:  # return the final validity result
            return True
        else:
            return False

    def create_article_table(self):  # create the article table
        print("creating article table...")
        self.curs.execute(
            '''CREATE TABLE articles (
                article_id INTEGER PRIMARY KEY, 
                author TEXT, 
                title TEXT, 
                body TEXT, 
                timestamp INTEGER
            )'''
        )

    def create_comment_table(self):  # create the comment table
        print("creating comments table...")
        self.curs.execute(
            '''CREATE TABLE comments (
                comment_id INTEGER PRIMARY KEY,
                email TEXT,
                body TEXT,
                timestamp,
                article_id,
                FOREIGN KEY (article_id)
                    REFERENCES articles (article_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
            )'''
        )

    def article_id_exists(self, article_id):  # check if an article exists by id
        self.curs.execute("SELECT * FROM articles WHERE article_id = ?", (article_id,))
        if len(self.curs.fetchall()) == 0:
            return False  # no article with the given id exists
        else:
            return True  # article exists

    def add_new_article(self, author, title, body):  # add new article to database
        timestamp = round(time.time())

        if self.check_article_input(author, title, body):  # if input is valid add article to database
            self.curs.execute('''INSERT INTO articles (article_id, author, title, body, timestamp) 
                            VALUES (NULL, ?, ?, ?, ?)''', (author, title, body, timestamp))
            self.conn.commit()
            print("saved article to database")
        else:
            print("input is not valid please try again")

    def add_new_comment(self, email, body, article_id):  # add new comment to database
        timestamp = round(time.time())

        if self.check_comment_input(email, body):  # if input is valid add comment to database
            if self.article_id_exists(article_id):  # check if article exists
                self.curs.execute('''INSERT INTO comments (comment_id, email, body, timestamp, article_id) 
                             VALUES (NULL, ?, ?, ?, ?)''', (email, body, timestamp, article_id))
                self.conn.commit()
                print("saved comment to database")
            else:
                print("return cannot add comment, no article exists")  # article to add does not exist
        else:
            print("return input is not valid")

    def get_article_by_id(self, article_id):  # get article by id
        if self.article_id_exists(article_id):  # check if article with given id exists
            self.curs.execute("SELECT * FROM articles WHERE article_id = ?", (article_id,))
            return self.curs.fetchone()  # return found article
        else:
            return "article not found"

    def get_all_article_comments(self, article_id):  # get comments of an article by article id
        if self.article_id_exists(article_id):  # check if the article with given id exists
            self.curs.execute("SELECT * FROM comments WHERE article_id = ?", (article_id,))
            return self.curs.fetchall()  # return all found comments
        else:
            print("article not found")

    def get_all_articles(self):  # get all articles from the database
        if self.check_article_table_exists():  # check if the article table exists
            self.curs.execute("SELECT * FROM articles")
            return self.curs.fetchall()  # return all found articles

    def check_article_table_exists(self):  # check if the article table exists
        self.curs.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='articles' ''')

        if self.curs.fetchone()[0] == 1:
            return True  # table exists
        else:
            return False  # table does not exist

    def check_comments_table_exists(self):  # check if the article table exists
        self.curs.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='comments' ''')

        if self.curs.fetchone()[0] == 1:
            return True  # table exists
        else:
            return False  # table does not exist

    def start_database(self):  # start the database
        if not self.check_article_table_exists():  # check if the article table exists
            self.create_article_table()  # call create the article table

        if not self.check_comments_table_exists():  # check if the comment table exists
            self.create_comment_table()  # call create the comments table

    def delete_all_articles(self):  # delete all articles
        if self.check_article_table_exists():  # check if the article table exists
            self.curs.execute("DELETE FROM articles")
            self.conn.commit()
            return "deleted all articles"

    def delete_article_by_id(self, article_id):  # delete article by id
        if self.check_article_table_exists() and self.article_id_exists(article_id):  # check if article exists
            self.curs.execute(" DELETE FROM articles WHERE article_id = ?", (article_id,))
            self.conn.commit()

    def modify_article_by_id(self, article_id, new_author, new_title, new_body):  # modify article by id
        timestamp = repr(round(time.time()))
        new_author = repr(new_author)  # escape the input string
        new_title = repr(new_title)  # escape the input string
        new_body = repr(new_body)  # escape the input string

        if self.check_article_table_exists() and self.article_id_exists(article_id):  # check if article exists
            self.curs.execute("UPDATE articles SET author={0}, title={1}, body={2}, timestamp={3} WHERE article_id=1"
                              .format(new_author, new_title, new_body, timestamp))
            self.conn.commit()
        else:
            return "return article not found"

    def database_main(self):
        self.start_database()
        # self.add_new_article("nOnE", "js rules", "need to justify why?")
        # add_new_comment("NoNemail", "subj js rules", 1)

        # add_new_article("nada", "ts for the win", "for real, it rocks")
        # add_new_article("ola", "interface in your face", "with inheritance")


# database_main()

# get all articles from db (helper)
# print("fetching articles")
# curs.execute("SELECT * FROM articles")
# print(curs.fetchall())

# get all comments from db
# print("fetching comments")
# curs.execute("SELECT * FROM comments")
# print(curs.fetchall())


# remove article table (helper)
# print("removing table")
# curs.execute("DROP TABLE articles")


# get by query (helper)
# print("getting by query")
# curs.execute("SELECT * FROM articles WHERE article_id = 4")
# print(len(curs.fetchall()))
