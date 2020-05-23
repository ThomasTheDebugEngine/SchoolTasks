from bottle import get, post, delete, put, run, template, request
from datetime import datetime
from SchoolTasks.assignment4.Database import Database  # change tis accordingly to your file structure

db = Database()  # initialise database 
db.database_main()  # start the database

usr_input = input("is this for testing task 2 ? [y]es or [n]o: ")

if usr_input == "y":  # task 2, (adding 3 articles and 3 comments to each article
    db.delete_all_articles()

    db.add_new_article("author1", "title1", "body1")
    db.add_new_comment("comment_email11", "comment_body11", 1)
    db.add_new_comment("comment_email11", "comment_body12", 1)
    db.add_new_comment("comment_email11", "comment_body13", 1)

    db.add_new_article("author2", "title2", "body2")
    db.add_new_comment("comment_email11", "comment_body21", 2)
    db.add_new_comment("comment_email11", "comment_body22", 2)
    db.add_new_comment("comment_email11", "comment_body23", 2)

    db.add_new_article("author3", "title3", "body3")
    db.add_new_comment("comment_email11", "comment_body31", 3)
    db.add_new_comment("comment_email11", "comment_body32", 3)
    db.add_new_comment("comment_email11", "comment_body33", 3)


@get("/articles")
def all_articles():  # get all articles
    articles_list = db.get_all_articles()  # get all articles form database
    authors_list = []
    title_list = []
    body_list = []
    times_list = []

    for article in articles_list:  # save articles into list
        print(article)
        authors_list.append(article[1])
        title_list.append(article[2])
        body_list.append(article[3])
        times_list.append(unix_to_date(article[4]))

    if len(articles_list) <= 0:
        return template("not_found_template")  # return not found template
    else:
        all_articles_dict = {
            "mode": "all articles",
            "articles_list_length": len(articles_list),
            "authors_list": authors_list,
            "title_list": title_list,
            "times_list": times_list
        }

        return template("all_article_template", **all_articles_dict)  # return template


@get("/articles/<article_id:int>")
def article_by_id(article_id):  # get article by id
    article = db.get_article_by_id(article_id)  # get article by id from database

    if type(article) == str:  # check if the requested article exists
        return template("not_found_template")  # return not found template
    else:
        single_article_dict = {  # store the variables for rendering
            "mode": "single article",
            "article_author": article[1],
            "article_title": article[2],
            "article_body": article[3],
            "article_date": unix_to_date(article[4])
        }

        return template("single_article_template", **single_article_dict)  # return template


@get("/articles/<article_id:int>/comments")
def get_article_comment(article_id):
    article = db.get_article_by_id(article_id)  # get article by id from database
    comments_list = db.get_all_article_comments(article_id)  # get comments from database

    if db.get_article_by_id(article_id) == "article not found":  # check if article exists
        return template("not_found_template")  # return not found template
    else:
        if len(comments_list) == 0:  # check the length of the comments list
            return template("not_found_template")  # return not found template
        else:
            comment_email_list = []
            comment_body_list = []
            comment_time_list = []

            for comment in comments_list:  # save comments into list
                comment_email_list.append(comment[1])
                comment_body_list.append(comment[2])
                comment_time_list.append(unix_to_date(comment[3]))

            if type(article) == str:  # check if the requested article exists
                return template("not_found_template")  # return not found template
            else:
                comment_article_dict = {  # store the variables for rendering
                    "mode": "article comments",
                    "article_author": article[1],
                    "article_title": article[2],
                    "article_date": unix_to_date(article[4]),
                    "comment_list_length": len(comments_list),
                    "comment_email_list": comment_email_list,
                    "comment_body_list": comment_body_list,
                    "comment_time_list": comment_time_list
                }

                return template("article_with_comments_template", **comment_article_dict)  # return template


@post("/article")
def post_new_article():  # post a new article
    author = request.json.get("author")  # get information from request body
    title = request.json.get("title")
    body = request.json.get("body")

    if check_input(author, title, body):  # check if input is valid
        db.add_new_article(author, title, body)  # add article to database
        return {"action": "POST", "author": author, "title": title, "body": body}  # return article information
    else:
        return "parameters were not valid please try again"  # return not valid message


@delete("/article/<article_id:int>")
def delete_article_by_id(article_id):  # delete article by id
    if type(article_id) == int:  # check if id is integer
        if article_id >= 0:  # check if article id is positive
            article = db.get_article_by_id(article_id)  # get article information from database
            db.delete_article_by_id(article_id)  # delete article from database
            return {"action": "DELETE", "author": article[1], "title": article[2], "body": article[3]}  # send response
        else:
            return "parameters were not valid please try again"  # return not valid message
    else:
        return "parameters were not valid please try again"  # return not valid message


@put("/article/<article_id:int>")
def modify_article_by_id(article_id):
    new_author = request.json.get("author")
    new_title = request.json.get("title")
    new_body = request.json.get("body")

    if check_input(new_author, new_title, new_body):  # check if input is valid
        if type(article_id) == int:  # check if id is integer
            if article_id >= 0:  # check if article id is positive
                db.modify_article_by_id(article_id, new_author, new_title, new_body)
                return {"action": "PUT", "author": new_author, "title": new_title, "body": new_body}
            else:
                return "parameters were not valid please try again"  # return not valid message
        else:
            return "parameters were not valid please try again"  # return not valid message
    else:
        return "parameters were not valid please try again"  # return not valid message


def check_input(author, title, body):  # validate input
    author_is_valid = False
    title_is_valid = False
    body_is_valid = False

    if type(author) == str and type(title) == str and type(body) == str:  # check if input is string
        if len(author) >= 0 and len(title) >= 0 and len(body) >= 0:  # check if input is empty
            author_is_valid = True
            title_is_valid = True
            body_is_valid = True

    if author_is_valid and title_is_valid and body_is_valid:  # check if all input is valid
        return True  # input is valid
    else:
        return False  # input is not valid


def unix_to_date(timestamp):  # convert unix timestamp to date
    if type(timestamp) == int:  # check if the date is integer
        return str(datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))  # convert date
    else:
        return 0


run(host='localhost', port=3030)
