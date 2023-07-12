import re
import magic
from email import message_from_string
import pandas as pd
import os
import docx2txt
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
import seaborn as sns
import os
from PyPDF4 import PdfFileReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from email import message_from_string
import pandas as pd
# this function loops through th
from PyPDF4 import PdfFileReader
from email import message_from_string
import pandas as pd
import os

# Loading
df = pd.DataFrame()
df = pd.read_csv('email_data.csv')

def find_spam(column):
    pattern = r'\bspam\b'
    match = re.search(pattern, column, re.IGNORECASE)
    return match is not None

# Use apply to create a new column with True where 'spam' is found and False otherwise
df['contains_spam_directory'] = df['directory'].apply(find_spam)
df['contains_spam_file_name'] = df['file_name'].apply(find_spam)
print(df)

# assuming df is your DataFrame and 'file_size' is the column name
sns.boxplot(x=df['file_size'])
# plt.show()

# finding median file size
median_file_size = df['file_size'].median()

# going to do a sentiment analysis of those below median filesize and do random samples from each?
df_below_median = df[df['file_size'] < median_file_size]
df_above_median = df[df['file_size'] > median_file_size]

# Step 1: Determine median file size
median_file_size = df['file_size'].median()

# Step 2: Split DataFrame based on file size
above_median = df[df['file_size'] > median_file_size]
below_median = df[df['file_size'] <= median_file_size]

# Step 3: Take a random sample from each DataFrame
sample_size = 1000  # adjust this to fit your needs
above_sample = above_median.sample(sample_size)
below_sample = below_median.sample(sample_size)

def fetch_data(dir_path, sample_df):
    data = {'directory': [], 'file_name': [], 'file_size': [], 'file_date': [], 'content': [], 'email_body': []}
    for index, row in sample_df.iterrows():
        dirpath = row['directory']
        f = row['file_name']
        f_path = os.path.join(dirpath, f)
        data["directory"].append(dirpath)
        data["file_name"].append(f)
        data["file_size"].append(os.path.getsize(f_path))
        data["file_date"].append(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(f_path))))
        try:
            with open(f_path, 'r') as file:
                content = file.read()
                message = message_from_string(content)
                print(message)  # Do something with the message if required
                # Get the email body
                if message.is_multipart():
                    for part in message.walk():
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload()
                            data["email_body"].append(body)
                            data["content"].append(content)
                else:
                    body = message.get_payload()
                    data["email_body"].append(body)
                    data["content"].append(content)

        except Exception as e:
            print(f"Error reading file {f_path}: {e}")

        df = pd.DataFrame(data)
        # print(df.head())

dir_path = "/Users/mattdolan/Downloads/maildir"
above_median_sentiment_analysis = fetch_data(dir_path, above_sample)
below_median_sentiment_analysis = fetch_data(dir_path, below_sample)

# print(above_median_sentiment_analysis.head())
# print(below_median_sentiment_analysis.heaD())

# Sentiment Analysis
sia = SentimentIntensityAnalyzer()

# Apply sentiment analysis on email body
above_sample['sentiment'] = above_sample['EmailBody'].apply(lambda x: sia.polarity_scores(x))
below_sample['sentiment'] = below_sample['EmailBody'].apply(lambda x: sia.polarity_scores(x))
#
# # Extract compound score
# above_sample['compound'] = above_sample['sentiment'].apply(lambda score_dict: score_dict['compound'])
# below_sample['compound'] = below_sample['sentiment'].apply(lambda score_dict: score_dict['compound'])
#
# # Now you have two samples you can compare for sentiment analysis
#
#
#
#
#
#
#
#
#
#
#
#
# """Folder-level EDA"""
# # details per folder:
# folders_stats = df.groupby("directory").agg({"file_name": 'count',
#                                              "file_size": "sum"}) \
#     .rename(columns={"file_name": "total_files", "file_size": "total_size"}) \
#     .reset_index()
#
# print(folders_stats)
