import requests
from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


def spin_up_twilio() -> Client:
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    return Client(account_sid, auth_token)


def text_alex(msg: str) -> None:
    client = spin_up_twilio()
    client.messages.create(
        body=msg, from_=os.getenv("TWILIO_FROM"), to=os.getenv("TWILIO_TO"),
    )


def is_open(
    html: str,
    search_term: str = "Please note that we have stopped processing Foreign Birth Registrations",
) -> bool:
    return search_term not in html


def fetch_webpage(url: str) -> str:
    return requests.get(url).text


def fetch_irish_fbr_webpage() -> str:
    return fetch_webpage(
        "https://www.dfa.ie/citizenship/born-abroad/registering-a-foreign-birth/"
    )


if __name__ == "__main__":
    response = fetch_irish_fbr_webpage()

    if is_open(response):
        text_alex("Irish Foreign Birth Register website has changed.")
