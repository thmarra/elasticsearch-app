from .settings import config
import textract
import os

UPLOAD_FOLDER = config('IMAGE_FOLDER')
ALLOWED_IMAGES = ['png', 'jpg', 'jpeg']


def allowed_image(filename):
    # Verifies if file is a valid image
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGES


def save_file(file, filename):
    # Saves image to shared folder
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return True


def conver_to_text(filepath):
    # TODO arrumar o tratamento de tipo de arquivo
    if not filepath.endswith('.pdf'):
        return None
    # Returns the text of given file
    text = textract.process(filepath)
    return text.decode('utf-8')