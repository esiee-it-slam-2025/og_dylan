import json
from PIL import Image, ImageDraw, ImageFont


# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  DATAS AND VARIABLES
# ****************************************************************************************************************************************************************

# Loading data from JSON files
events = json.load(open('events.json', 'r', encoding="utf-8"))
stadiums = json.load(open('stadiums.json', 'r', encoding="utf-8"))
tickets = json.load(open('tickets.json', 'r', encoding="utf-8"))

# Loading font types
font36 = ImageFont.truetype('fonts/Paris2024.ttf', 36, encoding="utf-8") 
font22 = ImageFont.truetype('fonts/Paris2024.ttf', 22, encoding="utf-8")

# Defining colors
blue = (51, 19, 104)
white = (255, 255, 255)

# Predefined placement of elements in the ticket
ticket_placement = {
    "HomeT": (37, 426),
    "AwayT": (112, 503),
    "Stadium": (60, 588),
    "Date": (60, 656),  
    "Category": (20, 756),
    "Seat": (200, 756),  
    "Price": (325, 756),
    "QRCode": (126, 835)
}