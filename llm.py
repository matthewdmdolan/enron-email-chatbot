


above_sample = pd.read_csv('email_data.csv')


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