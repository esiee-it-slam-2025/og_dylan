import json, os, time, uuid, re, qrcode
from datetime import datetime
from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
from datas_variables import *


# ****************************************************************************************************************************************************************
# /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  /  FUNCTION
# ****************************************************************************************************************************************************************

# Function to display menu options
def show_actions():
    print("==================================")
    print("|  Choose an action (1-4) :")
    print("|  1 - Generate all the tickets")
    print("|  2 - Create a new ticket")
    print("|  3 - View available tickets")
    print("|  4 - Exit program")

# Function to verify integer input within a specified range
def verif_int(texte, lim):
    while True:
        valeur = input(texte)
        if valeur.isdigit() and 0 < int(valeur) <= lim:
            return int(valeur)
        else:
            print(f"Please enter an integer between 1 and {lim}")

# Function to format datetime string
def format_datetime(iso_datetime):
    dt = datetime.fromisoformat(iso_datetime)
    formatted_date = dt.strftime("%d/%m/%Y")
    formatted_time = dt.strftime("%H:%M")
    return formatted_date, formatted_time

# Function to display a loading bar
def display_loading_bar(percentage):
    filled_character = int(50 * percentage / 100)
    empty_character = 50 - filled_character
    loading_bar = '[' + '=' * filled_character + ' ' * empty_character + ']'
    print('\r' + loading_bar + f' {percentage:.1f}%', end='', flush=True)

# Recursive function to update and display loading bar
def recursive_loading_bar(percentage):
    if percentage <= 100:
        display_loading_bar(percentage)
        time.sleep(0.05)
        recursive_loading_bar(percentage + 1)

# Function to clear the 'tickets' folder
def clear_folder():
    os.system("cls")
    print("Deleting existing files in the folder...")
    time.sleep(2)
    for fichier in os.listdir("tickets"):
        chemin_fichier = os.path.join("tickets", fichier)
        try:
            if os.path.isfile(chemin_fichier):
                os.remove(chemin_fichier)
        except Exception as e:
            print(f"Error deleting file {chemin_fichier}: {e}")
    print("Contents of 'tickets' folder successfully deleted.")
    time.sleep(2)

# Function to generate tickets
def generate_tickets():
    os.system("cls")
    print("Generating tickets...")
    recursive_loading_bar(0)
    for ticket in tickets:

        # Finding the event associated with the ticket
        event = next(filter(lambda x: x["id"] == ticket["event_id"], events), None)
        stadium = next(filter(lambda x: x["id"] == event["stadium_id"], stadiums), None)

        # Extracting formatted date and time from the event start datetime
        formatted_date, formatted_time = format_datetime(event["start"])

        # Used to generate a shorter .png name
        home_team = event["team_home"][:3].upper()
        away_team = event["team_away"][:3].upper()

        # Condition to choose "€" or "$"
        seat = 'Libre' if ticket['seat'] == 'free' else ticket["seat"]

        # Open the ticket template image and prepare to draw on it
        with Image.open("ticketJO.png") as img:
            # Create a drawing context
            add_data = ImageDraw.Draw(img)
            
            # Add text for home team, away team, stadium, date, category, seat, and price
            add_data.text(ticket_placement["HomeT"], event["team_home"], fill=blue, font=font36)
            add_data.text(ticket_placement["AwayT"], event["team_away"], fill=blue, font=font36)
            add_data.text(ticket_placement["Stadium"], f"{stadium['name']} - {stadium['location']}", fill=white, font=font22)
            add_data.text(ticket_placement["Date"], f"{formatted_date} à {formatted_time}", fill=white, font=font22)
            add_data.text(ticket_placement["Category"], ticket["category"], fill=white, font=font22)
            add_data.text(ticket_placement["Seat"], seat, fill=white, font=font22)
            add_data.text(ticket_placement["Price"], f"{ticket['price']} {'€' if ticket['currency'] != 'USD' else '$'}", fill=white, font=font22)
            
            # Create a QR code 
            qr = qrcode.QRCode(box_size=4, border=2)
            qr.add_data(ticket["id"])
            qr.make()
            
            # Paste the QR code onto the ticket template image
            img.paste(qr.make_image(fill_color="black", back_color="white").resize((148, 148)), ticket_placement["QRCode"])
            
            # Save the modified ticket image with a filename based on team names and seat
            img.save(f"tickets/{home_team}-{away_team}_{seat}.png")

            print("\nTickets successfully generated !")
            time.sleep(2)

