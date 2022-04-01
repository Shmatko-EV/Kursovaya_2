import json

DATA_POSTS_FILE = 'data/posts.json'
DATA_COMMENTS_FILE = 'data/comments.json'

def get_data_from_file(data_file):
    ''' Возвращает данные из файла JSON '''

    with open(data_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_posts_all():
    '''Возвращает все посты из файла '''

    posts = get_data_from_file(DATA_POSTS_FILE)

    return posts


def get_posts_by_user(user_name):
    '''Возвращает посты определенного пользователя '''

    # Переменная, в которой все имеющиеся посты.
    posts = get_data_from_file(DATA_POSTS_FILE)

    # Создаем список куда будем складывать посты определенного пользователя.
    user_posts = []

    # Добавляем все имеющиеся посты пользователя,
    # если имя есть в списке файла JSON.
    for post in posts:
        if user_name.lower() == post['poster_name']:
            user_posts.append(post)

    return user_posts


def get_comments_by_post_id(post_id):
    ''' Возвращает комментарии определенного поста '''

    # Читаем файл JSON с комментариями к постам.

    comments_for_posts = get_data_from_file(DATA_COMMENTS_FILE)

    # Создаем список куда будем складывать все комментарии к посту.
    comments_for_post_list = []

    # Добавляем все имеющиеся комментарии к посту,
    # если id запрошенного поста совпадает с id поста в списке комментариев.
    for comments in comments_for_posts:
        if post_id == comments['post_id']:
            comments_for_post_list.append(comments) # comments['comment']

    return comments_for_post_list


#print(get_comments_by_post_id(7))

def search_for_posts(query_word):
    ''' Возвращает список постов по ключевому слову '''

    # Переменная, в которой все имеющиеся посты.
    posts = get_data_from_file(DATA_POSTS_FILE)

    # Создаем список куда будем складывать посты по запрошенному слову.
    posts_by_query_word = []

    # Добавляем в список все имеющиеся посты по ключевому слову.
    for post in posts:
        if query_word.lower() in post['content'].lower():
            posts_by_query_word.append(post)

    return posts_by_query_word


def get_post_by_pk(pk):
    ''' Возвращает один пост по его идентификатору '''

    # Переменная, в которой все имеющиеся посты.
    posts = get_data_from_file(DATA_POSTS_FILE)

    found_post =None
    for post in posts:
        if pk == post['pk']:
            found_post = post
            break

    return found_post

