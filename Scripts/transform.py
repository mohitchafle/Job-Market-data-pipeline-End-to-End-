import json
import pandas as pd

def transform_data():
    with open("data/raw_jobs.json") as f:
        data = json.load(f)

    jobs = data["results"]

    job_list = []

    for job in jobs:
        job_list.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "category": job.get("category", {}).get("label"),
            "created": job.get("created")
        })

    df = pd.DataFrame(job_list)

    df.to_csv("data/processed_jobs.csv", index=False)

    print("Data transformed successfully!")

if __name__ == "__main__":
    transform_data()