from PIL import Image, ImageDraw

# Create a blank image with a white background
width, height = 100, 120
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw a black shield shape
shield_points = [
    (width // 2, 10),
    (10, 40),
    (10, height - 10),
    (width - 10, height - 10),
    (width - 10, 40),
]
draw.polygon(shield_points, fill="black")

# Save the image as an icon file
image.save("shield_icon.ico", "ICO")