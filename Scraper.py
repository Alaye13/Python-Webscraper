from bs4 import BeautifulSoup
import requests
import csv

# URL of the webpage containing the table
url = "http://ufcstats.com/fight-details/a74a8c1e0a49070d"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table body element
table_body = soup.find("tbody", class_="b-fight-details__table-body")

# Find all table rows within the table body
table_rows = table_body.find_all("tr", class_="b-fight-details__table-row")

#print ("The number of table rows," , table_rows)

# Open a CSV file in write mode
with open("fight_data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    header_row = [
        "Name",
        "Total Strikes Landed",       
        "Total Strikes Attempted",     
        "Significant Strikes Landed",
        "Significant Strikes Attempted",
        "Takedowns",
        "Submission Attempts",
        "Fight Time"
    ]
    writer.writerow(header_row)

    # Loop through each table row to extract data
    for row in table_rows:
        # Extract fighter names
        fighters = row.find_all("a", class_="b-link_style_black")
        print(fighters)
        fighter1 = fighters[0].get_text(strip=True)
        fighter2 = fighters[1].get_text(strip=True)

        # Extract all statistics for both fighters
        stats = row.find_all("p", class_="b-fight-details__table-text")
        stats = [stat.get_text(strip=True) for stat in stats]
        print(stats)

        # Combine the extracted data
        fighter1data = [
            fighter1,
            stats[2],             # Knockdown
            stats[4].split()[0],  # Fighter 1 Significant Strikes Landed
            stats[4].split()[2],  # Fighter 1 Significant Strikes Attempted
            stats[6],             # Significant Strikes %
            stats[8].split()[0],  
            stats[8].split()[2],           # total strikes landed
            stats[10].split()[0],  # Fighter 1 Takedowns
            stats[10].split()[2]   #take down atttempted
        ]

        fighter2data = [
                    fighter2,
                    stats[3],             # Knockdown
                    stats[5].split()[0],  # Fighter 1 Significant Strikes Landed
                    stats[5].split()[2],  # Fighter 1 Significant Strikes Attempted
                    stats[7],             # Significant Strikes %
                    stats[9].split()[0],  
                    stats[9].split()[2],           # total strikes landed
                    stats[11].split()[0],  # Fighter 1 Takedowns
                    stats[11].split()[2]   #take down atttempted
                ]
        # Write the combined data to the CSV file
        writer.writerow(fighter1data)
        writer.writerow(fighter2data)

