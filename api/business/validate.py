from ..blueprints.default import author, publisher
from ..utils.file import convert_to_text
from datetime import date, datetime


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
        'publisher': request.form.get('publisher'),
        'author': request.form.get('author'),
        'tags': request.form.getlist('tags[]'),
        'contents': None,
        'file': file.filename,
        'published_at': published_at,
        'imported_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print(data)

    if not data.get('publisher'):
        raise TypeError('The field publisher is required')
    if not data.get('author'):
        raise TypeError('The field author is required')
    if not file:
        raise TypeError('The field file is required')

    data['author'] = author(data['author'])
    data['publisher'] = publisher(data['publisher'])

    if not data['publisher']:
        raise TypeError('Invalid publisher')
    if not data['author']:
        raise TypeError('Invalid author')

    data['contents'] = convert_to_text(file)
    return data
