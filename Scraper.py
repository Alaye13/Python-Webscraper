from bs4 import BeautifulSoup
import requests
import csv


def multiScraper (urls):

    with open("fight_data.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)

# Send a GET request to the URL l
        for url in urls:
            response = requests.get(url)
            print(response)
            
            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Find the table body element & for the Significant Strikes table
            table_body = soup.find("tbody", class_="b-fight-details__table-body")
            
            sig_table_body = soup.find("tbody", class_="b-fight-details__table-body")
    

            # Significant Strikes

            head_sig_forfighter1 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(4) > p:nth-child(1)"
            ).get_text(strip=True)
            head_sig_forfighter2 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(4) > p:nth-child(2)"
            ).get_text(strip=True)
            
            body_sig_forfighter1 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(5) > p:nth-child(1)"
            ).get_text(strip=True)
            body_sig_forfighter2 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(5) > p:nth-child(2)"
            ).get_text(strip=True)
            leg_sig_forfighter1 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(6) > p:nth-child(1)"
            ).get_text(strip=True)
            leg_sig_forfighter2 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(6) > p:nth-child(2)"
            ).get_text(strip=True)
            distance_sig_forfighter1 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(7) > p:nth-child(1)"
            ).get_text(strip=True)
            distance_sig_forfighter2 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(7) > p:nth-child(2)"
            ).get_text(strip=True)
            clinch_sig_forfighter1 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(8) > p:nth-child(1)"
            ).get_text(strip=True)
            clinch_sig_forfighter2 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(8) > p:nth-child(2)"
            ).get_text(strip=True)
            ground_sig_forfighter1 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(9) > p:nth-child(1)"
            ).get_text(strip=True)
            ground_sig_forfighter2 = soup.select_one(
                "body > section > div > div > table > tbody > tr > td:nth-child(9) > p:nth-child(2)"
            ).get_text(strip=True)
            winforfighter1 = soup.select_one(
                "body > section > div > div > div.b-fight-details__persons.clearfix > div:nth-child(1) > i"
            ).get_text(strip=True)
            winforfighter2 = soup.select_one(
                "body > section > div > div > div.b-fight-details__persons.clearfix > div:nth-child(2) > i"
            ).get_text(strip=True)


            
                # Loop through each table row to extract data
            for row, sig_row in zip(
                table_body.find_all("tr", class_="b-fight-details__table-row"),
                sig_table_body.find_all("tr", class_="b-fight-details__table-row"),
            ):
                # for row, sig_row in zip(table_rows, sig_table_rows):

                # Extract all statistics for both fighters
                stats = row.find_all("p", class_="b-fight-details__table-text")
                stats = [stat.get_text(strip=True) for stat in stats]
                print(stats)
                sig_stats = [
                    data.get_text(strip=True)
                    for data in sig_row.find_all("p", class_="b-fight-details__table-text")
                ]
                # sig_stats = [stat.get_text(strip=True) for stat in sig_stats]
                print(sig_stats)
                
                ctrl_time_fighter1 = stats[18]

                ctrl_time_fighter2 = stats[19]
                
                def time_to_seconds(time_str):
                    minutes, seconds = map(int, time_str.split(':'))
                    return minutes * 60 + seconds

                ctrl_time_seconds_fighter1 = time_to_seconds(ctrl_time_fighter1)
                ctrl_time_seconds_fighter2 = time_to_seconds(ctrl_time_fighter2)

            
                # Combine the extracted data
                fighter1data = [
                    stats[0],  # Name (with double quotes)
                    stats[2],  # Knockdown
                    stats[4].split()[0],  # Fighter 1 Significant Strikes Landed
                    stats[4].split()[2],  # Fighter 1 Significant Strikes Attempted
                    stats[6],  # Significant Strikes %
                    stats[8].split()[0],  # Total Strikes Landed
                    stats[8].split()[2],  # total strikes Attempted
                    stats[10].split()[0],  # Fighter 1 Takedowns
                    stats[10].split()[2],  # take down attempted
                    stats[12],  # TD %
                    stats[14],  # Submission Attempts
                    stats[16],  # REV
                    ctrl_time_seconds_fighter1,  # CTRL TIME
                    head_sig_forfighter1.split()[0],
                    head_sig_forfighter1.split()[2],
                    body_sig_forfighter1.split()[0],
                    body_sig_forfighter1.split()[2],
                    leg_sig_forfighter1.split()[0],
                    leg_sig_forfighter1.split()[2],
                    distance_sig_forfighter1.split()[0],
                    distance_sig_forfighter1.split()[2],
                    clinch_sig_forfighter1.split()[0],
                    clinch_sig_forfighter1.split()[2],
                    ground_sig_forfighter1.split()[0],
                    ground_sig_forfighter1.split()[2],
                    winforfighter1,
                ]

                fighter2data = [
                    stats[1],  # Name (with double quotes)
                    stats[3],  # Knockdown
                    stats[5].split()[0],  # Fighter 1 Significant Strikes Landed
                    stats[5].split()[2],  # Fighter 1 Significant Strikes Attempted
                    stats[7],  # Significant Strikes %
                    stats[9].split()[0],  # Total Strikes Landed
                    stats[9].split()[2],  # total strikes Attempted
                    stats[11].split()[0],  # Fighter 1 Takedowns
                    stats[11].split()[2],  # take down attempted
                    stats[13],  # TD %
                    stats[15],  # Submission Attempts
                    stats[17],  # REV
                    ctrl_time_seconds_fighter2,  # CTRL TIME
                    head_sig_forfighter2.split()[0],
                    head_sig_forfighter2.split()[2],
                    body_sig_forfighter2.split()[0],
                    body_sig_forfighter2.split()[2],
                    leg_sig_forfighter2.split()[0],
                    leg_sig_forfighter2.split()[2],
                    distance_sig_forfighter2.split()[0],
                    distance_sig_forfighter2.split()[2],
                    clinch_sig_forfighter2.split()[0],
                    clinch_sig_forfighter2.split()[2],
                    ground_sig_forfighter2.split()[0],
                    ground_sig_forfighter2.split()[2],
                    winforfighter2,
                ]
                # Write the combined data to the CSV file
                writer.writerow(fighter1data)
                writer.writerow(fighter2data)
            
