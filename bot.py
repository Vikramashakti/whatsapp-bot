import os
import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Enable logging for debugging
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=['GET'])
def home():
    """Default homepage to prevent 404 errors."""
    return "WhatsApp Bot is Running!", 200

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    """Handles incoming WhatsApp messages via Twilio Webhook."""
    try:
        sender = request.form.get("From", "")
        msg = request.form.get("Body", "").strip()  # Ensure msg is not None
        logging.info(f"Received message from {sender}: {msg}")

        response = MessagingResponse()

        if not msg:
            reply = "Oops! I didn't receive any message. Try again."
        elif "hello" in msg.lower():
            reply = "Hello! How can I assist you today?"
        elif "help" in msg.lower():
            reply = "Sure! You can type:\n- 'info' for details\n- 'support' for help"
        elif "info" in msg.lower():
            reply = "This is a simple WhatsApp bot built with Flask and Twilio!"
        else:
            reply = "Sorry, I didn't understand that. Type 'help' for assistance."

        response.message(reply)
        logging.info(f"Replying to {sender}: {reply}")  # Log what is being sent

        return str(response)
    
    except Exception as e:
        logging.error(f"Error processing message: {str(e)}")
        return str(MessagingResponse().message("An error occurred. Please try again later."))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment
    app.run(host="0.0.0.0", port=port, debug=True)
