from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()

    resp.say("Hello Sindhooram. Have fun!")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)