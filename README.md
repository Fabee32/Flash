
# Cricket Score WhatsApp Automation

This project scrapes live cricket scores from Crex and sends ball-by-ball updates via WhatsApp.

## Requirements

- Python 3.x
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## How to Run

1. Clone the repository or open it in GitHub Codespaces.
2. Make sure to install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Replace the phone number in `cricket_whatsapp.py` with your own (in international format).
4. Run the script:
   ```bash
   python cricket_whatsapp.py
   ```

The script will send WhatsApp messages every 5 minutes with live cricket score updates.

**Note:** You need to have WhatsApp Web logged in for the script to work with `pywhatkit`.
