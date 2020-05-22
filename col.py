import math


def get_color_name(rgb):
    color = {"Red": [255, 0, 0],
             "Orange": [255, 127, 0],
             "Yellow": [255, 255, 0],
             "Green": [0, 255, 0],
             "Cyan": [0, 255, 255],
             "Blue": [0, 0, 255],
             "Violet": [127, 0, 255],
             "Brown": [165, 42, 42],
             "Black": [0, 0, 0],
             "Grey": [127, 127, 127],
             "White": [255, 255, 255],
             }

    res = "Red"
    mind = math.sqrt(math.pow(abs(rgb[0] - color["Red"][0]), 2) + math.pow(abs(rgb[1] - color["Red"][1]), 2) + math.pow(
        abs(rgb[2] - color["Red"][2]), 2))
    for c, x in color.items():
        dis = math.sqrt(
            math.pow(abs(rgb[0] - x[0]), 2) + math.pow(abs(rgb[1] - x[1]), 2) + math.pow(abs(rgb[2] - x[2]), 2))
        if dis < mind:
            mind = dis
            res = c
    return res


print(get_color_name([248, 149, 130]))
