from Request import Request
from Module.Logger import Logger
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

logger = Logger("-")
request = Request("shit11@shit.com", "shit@shit.com")
data = request.enter()[1]
logger.log("logged in")


def work_on_account(link):

    player = data.get_instance_by_link(link)
    habitats = [habitat for habitat in data.data["habitat"].values() if habitat.player_id == player.id]
    castles, fortresses, cities = (len([habitat for habitat in habitats if habitat.type == "CAST"]),
                                   len([habitat for habitat in habitats if habitat.type == "FORT"]),
                                   len([habitat for habitat in habitats if habitat.type == "CITY"]))
    if player.alliance_id is None:
        alliance = "-"
    else:
        alliance = [alliance for alliance in data.data["alliance"].values() if alliance.id == player.alliance_id][0].name
    return [player.name, alliance, int(player.points), castles]


def delete_row(ind):
    done = False
    while not done:
        try:
            sheet.delete_row(ind)
            done = True
        except gspread.exceptions.APIError:
            time.sleep(10)


def insert_row(rec, ind):
    done = False
    while not done:
        try:
            sheet.insert_row(rec, ind)
            done = True
        except gspread.exceptions.APIError:
            time.sleep(10)


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials2.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1cYbIylnAiJVKDB0TTFn_xbm4wceRG4ZaRQpiJOJEx24/edit?usp=sharing").sheet1

# Extract and print all of the values
records = sheet.get_all_records()
for index in range(len(records)):
    record = records[index]
    if not "@" in record["email"]:
        continue
    new_record = work_on_account(record["link"])
    new_record = [record["email"], record["password"], record["link"]] + new_record + [record["notes"]]
    logger.log(new_record)
    delete_row(index + 2)
    insert_row(new_record, index + 2)
