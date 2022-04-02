from flask import Blueprint, render_template, request

from utils import get_posts_all, get_post_by_pk, search_for_posts, get_posts_by_user, get_comments_by_post_id, \
    get_posts_by_tag

main_blueprint = Blueprint('main_bp', __name__, template_folder='templates')


@main_blueprint.route("/")
def page_index():
    ''' Реализует просмотр ленты всех постов '''

    posts = get_posts_all()

    return render_template('index.html', posts=posts)


@main_blueprint.route("/posts/<int:postid>")
def page_post(postid):
    ''' Реализует просмотр одного поста по post_id '''

    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)

    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route("/search/")
def page_search_posts_by_key_word():
    ''' Реализует вывод всех постов по ключевому слову поиска '''

    s = request.args.get('s', "")

    posts = search_for_posts(s)

    return render_template('search.html', s=s, posts=posts)


@main_blueprint.route("/users/<username>")
def page_posts_by_username(username):
    ''' Реализует вывод всех постов конкретного пользователя по имени '''

    posts_user = get_posts_by_user(username)

    return render_template('user-feed.html', posts_user=posts_user, username=username)


@main_blueprint.route("/tags/<string:tag>")
def page_posts_by_tag(tag):
    ''' Реализует вывод всех постов конкретного пользователя по имени '''

    posts = get_posts_by_tag(tag)

    return render_template('search.html', posts=posts, s=tag)
