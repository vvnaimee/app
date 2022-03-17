import email
import json
import os
from email.message import EmailMessage

from flask import url_for

from app.models import User


def login(flask_client) -> User:
    # create user, user is activated
    user = User.create(
        email="a@b.c",
        password="password",
        name="Test User",
        activated=True,
        commit=True,
    )

    r = flask_client.post(
        url_for("auth.login"),
        data={"email": "a@b.c", "password": "password"},
        follow_redirects=True,
    )

    assert r.status_code == 200
    assert b"/auth/logout" in r.data

    return user


def create_user(flask_client) -> User:
    # create user, user is activated
    return User.create(
        email="a@b.c",
        password="password",
        name="Test User",
        activated=True,
        commit=True,
    )


def pretty(d):
    """pretty print as json"""
    print(json.dumps(d, indent=2))


def load_eml_file(filename: str) -> EmailMessage:
    emails_dir = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "example_emls"
    )
    fullpath = os.path.join(emails_dir, filename)
    return email.message_from_file(open(fullpath))
