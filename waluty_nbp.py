from datetime import datetime

import pandas as pd
import requests

today = datetime.now().strftime("%Y-%m-%d")
table = "A"
api_url = f"https://api.nbp.pl/api/exchangerates/tables/{table}/{today}/?format=json"
res = requests.get(api_url)
if res.status_code != 200:
    print(f"Błąd pobierania notowań ({today} to dzień bez notowań?)")
    print(f"HTTP Error {res.status_code}")
    exit()

data = res.json()[0]

print(f"Notowanie {data['no']} z dnia {data['effectiveDate']}:")
print("=" * 61)

notowania = pd.DataFrame(sorted(data["rates"], key=lambda d: d["code"]))
print(notowania.to_markdown(index=False))
print("=" * 61)