# Function to create a new ticket
def create_ticket():
    os.system("cls")
    
    # Display the list of available games
    print("List of games:\n")
    for i, event in enumerate(events, start=1):
        formatted_date, formatted_time = format_datetime(event["start"])
        print(f"{i}. {event['team_home']} - {event['team_away']} at {formatted_time} on {formatted_date}")

    # Prompt the user to select a game by ID
    event_id = verif_int("\nEnter the ID of the game for which you are creating the ticket: ", len(events))
    
    # Prompt the user for currency (EUR or USD)
    currency = ""
    while currency not in ["EUR", "USD"]:
        currency = input("Currency (EUR or USD): ").upper()
    
    # Prompt the user for ticket category (Silver, Gold, or Platinum)
    category = ""
    while category not in ["Silver", "Gold", "Platinum"]:
        category = input("Category (Silver, Gold, or Platinum): ")
    
    # Validate and prompt the user for seat number (format LETTER-XX)
    seat_pattern = re.compile(r'^[A-Z]-\d{2}$')
    seat = ""
    while not seat_pattern.match(seat):
        seat = input("Seat Number (format LETTER-XX): ").strip().upper()
        if not seat_pattern.match(seat):
            print("Invalid format. Please enter seat number in the format LETTER-XX (e.g., A-10).")
    
    # Create a new ticket with provided details
    new_ticket = {
        "id": str(uuid.uuid4()),
        "event_id": event_id,
        "category": category,
        "seat": seat,
        "price": int(input("Ticket Price: ")),
        "currency": currency
    }

    print("Creating a new ticket...\n")
    recursive_loading_bar(0)
    
    # Add the new ticket to the list of tickets
    tickets.append(new_ticket)
    
    # Save the updated list of tickets to a JSON file
    with open('tickets.json', 'w', encoding='utf-8') as f:
        json.dump(tickets, f, ensure_ascii=False, indent=4)
    
    print("\nNew ticket created successfully!")
    time.sleep(2)


# Function to display a ticket using Tkinter
def show_ticket(ticket_name):
    # Create a Tkinter window
    window = tk.Tk() 
    window.title("Ticket")
    
    # Open the ticket image file and resize it
    img = Image.open(os.path.join("tickets", ticket_name))
    img = img.resize((400, 900))
    
    # Convert the image to a Tkinter-compatible format
    photo = ImageTk.PhotoImage(img)
    
    # Create a Tkinter label to display the image
    label = tk.Label(window, image=photo)
    label.image = photo
    label.pack()
    
    # Create a Tkinter button to close the window
    button = tk.Button(window, text="Close", command=window.destroy)
    button.pack()
    
    window.mainloop()


# Function to display available tickets
def display_available_tickets():
    # Get the list of ticket files in the "tickets" folder
    files = os.listdir("tickets")

    if not files:
        os.system("cls")
        print("No tickets available.")
        time.sleep(2)
        return
    
    os.system("cls")
    
    # Display the list of available tickets
    print("Available Tickets:\n")
    for index, file in enumerate(files, start=1):
        # Extract filename without the extension
        filename, extension = os.path.splitext(file)
        print(f"{index}. {filename}")
    
    # Prompt the user to select a ticket by number
    ticket_choice = int(input("\nEnter the number of the ticket you want to view: ")) - 1
    try:
        if 0 <= ticket_choice < len(files):
            show_ticket(files[ticket_choice])
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid choice. Please enter a valid number.")

