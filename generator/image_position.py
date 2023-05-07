class ImagePosition:
    position_cord = {
        1: [2000, 2000],
        2: [2000, 2000],
        3: [2000, 1250],
        4: [2000, 1780],
        5: [2000, 2180],
        6: [2000, 2800],
        7: [2000, 3652]
    }

    def __init__(self, position_number):
        self.position_number = position_number
        self.x_cord, self.y_cord = self.position_cord.get(position_number)
        self.elements = []

    def count_position_cord(self, element_size: list):
        width, height = element_size
        x = self.x_cord - width // 2
        y = self.y_cord - height // 2
        return x, y
