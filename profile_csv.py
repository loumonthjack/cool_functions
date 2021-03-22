import csv
import pandas as pd

def create_user_csv():
    fields = ['Email Address', 'Address']
    rows = [
        ['address@address.com', '211 address'],
        ['email@email.com', '1233 address']
    ]
    all_users_file = 'Profile.csv'

    with open(all_users_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    preview_file = pd.read_csv(all_users_file)
    print(preview_file)

create_user_csv()