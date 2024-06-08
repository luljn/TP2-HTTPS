# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask import Flask, render_template, request, redirect
import sqlite3
import hashlib

# définir le message secret
SECRET_MESSAGE = "Azertyuiop_1234!#qprtt"
app = Flask(__name__)
app.config['DATABASE'] = "lib/database.sql"

def get_secret_message():
    return SECRET_MESSAGE

def getDatabase():
    
    return sqlite3.connect(app.config['DATABASE'])

@app.route("/", methods = ['GET', 'POST'])
def login():
    
    if(request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        conn = getDatabase()
        cursor = conn.cursor()
        
        cursor.execute('SELECT email, password FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        
        if user and user[1] == hashlib.sha256(password.encode()).hexdigest():
            return redirect("/home")
        
        return render_template("login.html", errorMessage = "Adresse mail et/ou mot de passe incorrect(s)")
    
    return render_template("login.html")

@app.route("/home")
def getHome():
    return render_template("home.html", message = get_secret_message())

@app.route("/logout")
def logout():
    return redirect("/")

if __name__ == "__main__":
    # HTTP version
    # app.run(debug=True, host="0.0.0.0", port=8081)
    
    # HTTPS version
    context = ("resources/server-public-key.pem", "resources/server-private-key.pem")
    app.run(ssl_context = context, port = 8081)