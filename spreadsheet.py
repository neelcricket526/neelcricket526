import gspread

# Helper method to determine if a String can be parsed as an int
def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True

#specify the path of the file "service_account.json" as the parameter 'filename' in order to run the gspread
gc = gspread.service_account(filename='service_account.json')

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = gc.open("Copy of Summer 2021 Work Party Master Sheet").sheet1

# Extract and print all of the values
# Will be a list of dictionaries
list_of_hashes = sheet.get_all_records()

# Initialize array for bros who have work parties due Tuesday
tuesday_work_party_members = []

# Iterate through the list of hashes, where each hash is a dictionary object
for hash in list_of_hashes:

	# Create a dictionary with the brother's name and their effective score, and add them to tuesday work members
	brother_dictionary = {"name" : hash["Name"], "score" : hash["Effective Score"]}
	tuesday_work_party_members.append(brother_dictionary)

# Sort the dictionaries based on scores
tuesday_work_party_members = sorted(tuesday_work_party_members, key = lambda i: str(i['score']))

# Read the first row for valid work parties
first_row = (list_of_hashes[0])
work_parties = []
for item in first_row.items():
	if is_int(item[1]):
		work_parties.append(item)

# Sort the work parties based on point value from highest to lowest
work_parties = sorted(work_parties, key = lambda i : i[1], reverse = True)

dictionary = dict(zip(work_parties, tuesday_work_party_members))

for item in dictionary.items():
	print(item[0][0])
	print(item[1].get('name'))
	print()
