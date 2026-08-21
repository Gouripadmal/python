from tracker import create_record
from datetime import datetime
import json

# Create travel records
records = [
    create_record("Delhi", "Visited the Red Fort", "05-06-2022"),
    create_record("Mumbai", "Enjoyed Marine Drive", "15-07-2023"),
    create_record("Jaipur", "Explored the Amber Fort", "20-08-2024")
]

# Convert date into readable format
for record in records:
    date_object = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_object.strftime("%B %d, %Y")

# Convert list into JSON string
json_data = json.dumps(records, indent=4)

print("JSON String:")
print(json_data)

# Parse JSON back into Python object
python_data = json.loads(json_data)

# Display each record separately
print("\nTravel Records:")

for record in python_data:
    print(record)