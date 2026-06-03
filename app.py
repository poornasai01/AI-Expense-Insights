from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io
from categorizer import clean_description, get_ai_category, candidate_labels

app = FastAPI(title = 'AI Expense Categorizer API')

@app.get("/")
def home():
    return {"message": "Welcome to the AI Expense Categorizer API! Use the /upload endpoint to process CSVs."}

@app.post("/upload")
async def upload_statement(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    df['Clean_Description'] = df['Description'].apply(clean_description)
    df['AI_Category'] = df['Clean_Description'].apply(get_ai_category)

    result_data = df[['Description', 'AI_Category']].to_dict(orient='records')

    return {"status": "Success", "transactions": result_data}