import os
import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=['GET', 'POST'])
def home():
    """Default homepage to prevent 404/405 errors."""
    return "WhatsApp Bot is Running!", 200

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    """Handles incoming WhatsApp messages via Twilio Webhook."""
    try:
        msg = request.form.get("Body", "").strip()  # Ensure msg is not None
        sender = request.form.get("From", "Unknown")  # Capture sender info
        logging.info(f"Received message from {sender}: {msg}")

        response = MessagingResponse()

        responses = {
            "hello": "Hello! How can I assist you today?",
            "help": "Sure! You can type:\n- 'info' for details\n- 'support' for help",
            "info": "This is a simple WhatsApp bot built with Flask and Twilio!",
            "support": "Contact our support team at support@example.com."
        }

        # Match user input against known responses
        reply = responses.get(msg.lower(), "Sorry, I didn't understand that. Type 'help' for assistance.")
        response.message(reply)

        return str(response)
    
    except Exception as e:
        logging.error(f"Error processing message: {str(e)}")
        return str(MessagingResponse().message("An error occurred. Please try again later."))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment
    app.run(host="0.0.0.0", port=port, debug=True)
