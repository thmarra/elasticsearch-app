import textract

text = textract.process("/home/cpmarra/Downloads/conta_sabesp_1312.jpg")
print(text.decode('utf-8'))
