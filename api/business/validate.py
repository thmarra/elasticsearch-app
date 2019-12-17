from ..blueprints.default import _AUTHORS, _PUBLISHERS
from ..utils.file import convert_to_text
from datetime import date, datetime


def is_valid_publisher(id):
    return any(x['id'] == id for x in _PUBLISHERS)


def is_valid_author(id):
    return any(x['id'] == id for x in _AUTHORS)


def is_valid_request_new_document(request):
    if 'file' not in request.files:
        raise TypeError('The field file is required')

    file = request.files['file']
    published_at = request.form.get('published_at')

    try:
        if published_at:
            datetime.strptime(published_at, "%Y-%m-%d %H:%M:%S")
        else:
            published_at = date.today().strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        raise TypeError('The field published_at is in the wrong format')

    data = {
        'publisher_id': request.form.get('publisher'),
        'author_id': request.form.get('author'),
        'tags': request.form.getlist('tags[]'),
        'contents': None,
        'file': file.filename,
        'published_at': published_at,
        'imported_at': date.today().strftime("%Y-%m-%d %H:%M:%S")
    }

    if not data.get('publisher_id'):
        raise TypeError('The field publisher is required')
    if not data.get('author_id'):
        raise TypeError('The field author is required')
    if not file:
        raise TypeError('The field file is required')
    if not is_valid_publisher(data.get('publisher_id')):
        raise TypeError('Invalid publisher')
    if not is_valid_author(data.get('author_id')):
        raise TypeError('Invalid author')

    data['contents'] = convert_to_text(file)
    return data