###############################################################################
# Write the Header row
with open("fight_data.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row
        header_row = [
            "Name",
            "Knockdown",
            "Significant_Strikes_Landed",
            "Significant_Strikes_Attempted",
            "Significant_Strike_%",
            "Total_Strikes_Landed",
            "Total_Strikes_Attempted",
            "Takedowns_Landed",
            "Takedowns_Attempted",
            "Takedowns_Percent",
            "Submission_Attempts",
            "REV",
            "Control_Time",
            "Head_Landed",
            "Head_Attempted",
            "Body_Landed",
            "Body_Attempted",
            "Leg_Landed",
            "Leg_Attempted",
            "Distance_Landed",
            "Distance_Attempted",
            "Clinch_Landed",
            "Clinch_Attempted",
            "Ground_Landed",
            "Ground_Attempted",
            "Winner",
        ]
        writer.writerow(header_row)







###############################################################################
#This is where event details will be scraped

def eventScraper(event_details): 
    

    for event in event_details:
        response = requests.get(event)

    # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        anchor_tags = soup.find_all("a")
        hrefs = []
        
        for tag in anchor_tags:
            if 'href' in tag.attrs:
                href = tag['href']
                hrefs.append(href)
            else:
                print("Anchor tag without href attribute:", tag)

            

        # Filter hrefs that start with the desired prefix
        fight_details = [tag['href'] for tag in anchor_tags if tag.has_attr('href') and tag['href'].startswith("http://ufcstats.com/fight-details/")]
        
        multiScraper(fight_details)
        

#Scrape the URL for each anchor text http://ufcstats.com/statistics/events/completed?page=all
#for each URL scrape the fight details anchor tags nested in the data link = 
# This will generate muultiple URLs that will be inserted in the array of URL
# URL of the webpage containing the table
###############################################################################
event_details = [
    "http://ufcstats.com/event-details/e4a9dbade7c7e1a7"
]

response = requests.get("http://ufcstats.com/statistics/events/completed?page=all")

    # Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")
anchor_tags = soup.find_all("a")
hrefs = []

for tag in anchor_tags:
    if 'href' in tag.attrs:
        href = tag['href']
        hrefs.append(href)
    else:
        print("Anchor tag without href attribute:", tag)

    

# Filter hrefs that start with the desired prefix
event_details = [tag['href'] for tag in anchor_tags if tag.has_attr('href') and tag['href'].startswith("http://ufcstats.com/event-details/")]

eventScraper(event_details)


    