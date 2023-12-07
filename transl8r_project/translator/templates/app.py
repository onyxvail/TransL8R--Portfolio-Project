from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration for ProtonMail Bridge
app.config['MAIL_SERVER'] = '127.0.0.1'
app.config['MAIL_PORT'] = 1025  
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        country = request.form['country']
        subject = request.form['subject']

        # Send email
        msg = Message('New Contact Form Submission', sender='transl8r@protonmail.com', recipients=['transl8r@protonmail.com'])
        msg.body = f'First Name: {firstname}\nLast Name: {lastname}\nCountry: {country}\nSubject: {subject}'
        mail.send(msg)

        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
