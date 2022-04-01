from flask import Blueprint, render_template, request

from utils import get_posts_all, get_post_by_pk, search_for_posts, get_posts_by_user, get_comments_by_post_id

mane_blueprint = Blueprint('mane_blueprint', __name__, template_folder='templates')


@mane_blueprint.route("/")
def page_index():
    ''' Реализует просмотр ленты всех постов '''

    posts = get_posts_all()

    return render_template('index.html', posts=posts)


@mane_blueprint.route("/posts/<int:postid>")
def page_post(postid):
    ''' Реализует просмотр одного поста по post_id '''

    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    # Количество комментариев.
    len_comments = len(comments)

    return render_template('post.html', post=post, comments=comments, len_comments=len_comments)


@mane_blueprint.route("/search/")
def page_search_posts_by_key_word():
    ''' Реализует вывод всех постов по ключевому слову поиска '''

    s = request.args.get('s', "")

    posts = search_for_posts(s)

    # Количество постов по ключевому слову поиска.
    len_posts = len(posts)
    # Оставляем в списке найденных постов необходимое количество постов (10).
    # posts_range = []
    # if len_posts > 2:
    #    posts_range = posts[:2]

    return render_template('search.html', s=s, len_posts=len_posts, posts=posts)


@mane_blueprint.route("/users/<username>")
def page_posts_by_username(username):
    ''' Реализует вывод всех постов конкретного пользователя по имени '''

    posts_user = get_posts_by_user(username)

    return render_template('user-feed.html', posts_user=posts_user)
