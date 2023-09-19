import requests
import json


def get_shloka(ch, v):
    try:
        url = f"https://bhagavadgitaapi.in/slok/{ch}/{v}"
        r = requests.get(url)
        json_data = r.json()
        info = [json_data["slok"], json_data["transliteration"], json_data["purohit"]["et"]]
    except:
        info = ["Shloka doesn't exist", "Shloka doesn't exist", "Shloka doesn't exist"]

    return info
