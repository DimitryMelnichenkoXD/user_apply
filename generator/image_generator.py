import os
from typing import List

from PIL import Image, ImageOps

from generator.image_position import ImagePosition

image_path = "./base_image"


class ImageGenerator:

    def __init__(self) -> None:
        self.positions: List[ImagePosition] = self.create_positions()

    @staticmethod
    def create_positions():
        files = os.listdir(image_path)
        files_name = [file for file in files if file.endswith('.png')]
        positions = list(set([int(name.split(".")[0]) for name in files_name]))
        position_dict = {position: ImagePosition(position_number=position) for position in positions}
        for name in files_name:
            position = int(name.split(".")[0])
            image_position = position_dict.get(position)
            image_position.elements.append(Image.open(f"{image_path}/{name}"))
        position_list = [position for key, position in position_dict.items()]
        return position_list

    @staticmethod
    def invert_image(image, negative):
        image = image.convert('RGB')
        return ImageOps.invert(image) if negative else image

    @staticmethod
    def generate_background():
        return Image.new('RGBA', (4000, 4000), color=(255, 255, 255, 255))

    def image_generate(self, elements_index: list, negative: bool = False):
        background = self.generate_background()
        for position, element_index in zip(self.positions, elements_index):
            element = position.elements[element_index]
            element_cord = position.count_position_cord(element.size)
            background.alpha_composite(element, element_cord)
        background = self.invert_image(background, negative)
        return background
