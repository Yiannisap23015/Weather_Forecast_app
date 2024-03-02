from flask import Flask, redirect, url_for, request, render_template
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
import logging
from flask_wtf import CSRFProtect
import pickle
from models import User
import os
from config import USERFILE
from database import init_db, db_session
from sqlalchemy import desc
logging.basicConfig(filename="record.log", level=logging.DEBUG)

from weather import get_current_weather

app = Flask(__name__)
# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

with app.app_context():
    init_db()

import secrets

foo = secrets.token_urlsafe(16)
app.secret_key = foo

app.logger.info("Environmental variable Initialized")

@app.route('/')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if city is None:
        return render_template('weather.html')

    weather_data = get_current_weather(city)
    # City is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    
    if not city.strip():
        return render_template('city-not-provided.html')
    
    # Update the database
    show_user_form(city, weather_data['main']['temp'])

    # Assuming weather_data is a dictionary with relevant weather information
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}"
    )

@app.route("/fuser", methods=["POST"])
def show_user_form(city, weather):
    user = User(city=city, weather=weather)
    db_session.add(user)
    db_session.commit()
    return redirect(url_for("show_users"))

@app.route("/users", methods=["GET"])
def show_users():
    users = User.query.order_by(desc(User.date_created)).all()
    return render_template("users.html", users=users)
