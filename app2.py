from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Create a new chat bot named Charlie

app = Flask(__name__)
chatbot = chatbot = ChatBot(
    'Charlie',
    trainer='chatterbot.trainers.ListTrainer'
)
chatbot.set_trainer(ListTrainer)

chatbot.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('hello')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run(host='localhost',port=9874)
