from PIL import Image
from os.path import exists
import shutil


def isMultiple(num, check_with):
    return num % check_with == 0;


a = 300

for x in range(a):

    if x == 0:
        shutil.copyfile(f'test/test_{x}.png', "test/merged_image.png")

    elif x % 13 != 0:

        print(x)
        if exists('test/merged_image.png'):
            image1 = Image.open('test/merged_image.png')
            try:
                image2 = Image.open(f'test/test_{x}.png')
            except FileNotFoundError:
                break

            new_image = Image.new('RGB', (image1.size[0], image2.size[1] + image1.size[1]), (250, 250, 250))
            new_image.paste(image1, (0, 0))
            new_image.paste(image2, (0, image1.size[1]))
            new_image.save("test/merged_image.png", "PNG")
        else:
            shutil.copyfile(f'test/test_{x}.png', "test/merged_image.png")
    else:
        if exists('test/merged_image_length.png'):
            image1 = Image.open('test/merged_image_length.png')
            image2 = Image.open('test/merged_image.png')
            new_image = Image.new('RGB', (image2.size[0] + image1.size[0], image1.size[1]), (250, 250, 250))
            new_image.paste(image1, (0, 0))
            new_image.paste(image2, (image1.size[0], 0))
            new_image.save("test/merged_image_length.png", "PNG")
        else:
            shutil.copyfile('test/merged_image.png', 'test/merged_image_length.png')

        shutil.copyfile(f'test/test_{x}.png', "test/merged_image.png")


