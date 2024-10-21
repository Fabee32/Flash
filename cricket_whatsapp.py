
import requests
from bs4 import BeautifulSoup
import pywhatkit as kit
import time

# Function to scrape cricket scores from Crex
def get_cricket_score():
    url = 'https://www.crex.live/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    match_info = soup.find_all('div', class_='match-info')  # Adjust selector for Crex live site structure
    matches = []

    for match in match_info:
        team1 = match.find('div', class_='team1').text
        team2 = match.find('div', class_='team2').text
        score = match.find('div', class_='score').text
        status = match.find('div', class_='status').text
        matches.append(f"{team1} vs {team2} - {score} - {status}")
    
    return matches

# Function to send WhatsApp messages using pywhatkit
def send_whatsapp_message(message, phone_number):
    kit.sendwhatmsg_instantly(phone_number, message)

# Main function to fetch the score and send the updates
def cricket_score_update(phone_number):
    matches = get_cricket_score()
    for match in matches:
        send_whatsapp_message(match, phone_number)

# Continuous update every 5 minutes
if __name__ == "__main__":
    phone_number = "+919876543210"  # Replace with the actual phone number
    while True:
        cricket_score_update(phone_number)
        time.sleep(300)  # 5 minutes interval
