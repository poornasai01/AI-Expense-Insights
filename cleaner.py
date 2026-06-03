import pandas as pd
import re

def clean_description(text):
    text = str(text).upper()
    text = re.sub(r'(UPI|NEFT|IMPS|RTGS|POS DEBIT)[/-]?\d*', '', text)
    text = re.sub(r'[^A-Z\s]', '', text)
    return " ".join(text.split())

if __name__ == "__main__":
    df = pd.read_csv('statement.csv')
    df['clean_description'] = df['description'].apply(clean_description)
    print(df[['description', 'clean_description']])