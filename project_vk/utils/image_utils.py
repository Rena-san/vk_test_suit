from urllib.request import urlopen

from PIL import Image, ImageChops


class ImageUtils:

    @staticmethod
    def difference_images_from_file_url(path, url):
        img_1 = Image.open(path)
        img_2 = Image.open(urlopen(url))
        result = ImageChops.difference(img_1, img_2).getbbox()
        if result is None:
            return True
        return False
