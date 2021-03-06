"""
APP - Flask server endpoint

Sets up a super-simple HTTP POST endpoint, for the
GroupMe API to ping with new messages from the group

Flask parts were made almost entirely with this tutorial:
http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/
"""
import firstblood
from flask import Flask, request
app = Flask(__name__)
print(app.config)

@app.route("/", methods=['POST','GET'])
def webhook():
    data = request.get_json()

    print(data)
    print(type(data))
    print(data['name'])
    print(type(data['name']))

    if data['name'] != "firstblood":
        # msg = 'You (name={}) sent "{}"'.format(data['name'], data['text'])
        # send_message(msg)
        firstblood.incoming_message(data)
    return "ok", 200


# if __name__ == '__main__':
#     app.run(use_reloader=False)