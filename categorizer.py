from transformers import pipeline
from cleaner import clean_description

#print('AI MODEL IS LOADING...')

classifier = pipeline('zero-shot-classification', model="valhalla/distilbart-mnli-12-3")

candidate_labels = ['Food & Dining', 'Entertainment & Subscriptions', 'Salary & Income', 'Cash Withdrawals']

def get_ai_category(clean_text):
    if not clean_text.strip():
        return 'Other'
    result = classifier(clean_text, candidate_labels)
    return result['labels'][0]

# df = pd.read_csv('statement.csv')

# df['clean_description'] = df['description'].apply(clean_description)

# df['AI_Category'] = df['clean_description'].apply(get_ai_category)

# print("\n FINAL CATEGORIZED DATA: ")
# print(df[['description', 'AI_Category']])