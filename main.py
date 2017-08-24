import sys
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

from physical_sizes import *

if len(sys.argv) <= 1 or sys.argv[1] == "Standard":
    CARD_HEIGHT = STANDARD[0]
    CARD_WIDTH = STANDARD[1]
else:
    print("Unsupported")
    quit()

CARD_COLOR = "darkred"
CARD_HEADER_HEIGHT = 100
CARD_IMAGE_AREA_HEIGHT = 400
IMAGE_HEIGHT = CARD_IMAGE_AREA_HEIGHT - 200
IMAGE_WIDTH = CARD_WIDTH - 200
CARD_DESCRIPTION = "This is a good cat. Lorum Ipsum"
CARD_VALUE_LEFT = 12
CARD_VALUE_RIGHT = 11
TITLE = "Card Title"
CARD_DESCRIPTION_MARGIN = 50
CARD_CORNER_VALUE_MARGIN = 50

source_img = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), "white")
draw = ImageDraw.Draw(source_img)
draw.rectangle(((0, 0), (CARD_WIDTH, CARD_HEADER_HEIGHT )), fill=CARD_COLOR)   # Bacjground Color
draw.rectangle(((0, CARD_HEADER_HEIGHT + CARD_IMAGE_AREA_HEIGHT), (CARD_WIDTH, CARD_HEIGHT )), fill=CARD_COLOR)   # Bacjground Color

font = ImageFont.truetype("itisdefinetlypossible.ttf", 32)
TITLE_LOCATION_X = (CARD_WIDTH / 2) - (font.getsize(TITLE)[0]/2) - 1
draw.text((TITLE_LOCATION_X, 30), TITLE, font=font)

draw.text((50, 50), str(CARD_VALUE_LEFT), font=font)
draw.text((CARD_WIDTH - CARD_CORNER_VALUE_MARGIN, CARD_CORNER_VALUE_MARGIN), str(CARD_VALUE_RIGHT), font=font)
draw.text((100, CARD_HEADER_HEIGHT + CARD_IMAGE_AREA_HEIGHT + CARD_DESCRIPTION_MARGIN), CARD_DESCRIPTION, font=font)


img = Image.open('test2.jpg', 'r')
img_w, img_h = img.size
offset = ((CARD_WIDTH - img_w)/ 2, CARD_HEADER_HEIGHT + 100 )
source_img.paste(img, offset)


source_img.save("out.png", "PNG")
