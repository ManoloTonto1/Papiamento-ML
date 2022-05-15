import fitz  # this is pymupdf
import os
path = "./downloads"
text = ""
# for filename in os.listdir(path):
#     f = os.path.join(path, filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#         with fitz.open(f) as doc:
#             for page in doc:
#                 text += page.get_text()
#                 with open('data.txt', 'w',encoding="utf-8") as text_file:
#                     text_file.write(text)
                # print(text)

file = "./downloads/BNA-DIG-LAGO-DICTIONARY-1953.pdf"
with fitz.open(file) as doc:
    for page in doc:
        text += page.get_text()
        with open('papiamento_dictionar.txt', 'w',encoding="utf-8") as text_file:
            text_file.write(text)
    # print(text)

