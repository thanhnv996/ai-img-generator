# import required module
import os
import random

ROOT_DIR = '.'
URL = 'https://raw.githubusercontent.com/thanhnv996/ai-img-generator/main'
# GENERATE_CATEGORIES = ['jungle', 'flower', 'bird']
GENERATE_CATEGORIES = ['Nature _Landscapes', 'Nature _Landscapes']
# GENERATE_CATEGORIES = ['jungle', 'flower', 'bird', ]
# GENERATE_CATEGORIES = ['jungle', 'jungle', 'flower', ]
# GENERATE_CATEGORIES = ['jungle', 'flower', 'jungle', ]
# GENERATE_CATEGORIES = ['jungle', 'jungle', ]
# GENERATE_CATEGORIES = ['bird', 'nature', ]
# GENERATE_CATEGORIES = ['bird', 'flower', ]
# GENERATE_CATEGORIES = ['bird', 'jungle', 'flower', ]
# GENERATE_CATEGORIES = ['bird', 'flower']
# GENERATE_CATEGORIES = ['jungle', 'flower']
NUMBER_OUTPUT_COMMAND = 10
# --chaos accepts values 0–100.
# The default --chaos value is 0.
# Sự khác nhau của 4 hình ảnh tạo ra
CHAOS = 40
# --weird accepts values: 0–3000.
# The default --weird value is 0.
# Sự sáng tạo so với ảnh gốc
WEIRD = 300
STR_JOIN = ' '
# STR_JOIN = ':: '


category_dict = {}
image_links = []
for subdir, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        file_path = os.path.join(subdir, file)
        if os.path.isfile(file_path) and '.py' not in file_path:
            category = file_path.split("\\")[-2]
            # print(category)
            link = f'{URL}/{category}/{file}'
            if category not in category_dict:
                category_dict[category] = []
                image_links.append(None)
            category_dict[category].append(link)

index = 0
for category in category_dict:
    image_links[index] = category_dict[category]
    index += 1

imagines = []
image_links_1 = category_dict[GENERATE_CATEGORIES[0]]
# image_links_2 = category_dict[GENERATE_CATEGORIES[1]]
# for image_link_1 in image_links_1:
#     image_link_2 = random.choice(image_links_2)
#     imagine = f'/imagine {image_link_1} {image_link_2} --ar 16:9'
#     imagines.append(imagine)
#     print(imagine)

count = 0
imagine = '/imagine {'
random.shuffle(image_links_1)
for image_link_1 in image_links_1:
    selected_image_links = []
    for category in GENERATE_CATEGORIES:
        category_image_links = category_dict[category]
        random_image_link = random.choice(category_image_links)
        selected_image_links.append(random_image_link)
    remix_image_link = STR_JOIN.join(selected_image_links)
    imagine += f'{remix_image_link}, '
    imagines.append(imagine)

    count += 1
    if count > (NUMBER_OUTPUT_COMMAND - 1):
        break

imagine = imagine[:-2]
imagine += '} --ar 16:9 --chaos ' + str(CHAOS) + ' --weird ' + str(WEIRD) + ' --style raw'
# imagine += '} lush green, light --ar 16:9 --chaos 10 --weird 200 --style raw'
print(imagine)

# print(imagines)
