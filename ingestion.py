import os
import time
import pandas as pd

#looping through all 500k emails to identify metadata on files so we can begin our eda
def fetch_data(dir_path):
    data = {'directory': [], 'file_name': [], 'file_size': [], 'file_date': []}
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            f_path = os.path.join(dirpath, f)
            data["directory"].append(dirpath)
            data["file_name"].append(f)
            data["file_size"].append(os.path.getsize(f_path))
            data["file_date"].append(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(f_path))))
    return data

dir_path = "/Users/mattdolan/Downloads/maildir"
data = fetch_data(dir_path)

df = pd.DataFrame(data)
df.to_csv('email_data.csv', index=False)