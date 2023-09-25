import os
import secrets

paths = ['bird', 'flower', 'jungle', 'nature']

random_str = secrets.token_urlsafe(2)

for path in paths:
    files = os.listdir(path)

    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, ''.join([random_str + '-' + str(index), '.jpg'])))
