from flask import Flask, jsonify
from flask_mail import Mail, Message

# Create a Flask app with 1  route that sends an email to a user. Hint! using flask-mail package

#instance created 
app = Flask(__name__)

#SMTP credentials
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'sherlyne.ochieng@student.moringaschool.com'
app.config['MAIL_PASSWORD'] = 'slim hbpc dwit bsli'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

#create an instance of Message 
@app.route('/')
def email():
    msg = Message(
    subject = "First Email!",
    sender = "sherlyne.ochieng@student.moringaschool.com",
    recipients= ["sherlynea8622@gmail.com","ashley.natasha1@student.moringaschool.com", "antony.wambugu@student.moringaschool.com", "abdimalik.omar1@student.moringaschool.com" ],
    #What the message body will send
    body = "Hello,this is the first Flask email from the flask app. GROUP6")
    mail.send(msg)
    return "Message sent!"

if __name__ == '__main__':
    app.run(debug=True)
    