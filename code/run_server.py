# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""
from flask import Flask, render_template, request, redirect, url_for
import bcrypt


def get_hashed(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)


# définir le message secret
SECRET_MESSAGE = "Goldman"
app = Flask(__name__, template_folder='templates')

# définir les identifiants d'un utilisateur
slogin = get_hashed("marcus".encode('utf-8'))
smdp = get_hashed("azerty".encode('utf-8'))


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if check(request.form['name'].encode('utf-8'), slogin) and check(request.form['mdp'].encode('utf-8'), smdp):
            return redirect(url_for('output'))
    return render_template('Home.html')


@app.route('/output')
def output():
    return render_template('output.html')


if __name__ == "__main__":
    # HTTP version
    # app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    context = ('server-public-key.pem', 'server-private-key.pem')
    app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=context)
