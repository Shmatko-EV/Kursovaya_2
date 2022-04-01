from flask import Blueprint, jsonify

from utils import get_posts_all, get_post_by_pk

api_bp = Blueprint('api', __name__)


@api_bp.route('/posts')
def get_posts():
    ''' Возвращает вывод данных постов в виде JSON-списка по адресу /api/posts '''

    posts = get_posts_all()

    return jsonify(posts)


@api_bp.route('/posts/<int:postid>')
def get_post_by_id(postid):
    ''' Возвращает вывод данных поста в виде JSON-списка по адресу /api/posts '''

    post = get_post_by_pk(postid)

    if post is None:
        return {'error': 'Пост не найден'}, 404

    return jsonify(post)
