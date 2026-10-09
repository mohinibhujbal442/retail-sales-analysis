import csv
from pathlib import Path

file_path = Path(__file__).parent / "data" / "SampleSuperstore.csv"

if not file_path.exists():
    print("CSV file not found:", file_path)
else:
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    print("Dataset loaded successfully!")
    print("Number of rows:", len(rows))
    print("Number of columns:", len(reader.fieldnames or []))
    print("\nColumn names:")
    print(reader.fieldnames)

    print("\nFirst 3 rows:")
    for row in rows[:3]:
        print(row)
        