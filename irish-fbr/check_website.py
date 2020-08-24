import requests
import bs4

response = requests.get(
    "https://www.dfa.ie/citizenship/born-abroad/registering-a-foreign-birth/"
)

if (
    "Please note that we have stopped processing Foreign Birth Registrations"
    not in response.text
):
    pass
