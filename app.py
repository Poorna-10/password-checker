from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Too short")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        remarks.append("Missing uppercase letter")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        remarks.append("Missing lowercase letter")

    if re.search(r'\d', password):
        score += 1
    else:
        remarks.append("Missing number")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        remarks.append("Missing special character")

    if re.search(r'(123|password|qwerty|abc)', password.lower()):
        remarks.append("Contains common patterns")

    if score >= 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, remarks

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    remarks = []

    if request.method == 'POST':
        password = request.form['password']
        strength, remarks = check_strength(password)

    return render_template('index.html', strength=strength, remarks=remarks)

if __name__ == '__main__':
    app.run(debug=True)
