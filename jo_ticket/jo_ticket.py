import locale, json, qrcode
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

locale.setlocale(locale.LC_TIME, "fr_FR")

events = json.load(open('events.json', 'r', encoding="utf-8"))
stadiums = json.load(open('stadiums.json', 'r', encoding="utf-8"))
tickets = json.load(open('tickets.json', 'r', encoding="utf-8"))

font36 = ImageFont.truetype('fonts/Paris2024.ttf', 36, encoding="utf-8")
font22 = ImageFont.truetype('fonts/Paris2024.ttf', 22, encoding="utf-8")

blue = (51, 19, 104)
white = (255, 255, 255)


ticket_placement = {
    "HomeT": (45, 430),
    "AwayT": (123, 505),
    "Stadium": (68, 590),
    "Date": (68, 657),
    "Category": (45, 761),
    "Seat": (212, 761),
    "Price": (328, 761),
    "QRCode": (133, 842)
}

def format_datetime(iso_datetime):
    dt = datetime.fromisoformat(iso_datetime)
    formatted_date = dt.strftime("%d/%m/%Y")
    formatted_time = dt.strftime("%H:%M")
    return formatted_date, formatted_time

i = 1
for ticket in tickets:
    event = next(filter(lambda x: x["id"] == ticket["event_id"], events), None)
    stadium = next(filter(lambda x: x["id"] == event["stadium_id"], stadiums), None)

    formatted_date, formatted_time = format_datetime(event["start"])

    seat = ticket["seat"]
    if seat == "free":
        seat = "Libre"

    with Image.open("ticketJO.png") as img:
        addDatas = ImageDraw.Draw(img)
        addDatas.text(ticket_placement["HomeT"], event["team_home"], fill=blue, font=font36)
        addDatas.text(ticket_placement["AwayT"], event["team_away"], fill=blue, font=font36)
        addDatas.text(ticket_placement["Stadium"], f"{stadium['name']} - {stadium['location']}", fill=white, font=font22)
        addDatas.text(ticket_placement["Date"], f"{formatted_date} à {formatted_time}", fill=white, font=font22)
        addDatas.text(ticket_placement["Category"], ticket["category"], fill=white, font=font22)
        addDatas.text(ticket_placement["Seat"], seat, fill=white, font=font22)
        addDatas.text(ticket_placement["Price"], f"{ticket['price']}{'€' if ticket['currency'] != 'USD' else '$'}", fill=white, font=font22)

        qr = qrcode.QRCode(box_size=4)
        qr.add_data(ticket["id"])
        qr.make()
        img.paste(qr.make_image().resize((134,134)), ticket_placement["QRCode"])

        img.save(f"tickets/ticket-{i}.png")
        i+=1