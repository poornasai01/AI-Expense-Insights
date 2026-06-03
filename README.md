# AI-Expense-Insights
# 📊 AI-Powered Financial Insights Dashboard

An end-to-end Machine Learning pipeline that transforms messy, unstructured bank statements into clean, actionable financial insights using Zero-Shot Natural Language Processing (NLP).

## 🚀 Project Overview
Traditional expense trackers require users to manually categorize their transactions or rely on hard-coded keyword rules that easily break. This project solves that problem by integrating a pre-trained **Hugging Face Transformer model** to dynamically read and categorize raw bank jargon (like `UPI/Zomato/123456`) into intelligent categories—without needing a labeled training dataset.

## 🧠 Core Architecture
1. **Data Engineering (Pandas & Regex):** Cleans raw CSV data by stripping out banking codes, reference numbers, and special characters.
2. **AI Classification (Hugging Face):** Utilizes the `distilbart-mnli-12-3` zero-shot classification model to interpret the cleaned merchant names and intelligently assign them to custom categories.
3. **Backend API (FastAPI):** Orchestrates the data flow by receiving in-memory file uploads and processing the AI pipeline securely.
4. **Frontend UI (Streamlit & Plotly):** Provides a responsive, drag-and-drop web interface for users to visualize their spending patterns through interactive charts.

## 🛠️ Tech Stack
* **Language:** Python
* **Machine Learning:** Hugging Face Transformers, PyTorch
* **Data Processing:** Pandas, Regular Expressions (Regex)
* **Frontend:** Streamlit, Plotly
* **Backend:** FastAPI, Uvicorn
<img width="400" height="225" alt="video project" src="https://github.com/user-attachments/assets/f6e33d14-9a1d-4f4b-85c9-7956729db637" />
