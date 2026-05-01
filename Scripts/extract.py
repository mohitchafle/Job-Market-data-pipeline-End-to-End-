import requests
import json
import os

APP_ID = "787ac2a2"
APP_KEY = "50c3a0bf1685a5c4f9965d5fb9829b44"

def fetch_jobs():
    url = f"https://api.adzuna.com/v1/api/jobs/in/search/1?app_id={APP_ID}&app_key={APP_KEY}&what=data+engineer"
    
    response = requests.get(url)
    data = response.json()
    
    os.makedirs("data", exist_ok=True)

    with open("data/raw_jobs.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Data extracted successfully!")

if __name__ == "__main__":
    fetch_jobs()
