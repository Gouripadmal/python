import tracker
from datetime import datetime
import json
records = []
records.append(tracker.records(
    "Paris",
    "Visited the Eiffel Tower",
    "05-06-2022"
))
records.append(tracker.create_record(
    "India",
    "Visited the kashmir ",
    "10-06-2022"
))
records.append(tracker.create_record(
    "Nepal",
    "Visited the Kathmandu",
    "15-06-2022"
))
for record in records:
    date_object = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_object.strftime("%B %d, %Y")
json_data = json.dumps(records, indent=4)

print("JSON Data:")
print(json_data)

python_data = json.loads(json_data)
print("\nTravel Records:")

for record in python_data:
    print(
        record["city"],
        "-",
        record["comment"],
        "-",
        record["date"]
    )





















