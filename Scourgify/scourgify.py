import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input = sys.argv[1]
output = sys.argv[2]

try:
    input_file = open(input)
except FileNotFoundError:
    sys.exit(f"Could not read {input}")

new_format=[]

reader = csv.DictReader(input_file)
for row in reader:
    last, first = row["name"].split(", ")
    new_row = {"first": first, "last": last, "house": row["house"]}
    new_format.append(new_row)

input_file.close()

with open(output, "w") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in new_format:
        writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
