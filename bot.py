from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    msg = request.form.get("Body")
    response = MessagingResponse()
    
    if "hello" in msg.lower():
        response.message("Hello! How can I help you?")
    elif "help" in msg.lower():
        response.message("Sure! Type 'info' to learn more.")
    else:
        response.message("Sorry, I didn't understand that. Type 'help' for assistance.")
    
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
