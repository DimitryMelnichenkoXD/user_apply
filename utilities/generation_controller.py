import itertools
import random

from generator.image_generator import ImageGenerator


class GenerationController:

    def __init__(self):
        self.generator = ImageGenerator()

    def image_generate(self, elements_index: list = None, negative: bool = False):
        elements_index = self.generate_combination() if not elements_index else elements_index
        image = self.generator.image_generate(elements_index, negative)
        return image

    def generate_combination(self):
        pe = [len(p.elements) for p in self.generator.positions]
        e_range = [range(pe[0]), range(pe[1]), range(pe[2]), range(pe[3]), range(pe[4]), range(pe[5]), range(pe[6])]
        iteration = [e for e in itertools.product(*e_range)]
        random_iteration_elements = random.sample(iteration, 1)
        return random_iteration_elements[0]
