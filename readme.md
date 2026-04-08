# 📊 Instagram Engagement Predictor (Rule-Based)

## 🔹 Overview
This project predicts whether an Instagram post will achieve High or Low engagement using simple rule-based logic. Instead of using complex machine learning models, this system uses logical conditions to make predictions.

---

## 🔹 Dataset
The dataset is embedded directly in the code and contains:
- Post Type (Reel, Image, Carousel)
- Time of Posting (Day, Evening, Night)
- Number of Hashtags
- Caption Length
- Engagement Label (High / Low)

---

## 🔹 Methodology
A rule-based approach is used:

- Posts with many hashtags (≥ 8) are likely to perform well
- Reels posted at night generally receive higher engagement
- Posts with longer captions may attract more interaction
- All other cases are classified as Low engagement

---

## 🔹 Features
✔ Simple rule-based classifier (if-else logic)  
✔ Built-in dataset (no external files required)  
✔ Real-time user input prediction (bonus feature)  
✔ Easy to understand and modify  

---

## 🔹 How to Run

1. Install Python (if not installed)
2. Save the file as `classifier.py`
3. Open terminal in the file location
4. Run: