import svgwrite
from math import sqrt

def create_shield_svg(filename):
    golden_ratio = (1 + sqrt(5)) / 2
    width, height = 100, 100 * golden_ratio

    dwg = svgwrite.Drawing(filename, profile='tiny', size=(width, height))

    # Create a black shield shape
    shield_points = [
        (width / 2, 10),
        (10, 10 + (height - 20) / golden_ratio),
        (10, height - 10),
        (width - 10, height - 10),
        (width - 10, 10 + (height - 20) / golden_ratio),
    ]
    dwg.add(dwg.polygon(shield_points, fill='black'))

    # Save the SVG
    dwg.save()

create_shield_svg('shield_icon.svg')
