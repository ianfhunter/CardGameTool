from physical_sizes import *
import sys

if len(sys.argv) <= 1 or sys.argv[1] == "Standard":
    CARD_HEIGHT, CARD_WIDTH=STANDARD
else:
    print("Unsupported")
    quit()

CARD_COLOR = "darkred"

CARD_HEADER_HEIGHT = 100
CARD_IMAGE_AREA_HEIGHT = 400
CARD_DESCRIPTION_MARGIN = 50
CARD_DESCRIPTION_HEIGHT = 300
CARD_DESCRIPTION_INSERT = 50

IMAGE_HEIGHT = CARD_IMAGE_AREA_HEIGHT - 200
IMAGE_WIDTH = CARD_WIDTH - 200

CARD_CORNER_VALUE_MARGIN = 50

TITLE_OFFSET = 30

FONT = "itisdefinetlypossible.ttf"
FONT_SIZE = 32
