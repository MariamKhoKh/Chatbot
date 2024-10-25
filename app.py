from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user, current_user, login_required
from forms import RegisterForm, LoginForm, ChatForm
from extensions import app, db
from models import Message, User
from datetime import datetime
from werkzeug.security import check_password_hash
import requests
import json


RASA_LINK = "http://127.0.0.1:5005"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/blog/<int:blog_id>")
def blog_post(blog_id):
    return render_template("blog_post.html", blog_id=blog_id)


@app.route("/chat", methods=["GET", "POST"])
def chat():
    form = ChatForm()

    if form.validate_on_submit():
        data = {
            "sender": current_user.username,
            "message": form.user_input.data
        }

        try:
            # Send message to Rasa server
            response = requests.post(f"{RASA_LINK}/webhooks/rest/webhook",
                                     data=json.dumps(data),
                                     headers={'Content-Type': 'application/json'})

            if response.status_code == 200:
                # Save the user's message to the database
                user_message = Message(
                    text=form.user_input.data,
                    sent_at=datetime.now(),
                    user_id=current_user.user_id,
                    is_chatbot=False
                )
                db.session.add(user_message)

                # Loop through all Rasa responses and save them
                for bot_reply in response.json():
                    bot_message = Message(
                        text=bot_reply["text"],
                        sent_at=datetime.now(),
                        user_id=current_user.user_id,
                        is_chatbot=True
                    )
                    db.session.add(bot_message)

                db.session.commit()

                # Clear the form input after processing
                form.user_input.data = ''
                return redirect(url_for("chat"))

        except requests.RequestException as e:
            print(f"Error contacting Rasa: {e}")

    return render_template("chat.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # print(form.email.data, form.password.data)
        user = User.query.filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next:
                return redirect(next)
            return redirect(url_for("home"))

    print(form.errors)
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()

        if existing_user:
            if existing_user.username == form.username.data:
                form.username.errors.append("The username you entered is already in use. Please choose a different username.")
            if existing_user.email == form.email.data:
                form.email.errors.append("The email address you entered is already registered. Please use a different email or log in.")
            return render_template("register.html", form=form)


        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data)
        user.create()
        return redirect(url_for("login"))

    return render_template("register.html", form=form)




app.run(debug=True)
