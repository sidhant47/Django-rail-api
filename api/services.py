import dialogflow_v2 as dialogflow
import os
import requests
from dateutil import parser

project_id = "railway-api-e78a8"
language_code = 'en'
RAIL_API_KEY = "uh555p4jxy"


def detect_intent_texts(session_id, text, ):

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(
        session=session, query_input=query_input)
    return response


def station_to_code(city):
    data = {
        "delhi": "DLI",
        "amritsar": "ASR",
        "jammu": "JAT",
        "bhopal": "BPL",
        "banglore": "SBC",
        "kanpur": "CNB",
        "jaipur": "JP",
        "hyderabad": "HYD",
        "mumbai": "BCT",
        "kolkata": "KOAA",
    }
    return data[city.lower()]


def search_trains(source, destination, date):
    source = station_to_code(source)
    destination = station_to_code(destination)
    date = format_date(date)
    url = "https://api.railwayapi.com/v2/between/source/{}/dest/{}/date/{}/apikey/{}/".format(
        source, destination, date, RAIL_API_KEY)
    r = requests.get(url)
    return r.json()


def format_date(date):
    d = parser.parse(date)
    return "{}-{}-{}".format(d.day, d.month, d.year)
