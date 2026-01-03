# 📊 WhatsApp Chat Analyzer (Streamlit App)

A web-based WhatsApp chat analysis application built with **Python** and **Streamlit**, designed to extract meaningful insights from exported WhatsApp chat data.  
The app supports **group and individual analysis**, multilingual text (English + Banglish), and emoji-based interaction insights.

---

## 🚀 Features Implemented

### 1️⃣ Overall Chat Statistics
Provides a high-level summary of the chat:
- **Total messages**
- **Total words**
- **Total media messages**
- **Total shared links**

These metrics help understand overall chat volume and engagement.

---

### 2️⃣ Most Active Users Analysis (Group Chats)
- Displays **top contributors** in the group
- Visualized using a **bar chart**
- Includes **percentage contribution** of each user

This highlights participation dominance and group dynamics.

---

### 3️⃣ WordCloud Analysis (Group & Individual)

#### 🔹 Text Processing Steps
- Removal of **English stopwords**
- Removal of **Banglish stopwords**
- Removal of **emojis**
- Removal of empty or null messages

#### 🔹 Output
- **Group-level WordCloud**
- **Individual user WordCloud**

This helps identify the most frequently used meaningful words in conversations.

---

### 4️⃣ Most Frequently Used Words
- Cleaned and tokenized messages
- Word frequency calculation
- Visualization using a **bar chart**

This provides precise and interpretable frequency comparisons.

---

### 5️⃣ Emoji Analysis
- Extracts emojis from messages
- Counts emoji frequency
- Displays emoji usage using a **bar chart**

Emoji analysis offers insight into emotional expression and interaction patterns.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web application framework
- **Pandas** – Data manipulation
- **Matplotlib / Plotly** – Data visualization
- **WordCloud** – WordCloud generation
- **Regex** – Message parsing
- **Emoji** – Emoji extraction
- **Banglish Stopwords** – Custom Banglish stopword filtering

---

## 📂 Input Requirements

- WhatsApp chat export file (`.txt`)
- Supports **group chats** and **individual chats**
- Chat must be exported **without media**

---

## 🧠 Use Cases

- Group participation analysis
- User activity comparison
- Language usage insights
- Emoji behavior analysis
- Social, academic, and research-based chat analysis

---

## 📈 Future Enhancements (Planned)

- Timeline analysis (daily / monthly activity)
- Activity heatmap (day vs hour)
- Sentiment analysis

---

## ▶️ How to Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
