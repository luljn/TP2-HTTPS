# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask import Flask, render_template

# définir le message secret
SECRET_MESSAGE = "Azertyuiop_1234!#qprtt"
app = Flask(__name__)

def get_secret_message():
    return SECRET_MESSAGE

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home")
def getHome():
    return render_template("home.html")

if __name__ == "__main__":
    # HTTP version
    # app.run(debug=True, host="0.0.0.0", port=8081)
    
    # HTTPS version
    context = ("resources/server-public-key.pem", "resources/server-private-key.pem")
    app.run(ssl_context = context, port = 8081)