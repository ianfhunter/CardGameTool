
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

from physical_sizes import *
from card_layout import *

CARD_DESCRIPTION = "This is a good cat. Lorum Ipsum"
CARD_DESCRIPTION_2 = "Global Effect: Aww"
CARD_VALUE_LEFT = 12
CARD_VALUE_RIGHT = 11
TITLE = "Card Title"

source_img = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), "white")
draw = ImageDraw.Draw(source_img)
draw.rectangle(((0, 0), (CARD_WIDTH, CARD_HEADER_HEIGHT )), fill=CARD_COLOR)   # Bacjground Color
draw.rectangle(((0, CARD_HEADER_HEIGHT + CARD_IMAGE_AREA_HEIGHT), (CARD_WIDTH, CARD_HEIGHT )), fill=CARD_COLOR)   # Background Color

font = ImageFont.truetype(FONT, FONT_SIZE)
TITLE_LOCATION_X = (CARD_WIDTH / 2) - (font.getsize(TITLE)[0]/2) - 1
draw.text((TITLE_LOCATION_X, TITLE_OFFSET), TITLE, font=font)

draw.text((CARD_CORNER_VALUE_MARGIN, CARD_CORNER_VALUE_MARGIN), str(CARD_VALUE_LEFT), font=font)
draw.text((CARD_WIDTH - CARD_CORNER_VALUE_MARGIN, CARD_CORNER_VALUE_MARGIN), str(CARD_VALUE_RIGHT), font=font)
draw.text((CARD_DESCRIPTION_INSERT, CARD_HEADER_HEIGHT + CARD_IMAGE_AREA_HEIGHT + CARD_DESCRIPTION_MARGIN), CARD_DESCRIPTION, font=font)

draw.text((CARD_DESCRIPTION_INSERT, CARD_HEADER_HEIGHT + CARD_IMAGE_AREA_HEIGHT + CARD_DESCRIPTION_MARGIN + CARD_DESCRIPTION_HEIGHT), CARD_DESCRIPTION_2, font=font)

img = Image.open('test2.jpg', 'r')
img_w, img_h = img.size
offset = ((CARD_WIDTH - img_w)/ 2, CARD_HEADER_HEIGHT + 100 )
source_img.paste(img, offset)


source_img.save("out.png", "PNG")
