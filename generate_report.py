import csv
from datetime import datetime

# Generate report
filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Status"])
    writer.writerow([1, "Complete"])

print(f"Report saved as {filename}")