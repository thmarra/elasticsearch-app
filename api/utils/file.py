from .settings import config
import os
import PyPDF2


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


def convert_to_text(file):
    # Returns the text of given binary file
    reader = PyPDF2.PdfFileReader(file)
    count = reader.numPages
    contents = ""
    for i in range(count):
        page = reader.getPage(i)
        contents = contents + "\n" + page.extractText()
    return contents
