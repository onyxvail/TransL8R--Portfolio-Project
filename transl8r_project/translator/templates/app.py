from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration for ProtonMail Bridge
app.config['MAIL_SERVER'] = '127.0.0.1'  # Use localhost as the server since Bridge runs locally
app.config['MAIL_PORT'] = 1025  # The default port for ProtonMail Bridge
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False  # ProtonMail Bridge doesn't use SSL

mail = Mail(app)

@app.route('/')
def index():
    return render_template('home.html')  # Update this with your actual HTML file

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

        return render_template('home.html')  # Update this with your actual success HTML file

if __name__ == '__main__':
    app.run(debug=True)
